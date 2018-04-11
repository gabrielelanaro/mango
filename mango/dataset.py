from .base import Parameterized


class Dataset(Parameterized):
    pass


class SplitDataset(Dataset):

    def load(self):
        raise NotImplementedError()

    def train(self):
        raise NotImplementedError()

    def test(self):
        raise NotImplementedError()

    def transform_train(self, data):
        raise NotImplementedError()

    def transform_test(self, data):
        raise NotImplementedError()
