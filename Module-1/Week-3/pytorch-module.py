import torch
import torch.nn as nn
import torch.nn.functional as F

class CustomSoftmax(nn.Module):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Define layers
        self.fc1 = nn.Linear(1, 10)
        self.fc2 = nn.Linear(10, 5)
        self.fc3 = nn.Linear(5, 1)

    def forward(self, x):
        # Define the activation functions
        x = F.softmax(self.fc1(x), dim=1)
        x = F.softmax(self.fc2(x), dim=1)
        x = self.fc3(x)
        return x 

model_softmax = CustomSoftmax()
print(model_softmax)

print("========="*10)

# example_input = torch.randn(32, 1)
# print(example_input)
# print("========="*20)
# print(model_softmax(example_input))

input1 = torch.Tensor([1, 2, 3])
print(input1)
input1 = input1.view(-1, 1)
print(input1)
output1 = model_softmax(input1)
print(round(output1[0].item(), 2))
