from .base import Parameterized
from .reporters import TextReporter


class Experiment:

    def __init__(self):
        if not hasattr(self, 'trainer'):
            raise ValueError("{type(self).__name__}.trainer was not defined")

        if not hasattr(self, 'reporter'):
            self.reporter = TextReporter()

    def run(self):
        self.reporter.add_parameters(self.parameters())
        self.trainer.train()

    @classmethod
    def parameters(cls):
        result = {}

        for k, v in cls.__dict__.items():
            if isinstance(v, Parameterized):
                result[k] = v.meta()
        return result
