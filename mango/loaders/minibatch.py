import random

from toolz import partition

from ..base import Param, Parameterized


class MiniBatchLoader(Parameterized):

    batch_size = Param(int)

    def __init__(self, dataset, batch_size):
        super().__init__(batch_size=batch_size)
        self.batch_size = batch_size
        self.dataset = dataset

    def build(self):
        self.dataset.build()

    def train(self):
        self.data = self.dataset.train()
        self.transform = self.dataset.transform_train

    def test(self):
        self.data = self.dataset.test()
        self.transform = self.dataset.transform_test

    def __iter__(self):
        size = len(self.data)
        randomized = list(range(size))
        random.shuffle(randomized)

        for batch in partition(self.batch_size, randomized):
            if len(batch) == 0:
                continue

            yield self.transform([self.data[b] for b in batch])

    def __len__(self):
        return len(self.data) // self.batch_size
