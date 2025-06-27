import os
import requests
from tqdm import tqdm

BASE_URL = "https://data.cresis.ku.edu/data/snow/2022_Greenland_P3/images/20220419_01/"

IMAGE_NAMES = [
    "20220419_01_008_1echo.jpg",
    "20220419_01_002_1echo.jpg",
    "20220419_01_005_1echo.jpg",
    # Add more if needed
]

# Absolute path from script to ../data/raw/
SAVE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "raw"))
os.makedirs(SAVE_DIR, exist_ok=True)

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    else:
        print(f"Failed to download {url} — status code {response.status_code}")
def main():
    print(f"Downloading {len(IMAGE_NAMES)} echograms to {SAVE_DIR}...\n")
    for name in tqdm(IMAGE_NAMES):
        url = BASE_URL + name
        save_path = os.path.join(SAVE_DIR, name)
        if not os.path.exists(save_path):
            download_image(url, save_path)
        else:
            print(f"{name} already exists, skipping.")
    print("\nDone.")

if __name__ == "__main__":
    main()

