from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import ImageFolder
# self
from dataset import Dataset

# transforms
normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
transform = transforms.Compose([
    transforms.Resize(224),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    normalize
])

# torchvision ImageFolder
img_folder = '../data/icon/'
# train_dataset = ImageFolder(img_folder + 'train/', transform=transform)
# test_dataset = ImageFolder(img_folder + 'test/', transform=transform)
train_dataset = Dataset(img_folder + 'train/', transforms=transform)
test_dataset = Dataset(img_folder + 'test/', transforms=transform)

idx2class = train_dataset.idx2class
class2idx = train_dataset.class2idx
# print(idx2class)

print('Train: ', len(train_dataset))
print('Test: ', len(test_dataset))

# preparing train loader
train_loader = DataLoader(train_dataset, batch_size=16, shuffle=False,
    num_workers=0, pin_memory=True)
test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False,
    num_workers=0, pin_memory=True)

print('Datasets load success!')