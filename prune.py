import torch
from torch.nn.utils import prune

def prune_icnet(model, method='std', s=0.25):
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Conv2d):
            # Prune the Conv2d layers
            prune.ln_structured(module, name='weight', amount=s, n=2, dim=1)
        elif isinstance(module, torch.nn.Linear):
            # Prune the Linear layers
            prune.ln_structured(module, name='weight', amount=s, n=2, dim=1)




