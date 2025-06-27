import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from data_loader import EchogramDataset
from model import UNet
from eval import compute_iou, compute_f1, visualize_predictions
from tqdm import tqdm

# === Paths ===
PROCESSED_DIR = os.path.abspath(os.path.join("..", "data", "processed"))
WEAK_LABEL_DIR = os.path.abspath(os.path.join("..", "data", "labels_weak"))
MANUAL_LABEL_DIR = os.path.abspath(os.path.join("..", "data", "labels_manual"))

# === Config ===
BATCH_SIZE = 2
EPOCHS_WEAK = 5
EPOCHS_MANUAL = 10
LR = 1e-3
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_file_list(label_dir):
    return sorted([f.replace(".png", ".npy") for f in os.listdir(label_dir) if f.endswith(".png")])

bce = nn.BCEWithLogitsLoss()

def dice_loss(pred, target, smooth=1.0):
    pred = torch.sigmoid(pred)
    pred = pred.view(-1)
    target = target.view(-1)
    intersection = (pred * target).sum()
    return 1 - ((2. * intersection + smooth) / (pred.sum() + target.sum() + smooth))

def combined_loss(pred, target):
    return 0.5 * bce(pred, target) + 0.5 * dice_loss(pred, target)

def train(model, dataloader, optimizer, loss_fn):
    model.train()
    total_loss = 0
    for x, y in tqdm(dataloader, desc = "Training"):
        x, y = x.to(DEVICE), y.to(DEVICE)
        preds = model(x)
        loss = loss_fn(preds, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(dataloader)

def main():
    print(f"Using device: {DEVICE}")

    # === Load file lists ===
    weak_files = get_file_list(WEAK_LABEL_DIR)
    manual_files = get_file_list(MANUAL_LABEL_DIR)

    # === Datasets and Dataloaders ===
    weak_dataset = EchogramDataset(PROCESSED_DIR, WEAK_LABEL_DIR, weak_files)
    manual_dataset = EchogramDataset(PROCESSED_DIR, MANUAL_LABEL_DIR, manual_files)

    weak_loader = DataLoader(weak_dataset, batch_size = BATCH_SIZE, shuffle = True)
    manual_loader = DataLoader(manual_dataset, batch_size = BATCH_SIZE, shuffle = True)

    # === Model, Loss, Optimizer ===
    model = UNet(in_channels = 1, out_channels = 1).to(DEVICE)
    optimizer = optim.Adam(model.parameters(), lr = LR)

    # === Phase 1: Pretrain on weak labels ===
    print("\n Pretraining on weak labels...")
    for epoch in range(EPOCHS_WEAK):
        loss = train(model, weak_loader, optimizer, combined_loss)
        print(f"[Weak Epoch {epoch+1}] Loss: {loss:.4f}")

    # === Phase 2: Fine-tune on manual labels ===
    print("\n Fine-tuning on manual labels...")
    for epoch in range(EPOCHS_MANUAL):
        loss = train(model, manual_loader, optimizer, combined_loss)
        print(f"[Manual Epoch {epoch+1}] Loss: {loss:.4f}")

        # Visual eval
        eval_dir = f"../results/overlays/epoch_{epoch+1}"
        visualize_predictions(model, manual_loader, DEVICE, eval_dir, epoch + 1)

    # Save model
    os.makedirs("../results", exist_ok = True)
    torch.save(model.state_dict(), "../results/model_final.pth")
    print("Training complete. Model saved to results/model_final.pth")

if __name__ == "__main__":
    main()
	
