import torch
import visdom

class Vis:
    def __init__(self, env):
        self.vis = visdom.Visdom(env=env, use_incoming_socket=False)

        # empty
        self.vis.line(X=torch.Tensor([0]), Y=torch.Tensor([0]),
                win='train_loss',
                opts={'title': 'train_loss', 'xlabel':'batch', 'ylabel':'error'})
        self.vis.line(X=torch.Tensor([0]), Y=torch.Tensor([0]),
                 win='test_acc',
                 opts={'title': 'test_acc', 'xlabel':'epoch', 'ylabel':'acc(%)'})
        self.vis.text('==========Start Training==========',win='status')

    def update_train(self, x, y, status):
        self.vis.line(X=x, Y=y, win='train_loss', update='append',
                 opts={'title': 'train_loss', 'xlabel':'batch', 'ylabel':'error'})
        self.vis.text(status, win='status')

    def update_test(self, x, y, status):
        self.vis.line(X=x, Y=y, win='test_acc', update='append',
                opts={'title': 'test_acc', 'xlabel':'epoch', 'ylabel':'acc(%)'})
        self.vis.text(status, win='status')
