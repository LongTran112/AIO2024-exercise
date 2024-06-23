import torch
import torch.nn as nn
import torch.nn.functional as F

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition
    
class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition

data1 = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output1 = softmax_stable(data1)
print(output1)


data2 = torch.Tensor([1, 2, 33])
my_softmax = MySoftmax()
output2 = my_softmax(data2)
print(output2)
