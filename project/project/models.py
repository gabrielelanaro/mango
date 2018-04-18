from mango import Model, Param
import numpy as np
from sklearn.linear_model import LogisticRegression

class StupidModel(Model):

    alpha = Param(float, default=0.1)
    const = Param(float)

    def train(self, data):
        X = data['X']
        y = data['y']

        for i, x in enumerate(X):
            self.reporter.add_scalar('loss', x**2, i)
            self.reporter.add_embedding('embedding',
                                        np.random.rand(32, 26),
                                        labels=['hello'] * 32,
                                        iteration=i)
            self.reporter.add_histogram('histogram', np.random.rand(32, 25, 26), iteration=i)

    def predict(self, data):
        return [self.const] * len(data['X'])
