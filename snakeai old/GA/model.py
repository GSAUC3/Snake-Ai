import torch,os
from torch import nn 


class Snakenet(nn.Module):
    def __init__(self,inputs=13) -> None:
        super(Snakenet,self).__init__()

        self.brain= nn.Sequential(
            nn.Linear(inputs,16,bias=False),
            nn.ReLU(),
            nn.Linear(16,8,bias=False),
            nn.ReLU(),
            nn.Linear(8,4,bias=False)
        )
        # self.brain = nn.Linear(inputs,4)
    def forward(self,x):
        x = self.brain(x)
        x = torch.softmax(x,dim=0)
        return x

    def save(self,filename='model.pth'):
        path = './model/'
        if not os.path.exists(path):
            os.makedirs(path)
        filename = os.path.join(path,filename)
        torch.save(self.state_dict(),filename)
