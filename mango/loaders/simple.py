from ..base import Param, Parameterized


class SimpleLoader(Parameterized):

    def __init__(self, dataset):
        super().__init__()
        self.dataset = dataset

    def build(self):
        self.dataset.build()

    def train(self):
        self._data = self.dataset.train()
        self._transform = self.dataset.transform_train

    def test(self):
        self._data = self.dataset.test()
        self._transform = self.dataset.transform_test

    def __iter__(self):
        yield from self._data

    def __len__(self):
        return len(self._data)
