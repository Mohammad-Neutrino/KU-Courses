import os
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.nn.functional import sigmoid
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
LABEL_DIR = "../data/labels_manual"
SAVE_PLOT = "../report/figs/manual_set_performance.png"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def main():
    # === Load model ===
    model = UNet(in_channels = 1, out_channels = 1).to(DEVICE)
    model.load_state_dict(torch.load(MODEL_PATH, map_location = DEVICE))
    model.eval()

    # === Load dataset ===
    file_list = sorted([f.replace(".png", ".npy") for f in os.listdir(LABEL_DIR) if f.endswith(".png")])
    dataset = EchogramDataset(DATA_DIR, LABEL_DIR, file_list)
    loader = DataLoader(dataset, batch_size = 1, shuffle = False)

    iou_scores, f1_scores = [], []
    file_names = []

    with torch.no_grad():
        for (x, y), fname in zip(loader, file_list):
            x = x.to(DEVICE)
            y = y.to(DEVICE)
            pred = sigmoid(model(x)).cpu().numpy()[0, 0]
            true = y.cpu().numpy()[0, 0]
            iou = compute_iou(pred, true)
            f1 = compute_f1(pred, true)
            iou_scores.append(iou)
            f1_scores.append(f1)
            file_names.append(fname.replace(".npy", ""))

    # === Sort and plot ===
    sorted_idxs = np.argsort(iou_scores)
    iou_sorted = np.array(iou_scores)[sorted_idxs]
    f1_sorted = np.array(f1_scores)[sorted_idxs]
    file_sorted = np.array(file_names)[sorted_idxs]

    x = np.arange(len(file_sorted))
    plt.figure(figsize = (10, 5))
    plt.yscale('log')
    plt.bar(x - 0.2, iou_sorted, width = 0.4, label = 'IoU', alpha = 0.5, edgecolor = 'g', facecolor = 'lime', ls = 'solid')
    plt.bar(x + 0.2, f1_sorted, width = 0.4, label = 'F1 Score', alpha = 0.5, edgecolor = 'k', facecolor = 'gray', ls = 'dashed')
    plt.axhline(1, color = 'r', ls = 'dotted')
    plt.ylabel("Score", fontweight = 'bold')
    plt.xlabel("Manual Label Sample Index (Sorted by IoU)", fontweight = 'bold')
    plt.title("Final Model Performance on Manual Labels", fontweight = 'bold')
    plt.xticks(x, fontsize = 10)
    plt.ylim(0.8, 1.05)
    plt.legend()
    plt.tight_layout()
    os.makedirs(os.path.dirname(SAVE_PLOT), exist_ok = True)
    plt.savefig(SAVE_PLOT, dpi = 400)
    plt.close()
    print(f"Saved performance plot to: {SAVE_PLOT}")

if __name__ == "__main__":
    main()

