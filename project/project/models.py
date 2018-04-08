from mango import Model

class StupidModel(Model):

    const = 0.0

    def train(self, X, y):

        for i, x in enumerate(X):
            self.reporter.add_scalar('loss', x**2, i)

    def predict(self, X):
        return [self.const] * len(X)
