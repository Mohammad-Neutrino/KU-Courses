import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import json
from tqdm import tqdm
from scipy.ndimage import gaussian_filter1d

import matplotlib
matplotlib.rcParams.update({'font.size': 10})
font = {'weight' : 'bold', 'size'   : 10}
matplotlib.rc('font', **font)

# === Paths ===
PROCESSED_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "processed"))
MANUAL_LABEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "labels_manual"))
WEAK_LABEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "labels_weak"))
os.makedirs(WEAK_LABEL_DIR, exist_ok = True)

# === Config ===
N_WEAK_LABELS = 10
BLUR_SIGMA = 3  # smooth out jagged trace

def get_surface_line(img):
    # Row index with min pixel value in each column
    surface = np.argmin(img, axis = 0).astype(np.float32)
    surface_smooth = gaussian_filter1d(surface, sigma = BLUR_SIGMA)
    return surface_smooth

def surface_to_mask(surface_y, img_shape):
    mask = np.zeros(img_shape, dtype = np.uint8)
    for col, row in enumerate(surface_y):
        if 0 <= row < img_shape[0]:
            mask[int(row):, col] = 1
    return mask

def main():
    all_files = sorted([f for f in os.listdir(PROCESSED_DIR) if f.endswith(".npy")])
    manually_labeled = {f.replace(".png", ".npy") for f in os.listdir(MANUAL_LABEL_DIR)}
    to_label = [f for f in all_files if f not in manually_labeled][:N_WEAK_LABELS]

    print(f"Generating weak labels for {len(to_label)} echograms...\n")

    for fname in tqdm(to_label):
        fpath = os.path.join(PROCESSED_DIR, fname)
        img = np.load(fpath)

        surface_y = get_surface_line(img)
        mask = surface_to_mask(surface_y, img.shape)

        # Save binary mask
        mask_path = os.path.join(WEAK_LABEL_DIR, fname.replace(".npy", ".png"))
        Image.fromarray(mask * 255).save(mask_path)

        # Save surface trace
        trace_path = mask_path.replace(".png", ".json")
        with open(trace_path, "w") as f:
            json.dump(surface_y.tolist(), f)

    print("\n Weak label generation complete.")

if __name__ == "__main__":
    main()

