import os
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.nn.functional import sigmoid
from PIL import Image
from data_loader import EchogramDataset
from model import UNet
from eval import compute_iou, compute_f1
from torch.utils.data import DataLoader

import matplotlib
matplotlib.rcParams.update({'font.size': 10})
font = {'weight' : 'bold', 'size'   : 10}
matplotlib.rc('font', **font)

# === Config ===
MODEL_PATH = "../results/model_final.pth"
DATA_DIR = "../data/processed"
MANUAL_LABEL_DIR = "../data/labels_manual"
WEAK_LABEL_DIR = "../data/labels_weak"
SAVE_DIR = "../results/heldout_eval"
SAVE_PLOT = "../report/figs/heldout_set_performance.png"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

os.makedirs(SAVE_DIR, exist_ok=True)

# === Detect held-out files ===
all_files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".npy")])
manual_files = {f.replace(".png", ".npy") for f in os.listdir(MANUAL_LABEL_DIR)}
weak_files = {f.replace(".png", ".npy") for f in os.listdir(WEAK_LABEL_DIR)}
holdout_files = [f for f in all_files if f not in manual_files and f not in weak_files][:10]

print(f"Evaluating on held-out files: {holdout_files}")

# === Minimal Dataset Class for Inference ===
class HeldoutDataset(torch.utils.data.Dataset):
    def __init__(self, image_dir, file_list):
        self.image_dir = image_dir
        self.file_list = file_list

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        fname = self.file_list[idx]
        fpath = os.path.join(self.image_dir, fname)
        img = np.load(fpath).astype(np.float32)
        img_tensor = torch.from_numpy(img).unsqueeze(0)  # (1, H, W)
        return img_tensor, fname

# === Load model ===
model = UNet(in_channels = 1, out_channels = 1).to(DEVICE)
model.load_state_dict(torch.load(MODEL_PATH, map_location = DEVICE))
model.eval()

# === Load dataset ===
dataset = HeldoutDataset(DATA_DIR, holdout_files)
loader = DataLoader(dataset, batch_size = 1, shuffle = False)

iou_scores = []
f1_scores = []

with torch.no_grad():
    for x, fname in loader:
        x = x.to(DEVICE)
        pred = sigmoid(model(x)).cpu().numpy()[0, 0]
        pred_mask = pred > 0.5

        # Save overlay with just prediction
        img = x.cpu().numpy()[0, 0]
        H, W = img.shape

        fig, ax = plt.subplots(1, 2, figsize = (12, 5), constrained_layout = True)
        ax[0].imshow(img, cmap = "gray", aspect = "equal", extent = (0, W, H, 0))
        ax[0].set_title("Input Echogram", fontsize = 12, fontweight = 'bold')

        ax[1].imshow(img, cmap = "gray", aspect = "equal", extent = (0, W, H, 0))
        ax[1].imshow(pred_mask, cmap = "Blues", alpha = 0.5, extent = (0, W, H, 0))
        ax[1].set_title("Prediction", fontsize = 12, fontweight = 'bold')

        for a in ax:
            a.axis("off")

        save_path = os.path.join(SAVE_DIR, fname[0].replace(".npy", ".png"))
        plt.savefig(save_path, dpi = 400)
        plt.close()

        # Save prediction mask as PNG (optional)
        mask_img = Image.fromarray((pred_mask * 255).astype(np.uint8))
        mask_img.save(save_path.replace(".png", "_mask.png"))

print("\n Held-out evaluation complete. Overlays saved to:", SAVE_DIR)

