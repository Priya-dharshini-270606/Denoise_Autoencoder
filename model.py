import torch
import torch.nn as nn

class DnCNN(nn.Module):
    def __init__(self, channels=3):
        super(DnCNN, self).__init__()

        self.net = nn.Sequential(
            nn.Conv2d(channels, 64, 3, padding=1),
            nn.ReLU(),

            nn.Conv2d(64, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),

            nn.Conv2d(64, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),

            nn.Conv2d(64, channels, 3, padding=1)
        )

    def forward(self, x):
        noise = self.net(x)
        return x - noise
