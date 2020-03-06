# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 08:10:16 2020

@author: nsde
"""

import torch
from pytorch_metrics import Metric

class MeanSquaredError(Metric):
    
    def reset(self):
        self._squared_error = 0
        self._n = 0
        
    def update(self, target, pred):
        self._squared_error += torch.pow(pred - target, 2).sum().item()
        self._n += target.shape[0]
        
    def compute(self):
        if self._n == 0:
            raise RuntimeError('Must have one sample, before compute can be called')
        return self._squared_error / self._n