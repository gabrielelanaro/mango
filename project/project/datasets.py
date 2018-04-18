from mango.dataset import SplitDataset

class StupidDataset(SplitDataset):

    def build(self):
        self.X_train = [0, 1, 2, 3, 4, 5]
        self.y_train = [0, 1, 2, 3, 4, 5]

    def train(self):
        return {'X': self.X_train, 'y': self.y_train}

    def eval(self):
        return {'y': self.X_train}


class IndexedDataset(SplitDataset):

    def build(self):
        self.data = []
