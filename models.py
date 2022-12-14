import torch
import torch.nn as nn
import torch.nn.functional as F
from torch import optim

class Actor(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Actor,self).__init__()
        self.linear1 = nn.Linear(input_size,hidden_size)
        self.linear2 = nn.Linear(hidden_size,hidden_size)
        self.linear3 = nn.Linear(hidden_size,output_size)

    def forward(self, state):
        x = F.relu(self.linear1(state.float()))
        x = F.relu(self.linear2(x))
        x = torch.tanh(self.linear3(x))
        return x

class Critic(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Critic,self).__init__()
        self.linear1 = nn.Linear(input_size,hidden_size)
        self.linear2 = nn.Linear(hidden_size,hidden_size)
        self.linear3 = nn.Linear(hidden_size,output_size)

    def forward(self, state, action):
        x = torch.cat([state, action],1).float()
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = self.linear3(x)
        return x
