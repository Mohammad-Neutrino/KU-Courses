import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from PIL import Image
import json

import matplotlib
matplotlib.rcParams.update({'font.size': 10})
font = {'weight' : 'bold', 'size'   : 10}
matplotlib.rc('font', **font)

# Paths 
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "processed"))
SAVE_MASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "labels_manual"))
os.makedirs(SAVE_MASK_DIR, exist_ok=True)

def save_label_mask(surface_y, img_shape, save_path):
    mask = np.zeros(img_shape, dtype=np.uint8)
    for col, row in enumerate(surface_y):
        if 0 <= row < img_shape[0]:
            mask[int(row):, col] = 1  # Fill below the surface
    Image.fromarray(mask * 255).save(save_path)

def main():
    files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".npy")])[:10]
    print(f"Labeling {len(files)} echograms manually...")

    for fname in files:
        fpath = os.path.join(DATA_DIR, fname)
        img = np.load(fpath)

        surface_clicks = []

        fig, ax = plt.subplots(figsize = (10, 6))
        ax.imshow(img, cmap = "gray", aspect = "auto")
        ax.set_title(f"Manual Labels (Clicks) Along the Surface of Echogram", fontweight = 'bold')
        ax.set_xlabel("Range Pixel")
        ax.set_ylabel("Depth Pixel")
        plt.show()

        fig, ax = plt.subplots(figsize = (10, 6))
        ax.imshow(img, cmap = "gray", aspect = "auto")
        ax.set_title(f"Manual Labels (Clicks) Along the Surface of Echogram", fontweight = 'bold')
        ax.set_xlabel("Range Pixel")
        ax.set_ylabel("Depth Pixel")
        clicked_dots, = ax.plot([], [], 'ro', markersize = 4)

        def onclick(event):
            if event.xdata is not None and event.ydata is not None:
                surface_clicks.append((event.xdata, event.ydata))
                update_plot()

        def onkey(event):
            if event.key == 'u' or event.key == 'backspace':
                if surface_clicks:
                    surface_clicks.pop()
                    update_plot()

        def update_plot():
            if surface_clicks:
                x, y = zip(*surface_clicks)
                clicked_dots.set_data(x, y)
            else:
                clicked_dots.set_data([], [])
            fig.canvas.draw_idle()

        cid_click = fig.canvas.mpl_connect('button_press_event', onclick)
        cid_key = fig.canvas.mpl_connect('key_press_event', onkey)

        plt.show()

        fig.canvas.mpl_disconnect(cid_click)
        fig.canvas.mpl_disconnect(cid_key)

        if len(surface_clicks) < 2:
            print("Not enough points clicked. Skipping.")
            continue

        surface_clicks.sort()
        x, y = zip(*surface_clicks)
        interp_fn = interp1d(x, y, kind='linear', bounds_error=False, fill_value='extrapolate')
        full_x = np.arange(img.shape[1])
        full_y = interp_fn(full_x)

        # Save mask
        save_mask_path = os.path.join(SAVE_MASK_DIR, fname.replace(".npy", ".png"))
        save_label_mask(full_y, img.shape, save_mask_path)

        # Save trace as JSON (optional)
        save_json_path = save_mask_path.replace(".png", ".json")
        with open(save_json_path, "w") as f:
            json.dump(full_y.tolist(), f)

        print(f"Saved mask and surface trace: {fname}")

if __name__ == "__main__":
    main()

