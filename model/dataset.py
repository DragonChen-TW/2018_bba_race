import torch
from torch.utils import data
import os
import json
from PIL import Image
# self
import vars

def pil_loader(path):
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('RGB')

class Dataset(data.Dataset):
    def __init__(self, root, transforms=None, return_class=True):
        # img
        imgs = [img for img in os.listdir(root) if '.' in img] # just file
        self.imgs = [os.path.join(root, img) for img in imgs]
        # label
        json_file = vars.data_path + 'json/google_play_all.json'
        with open(json_file) as f:
            data = json.load(f)
        self.labels = [int(d['Installs']) for d in data]
        self.return_class = return_class

        idx2class = set(self.labels)
        self.idx2class = [str(i) for i in sorted([int(i) for i in idx2class])]
        self.class2idx = {int(c):i for i, c in enumerate(self.idx2class)}

        self.transforms = transforms

    def __getitem__(self, index):
        img_path = self.imgs[index]
        img = pil_loader(img_path)
        if self.transforms:
            img = self.transforms(img)

        true_idx = int(img_path.split('/')[-1].replace('.jpg',''))
        label = self.labels[true_idx]
        if self.return_class:
            label = self.class2idx[label]

        return img, label
    def __len__(self):
        return len(self.imgs)

if __name__ == '__main__':
    dataset = Dataset(vars.icon_path + 'train/')

    for i in range(10):
        img, label = dataset[i]
        print(img.size, label)
