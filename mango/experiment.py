from .base import Parameterized

class Experiment:

    @classmethod
    def parameters(cls):
        result = {}

        for k, v in cls.__dict__.items():
            if isinstance(v, Parameterized):
                result[k] = {p_key: p_val.__get__(v, type(v)) for p_key, p_val in
                             v.params.items() }
        return result
