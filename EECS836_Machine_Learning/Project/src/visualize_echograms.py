import os
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({'font.size': 10})
font = {'weight' : 'bold', 'size'   : 10}
matplotlib.rc('font', **font)

# Set your path to processed echograms
data_dir = "../data/processed"  # Adjust if needed
sample_files = sorted([f for f in os.listdir(data_dir) if f.endswith(".npy")])[:5]

for fname in sample_files:
    fpath = os.path.join(data_dir, fname)
    echogram = np.load(fpath)

    plt.figure(figsize = (10, 6))
    plt.imshow(echogram, cmap = "gray", aspect = "auto")
    plt.title(f"Reconstructed (Cropped, Enhanced, Normalized) Echogram", fontweight = 'bold')
    plt.xlabel("Range Pixel")
    plt.ylabel("Depth Pixel")
    plt.colorbar(label = "Intensity")
    plt.tight_layout()
    plt.show()
