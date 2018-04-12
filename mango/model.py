from .reporters import TextReporter
from .base import Parameterized

class Model(Parameterized):

    def __init__(self, reporter=None, **params):
        super().__init__(**params)
        if reporter is None:
            self.reporter = TextReporter()
        else:
            self.reporter = reporter

    def build(self):
        pass
