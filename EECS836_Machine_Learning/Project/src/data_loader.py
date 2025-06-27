import os
import torch
from torch.utils.data import Dataset
import numpy as np
from PIL import Image

class EchogramDataset(Dataset):
    def __init__(self, image_dir, label_dir, file_list, transform=None):
        self.image_dir = image_dir
        self.label_dir = label_dir
        self.file_list = file_list
        self.transform = transform

    def __len__(self):
        return len(self.file_list)

    def __getitem__(self, idx):
        fname = self.file_list[idx]
        image_path = os.path.join(self.image_dir, fname)
        label_path = os.path.join(self.label_dir, fname.replace('.npy', '.png'))

        image = np.load(image_path).astype(np.float32)  # shape: (H, W)
        label = np.array(Image.open(label_path)) > 127  # binarize

        # Add channel dim: (1, H, W)
        image = torch.from_numpy(image).unsqueeze(0)
        label = torch.from_numpy(label.astype(np.float32)).unsqueeze(0)

        if self.transform:
            image, label = self.transform(image, label)

        return image, label

