from mango import Dataset

class StupidDataset(Dataset):

    def load(self):
        self.X = [0, 1, 2, 3, 4, 5]
        self.y = [0, 1, 2, 3, 4, 5]

    def train(self):
        return Transform(self.X_train)

    def eval(self):
        return self.y_train


class IndexedDataset(Dataset):

    def load(self):
        self.data = []
