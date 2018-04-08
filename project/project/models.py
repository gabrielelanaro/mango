from mango import Model
import numpy as np


class StupidModel(Model):

    const: float

    def train(self, X, y):

        for i, x in enumerate(X):
            self.reporter.add_scalar('loss', x**2, i)
            self.reporter.add_embedding('embedding',
                                        np.random.rand(32, 26),
                                        labels=['hello'] * 32,
                                        iteration=i)
            self.reporter.add_histogram('histogram', np.random.rand(32, 25, 26), iteration=i)

    def predict(self, X):
        return [self.const] * len(X)
