from paintstorch.network import Generator, Illustration2Vec

import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F


class PaintsTorch2(nn.Module):
    def __init__(self, features: int, g: str, f1: str, bn: bool) -> None:
        super(PaintsTorch2, self).__init__()

        ckpt = torch.load(args.model)
        G = nn.DataParallel(Generator(features, bn=bn))
        G.load_state_dict(ckpt["G"] if "G" in ckpt.keys() else ckpt)
        
        self.G = G.module.eval().cpu()
        self.F1 = Illustration2Vec(f1).eval().cpu()

        for param in self.G.parameters():
            param.requires_grad = False
        for param in self.F1.parameters():
            param.requires_grad = False

    @torch.no_grad()
    def forward(self, x: torch.Tensor, h: torch.Tensor) -> torch.Tensor:
        mask = x[:, -1].unsqueeze(1)
        y, *_ = self.G(x, h, self.F1(x))
        y = x[:, :3] * (1 - mask) + y * mask
        return y


parser = argparse.ArgumentParser()
parser.add_argument("--features", type=int, default=32)
parser.add_argument("--model",    type=str, required=True)
parser.add_argument("--save",     type=str, required=True)
parser.add_argument("--bn",       action="store_true")
args = parser.parse_args()


model = PaintsTorch2(args.features, args.model, "./models/i2v.pth", args.bn)
model = model.eval()

fake = torch.zeros((1, 4, 512, 512)), torch.zeros((1, 4, 128, 128))

torch.onnx.export(
    model,
    fake,
    args.save,
    verbose=True,
    input_names=["input", "hints"],
    output_names=["illustration"],
    opset_version=9,
    do_constant_folding=True,
)