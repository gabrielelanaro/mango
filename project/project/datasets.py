from mango import Dataset



class StupidDataset(Dataset):

    def load(self):
        self.X = [0, 1, 2, 3, 4, 5]
        self.y = [0, 1, 2, 3, 4, 5]


class IndexedDataset(Dataset):

    def load(self):
        self.data = []
