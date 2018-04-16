from .base import Parameterized


class Dataset(Parameterized):
    pass


class SplitDataset(Dataset):

    def build(self):
        raise NotImplementedError()

    def train(self):
        raise NotImplementedError()

    def test(self):
        raise NotImplementedError()

    def transform_train(self, data):
        return data

    def transform_test(self, data):
        return data
