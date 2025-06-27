import os
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.nn.functional import sigmoid

import matplotlib
matplotlib.rcParams.update({'font.size': 10})
font = {'weight' : 'bold', 'size'   : 10}
matplotlib.rc('font', **font)

def compute_iou(preds, targets, threshold = 0.5):
    preds_bin = preds > threshold
    targets_bin = targets > threshold
    intersection = np.logical_and(preds_bin, targets_bin).astype(float).sum()
    union = np.logical_or(preds_bin, targets_bin).astype(float).sum()
    return (intersection / union) if union > 0 else 0.0

def compute_f1(preds, targets, threshold = 0.5):
    preds_bin = preds > threshold
    targets_bin = targets > threshold
    tp = np.logical_and(preds_bin, targets_bin).astype(float).sum()
    fp = np.logical_and(preds_bin, np.logical_not(targets_bin)).astype(float).sum()
    fn = np.logical_and(np.logical_not(preds_bin), targets_bin).astype(float).sum()
    return (2 * tp / (2 * tp + fp + fn)) if (tp + fp + fn) > 0 else 0.0

def visualize_predictions(model, dataloader, device, save_dir, epoch):

    model.eval()
    os.makedirs(save_dir, exist_ok = True)

    with torch.no_grad():
        for idx, (x, y) in enumerate(dataloader):
            x = x.to(device)
            y = y.to(device)

            preds = sigmoid(model(x)).cpu().numpy()
            inputs = x.cpu().numpy()
            labels = y.cpu().numpy()

            for i in range(min(len(inputs), 3)):
                img = inputs[i][0]
                pred_mask = preds[i][0] > 0.5
                true_mask = labels[i][0] > 0.5
                H, W = img.shape

                # Compute metrics
                iou = compute_iou(pred_mask, true_mask)
                f1 = compute_f1(pred_mask, true_mask)

                # Plot
                fig, ax = plt.subplots(1, 3, figsize = (18, 6), constrained_layout = True)

                ax[0].imshow(img, cmap = "gray", aspect = "equal", extent = (0, W, H, 0))
                ax[0].set_title("Input Echogram", fontsize = 12, fontweight = 'bold')

                ax[1].imshow(img, cmap = "gray", aspect = "equal", extent = (0, W, H, 0))
                ax[1].imshow(true_mask, cmap = "Reds", alpha = 0.5, extent = (0, W, H, 0))
                ax[1].set_title("Ground Truth", fontsize = 12, fontweight = 'bold')

                ax[2].imshow(img, cmap = "gray", aspect = "equal", extent = (0, W, H, 0))
                ax[2].imshow(pred_mask, cmap = "Blues", alpha = 0.5, extent = (0, W, H, 0))
                ax[2].set_title(f"Prediction\nIoU: {iou:.3f}, F1: {f1:.3f}", fontsize = 12, fontweight = 'bold')

                for a in ax:
                    a.axis("off")

                save_path = os.path.join(save_dir, f"epoch{epoch}_sample{idx}_{i}.png")
                plt.savefig(save_path, dpi = 400)
                plt.close()

