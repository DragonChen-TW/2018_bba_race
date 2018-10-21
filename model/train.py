import torch
from torch import nn
from torch.autograd import Variable
import torch.functional as F
from torch.optim import Adam
from torchvision.models import resnet50
# self
from vis import Vis
from dataset import train_loader, test_loader, idx2class, class2idx
from test import test

def train(epoch, model, train_loader, criterion):
    model.train()
    for i, (data, label) in enumerate(train_loader):
        data = Variable(data).cuda() # gpu
        label = Variable(label).cuda() # gpu

        optimizer.zero_grad()

        output = model(data)

        loss = criterion(output, label)
        loss.backward()
        optimizer.step()

        if i % 10 == 0:
            status = 'Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch + 1, i * len(data), len(train_loader.dataset),
                100. * i / len(train_loader), loss.item())
            print(status)
            vis.update_train(x=torch.Tensor([epoch + i/len(train_loader)]),
                             y=torch.Tensor([loss.item()]), status=status)

if __name__ == '__main__':
    # load data and init
    # traint_loader test_loader
    vis = Vis('bba_race resnet')

    # model
    model = resnet50()
    input_size = model.fc.in_features
    model.fc = nn.Linear(input_size, len(idx2class)) # output 20 category

    # load exist
    checkpoints = 'checkpoints/res_net50_0_0.07.pt'
    if checkpoints:
        model.load_state_dict(torch.load(checkpoints)) # load exist model
    model.cuda() # gpu

    # criterion, optimizer
    criterion = nn.CrossEntropyLoss().cuda() # gpu
    optimizer = Adam(model.parameters(), lr=0.001)

    epoches = 15
    for epoch in range(epoches):
        train(epoch, model, train_loader, criterion)
        # save the model
        torch.save(model.state_dict(), 'checkpoints/res_net50_{}.pt'.format(epoch))
        test(model, test_loader)

    # save the model
    torch.save(model.state_dict(), 'checkpoints/res_net50.pt')
