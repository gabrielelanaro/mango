from typing import NamedTuple
import random
from toolz import partition
import numpy as np

class CrossValidationTrainer:

    def __init__(self, model, dataset):
        self.model = model
        self.dataset = dataset

    def train(self):
        self.model.train(self.dataset.X, self.dataset.y)


class MiniBatchTrainer:

    batch_size: int
    epochs: int

    def __init__(self, model, dataset, batch_size=32, epochs=10):
        self.model = model
        self.dataset = dataset
        self.batch_size = batch_size
        self.epochs = epochs

    def train(self):
        loader = MiniBatchLoader(self.dataset, batch_size=self.batch_size)

        for j in range(self.epochs):
            for i, batch in enumerate(loader):
                step_info = StepInfo(step=i,
                                     max_steps=len(loader),
                                     epoch=j,
                                     max_epoch=self.epochs,
                                     global_step=i + j * len(loader))
                self.model.batch(batch, step_info)
            self.model.epoch(step_info)


class MiniBatchLoader:

    def __init__(self, dataset, batch_size):
        self.batch_size = batch_size
        self.dataset = dataset

    def __iter__(self):
        size = len(self.dataset)
        randomized = list(range(size))
        random.shuffle(randomized)

        for batch in partition(self.batch_size, randomized):
            if len(batch) == 0:
                continue

            yield self._reduce([self.dataset[b] for b in batch])

    def __len__(self):
        return len(self.dataset) // self.batch_size

    def _reduce(self, items):
        if len(items) == 0:
            raise ValueError("Can't reduce")
        else:
            proto = items[0]
            return {key: np.array([i[key] for i in items])
                    for key in proto.keys()}


class StepInfo(NamedTuple):
    step: int
    max_steps: int
    epoch: int
    max_epoch: int
    global_step: int
