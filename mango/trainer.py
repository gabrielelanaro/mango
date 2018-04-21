import numpy as np
import random

from typing import NamedTuple
from toolz import partition


from .base import Param, Parameterized
from .loaders import MiniBatchLoader

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
        self.model.train(self.loader.transform(self.loader.data))

    def build(self):
        self.model.build()
        self.loader.build()


class MiniBatchTrainer(SimpleTrainer):

    epochs = Param(int, 10)

    def __init__(self, model, loader, epochs=10):
        super().__init__(model, loader, epochs=epochs)
        self._validate_loader(loader)
        self._validate_model(model)

    def train(self):
        self.model.build()
        self.loader.build()

        for j in range(self.epochs):
            self.loader.train()
            for i, batch in enumerate(self.loader):
                step_info = StepInfo(step=i,
                                     max_steps=len(self.loader),
                                     epoch=j,
                                     max_epoch=self.epochs,
                                     global_step=i + j * len(self.loader))
                self.model.batch(batch, step_info)
            self.model.epoch(step_info, self.loader)

    def _validate_loader(self, loader):
        if not isinstance(loader, MiniBatchLoader):
            raise ValueError(f'Loader {type(loader).__name__} must be MiniBatchLoader')

    def _validate_model(self, model):
        if not hasattr(model, 'batch'):
            raise ValueError(f'Model {type(model).__name__} must have a "batch" method')

        if not hasattr(model, 'epoch'):
            raise ValueError(f'Model {type(model).__name__} must have an "epoch" method')


class StepInfo(NamedTuple):
    step: int
    max_steps: int
    epoch: int
    max_epoch: int
    global_step: int
