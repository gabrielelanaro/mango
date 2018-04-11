
class Param:

    def __init__(self, type, default=None):
        self.default = default
        self.type = type

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise ValidationError(f'Parameter {self.name} should be of type {self.type.__name__}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

    def required(self):
        return self.default is None


class Parameterized:

    def __init__(self, **params):
        for name, param in self.params.items():
            if param.required() and not name in params:
                raise ValueError(f'Parameter "{name}" is required.')
            if name in params:
                param.__set__(self, params.pop(name))

        # We need to check for extra parameters
        for name in params:
            if name not in self.params:
                raise ValueError(f'No parameter named "{name}"')

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.params = {}

        for k, v in cls.__dict__.items():
            if isinstance(v, Param):
                cls.params[k] = v


class ValidationError(Exception):
    pass
