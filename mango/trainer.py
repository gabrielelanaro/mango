import numpy as np
import random

from typing import NamedTuple
from toolz import partition


from .base import Param, Parameterized


class Trainer(Parameterized):
    pass

class SimpleTrainer(Trainer):

    def __init__(self, model, loader, **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.loader = loader

    def train(self):
        self.build()

        self.loader.train()
        self.model.train(self.loader)

    def build(self):
        self.model.build()
        self.loader.build()


class MiniBatchTrainer(SimpleTrainer):

    epochs = Param(int, 10)

    def __init__(self, model, loader, epochs=10):
        super().__init__(model, loader, epochs=epochs)

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
