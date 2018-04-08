class CombinedReporter:

    def __init__(self, reporters):
        self.reporters = reporters

    def __getattr__(self, name):
        if not any(hasattr(r, name) for r in self.reporters):
            raise AttributeError(f"None of the reporters has method {name}")
        else:
            def f(*args, **kwargs):
                [getattr(r, name)(*args, **kwargs) for r in self.reporters if hasattr(r, name)]
            return f
