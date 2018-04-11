from .base import Param, Parameterized
from typing import NamedTuple
import random
from toolz import partition
import numpy as np


class Trainer(Parameterized):
    pass


class SimpleTrainer(Trainer):

    def __init__(self, model, loader):
        self.model = model
        self.loader = loader

    def train(self):
        self.loader.train()
        self.model.train(self.loader)


class MiniBatchTrainer(Trainer):

    epochs = Param(int, 10)

    def __init__(self, model, loader, epochs=10):
        super().__init__(epochs=epochs)
        self.model = model
        self.loader = loader

    def train(self):
        for j in range(self.epochs):
            self.loader.train()
            for i, batch in enumerate(loader):
                step_info = StepInfo(step=i,
                                     max_steps=len(loader),
                                     epoch=j,
                                     max_epoch=self.epochs,
                                     global_step=i + j * len(loader))
                self.model.batch(batch, step_info)
            self.model.epoch(step_info, self.loader)


class StepInfo(NamedTuple):
    step: int
    max_steps: int
    epoch: int
    max_epoch: int
    global_step: int
