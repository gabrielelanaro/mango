class CombinedReporter:

    def __init__(self, reporters):
        self.reporters = reporters

    def add_scalar(self, name, value, iteration):
        [r.add_scalar(name, value, iteration) for r in self.reporters if hasattr(r, 'add_scalar')]

    def add_embedding(self, name, embedding, labels=None, images=None, iteration=None):
        [r.add_embedding(name, embedding, labels=labels, images=images, iteration=iteration)
         for r in self.reporters if hasattr(r, 'add_embedding')]

    def log(self, value):
        [r.log(value) for r in self.reporters if hasattr(r, 'log')]
