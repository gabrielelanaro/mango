from .reporters import TextReporter

class Model:

    def __init__(self, **parameters):
        reporter = parameters.get('reporter')

        for p, t in self.required_params.items():
            if p not in parameters:
                raise ValueError(f'Error initializing {type(self).__name__}. Required parameter {p} of type {t.__name__}')
            else:
                setattr(self, p, parameters[p])
    
        if reporter is None:
            self.reporter = TextReporter()
        else:
            self.reporter = reporter

    def initialize(self):
        pass

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        cls.required_params = {
            name: value for name, value in cls.__annotations__.items()
        }

    def train(self):
        raise NotImplementedError()

    def predict(self):
        raise NotImplementedError()

    def meta(self):
        return {
            'parameters': self.parameters
        }
