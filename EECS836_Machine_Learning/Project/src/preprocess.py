import os
import numpy as np
from PIL import Image
from tqdm import tqdm

# === Paths ===
RAW_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "raw"))
SAVE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "processed"))
os.makedirs(SAVE_DIR, exist_ok=True)

# === Config ===
CROP_BOX = (162, 72, 1080, 812)  # (left, top, right, bottom) – adjust if needed
RESIZE_SHAPE = (256*4, 512*4)    # (height, width)

def preprocess_image(image_path):
    img = Image.open(image_path).convert("L")  # Convert to grayscale
    cropped = img.crop(CROP_BOX)               # Crop echogram only
    resized = cropped.resize((RESIZE_SHAPE[1], RESIZE_SHAPE[0]))  # Resize (W, H) for PIL
    img_array = np.array(resized, dtype=np.float32) / 255.0        # Normalize to [0, 1]
    return img_array

def main():
    jpg_files = [f for f in os.listdir(RAW_DIR) if f.endswith(".jpg")]
    print(f"Found {len(jpg_files)} raw echograms.")

    for fname in tqdm(jpg_files, desc="Preprocessing"):
        full_path = os.path.join(RAW_DIR, fname)
        img_array = preprocess_image(full_path)
        save_name = os.path.splitext(fname)[0] + ".npy"
        np.save(os.path.join(SAVE_DIR, save_name), img_array)

    print("Preprocessing complete. Cropped and resized images saved to data/processed/.")

if __name__ == "__main__":
    main()

