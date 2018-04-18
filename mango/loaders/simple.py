from ..base import Param, Parameterized


class SimpleLoader(Parameterized):

    def __init__(self, dataset):
        super().__init__()
        self.dataset = dataset

    def build(self):
        self.dataset.build()

    def train(self):
        self.data = self.dataset.train()
        self.transform = self.dataset.transform_train

    def test(self):
        self.data = self.dataset.test()
        self.transform = self.dataset.transform_test
