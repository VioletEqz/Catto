import os
import pandas as pd
from torchvision.io import read_image
from torch.utils.data import Dataset

class CatDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.img_labels = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.root_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        return image, label