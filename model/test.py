import torch
from torch import nn
from torch.autograd import Variable
import torch.functional as F
from torch.optim import Adam
from torchvision.models import resnet50
# self
from vis import Vis
from dataset import test_loader, idx2class, class2idx

def test(model, test_loader):
    model.eval()
    test_loss = 0
    correct = 0
    for i, (data, label) in enumerate(test_loader):
        data = Variable(data).cuda() # gpu
        label = Variable(label).cuda() # gpu
        output = model(data)

        # sum up batch loss
        test_loss += criterion(output, label).item()
        # get the index of max
        pred = output.data.max(1, keepdim=True)
        print(pred)
        pred = pred[1]
        correct += pred.eq(label.data.view_as(pred)).cuda().sum() # gpu

        if i % 10 == 0:
            status = 'Test: [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                i * len(data), len(test_loader.dataset),
                100. * i / len(test_loader), test_loss)
            print(status)

    test_loss /= len(test_loader.dataset)
    status = '\nTest avg loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset))
    print(status)
    vis.update_test(x=torch.Tensor([epoch]),
                    y=torch.Tensor([100. * correct / len(test_loader.dataset)]),
                    status=status)

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

    # criterion
    criterion = nn.CrossEntropyLoss().cuda() # gpu

    test(model, test_loader)
