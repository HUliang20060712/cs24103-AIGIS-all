"""U-Net 模型定义（实验四接入 PyTorch，当前为结构骨架）

参考：Ronneberger et al., U-Net: Convolutional Networks for Biomedical Image Segmentation
本模块用于遥感影像地物分割，num_classes=6（建筑/植被/水体/道路/裸地/其他）。
"""
import torch
import torch.nn as nn


class DoubleConv(nn.Module):
    """(Conv2d -> BatchNorm -> ReLU) x 2"""
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.block = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, padding=1, bias=False),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, padding=1, bias=False),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
        )

    def forward(self, x):
        return self.block(x)


class UNet(nn.Module):
    """U-Net 编码器-解码器结构。

    实验四在此基础上实现：
      - Encoder: 两次下采样（MaxPool2d）
      - Bottleneck
      - Decoder: 两次上采样（ConvTranspose2d）+ skip connection
      - Final: 1x1 Conv 输出 num_classes 通道
    """
    def __init__(self, in_channels=3, num_classes=6, base_ch=64):
        super().__init__()
        # 实验四：按标准 U-Net 结构搭建
        self.enc1 = DoubleConv(in_channels, base_ch)
        self.enc2 = DoubleConv(base_ch, base_ch * 2)
        self.bottleneck = DoubleConv(base_ch * 2, base_ch * 4)
        self.dec2 = DoubleConv(base_ch * 4 + base_ch * 2, base_ch * 2)
        self.dec1 = DoubleConv(base_ch * 2 + base_ch, base_ch)
        self.out_conv = nn.Conv2d(base_ch, num_classes, 1)
        self.pool = nn.MaxPool2d(2)
        self.up2 = nn.ConvTranspose2d(base_ch * 4, base_ch * 2, 2, stride=2)
        self.up1 = nn.ConvTranspose2d(base_ch * 2, base_ch, 2, stride=2)

    def forward(self, x):
        # 实验四：实现 skip connection 拼接
        e1 = self.enc1(x)
        e2 = self.enc2(self.pool(e1))
        b = self.bottleneck(self.pool(e2))
        d2 = self.dec2(torch.cat([self.up2(b), e2], dim=1))
        d1 = self.dec1(torch.cat([self.up1(d2), e1], dim=1))
        return self.out_conv(d1)
