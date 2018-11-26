from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import ImageFolder
# self
import vars
from dataset import Dataset

def get_data_loader(return_class=True):
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
    img_folder = vars.icon_path
    # train_dataset = ImageFolder(img_folder + 'train/', transform=transform)
    # test_dataset = ImageFolder(img_folder + 'test/', transform=transform)
    train_dataset = Dataset(img_folder + 'train/', transforms=transform, return_class=return_class)
    test_dataset = Dataset(img_folder + 'test/', transforms=transform, return_class=return_class)

    print('Train: ', len(train_dataset))
    print('Test: ', len(test_dataset))

    # preparing train loader
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=False,
        num_workers=0, pin_memory=True)
    test_loader = DataLoader(test_dataset, batch_size=16, shuffle=False,
        num_workers=0, pin_memory=True)

    print('Datasets load success!')

    return train_loader, test_loader
