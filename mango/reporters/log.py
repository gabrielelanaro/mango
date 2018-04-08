import os


class LogReporter:

    def __init__(self, name):
        self.logdir = self._create_dirs(name)

    def _create_dirs(self, logdir):
        if not os.path.exists(logdir):
            version = 0
        else:
            subdirs =[s for s in os.listdir(logdir) if s.isdigit()]
            if len(subdirs) == 0:
                version = 0
            else:
                version = max(int(d) for d in subdirs) + 1

        out = os.path.join(logdir, f'{version:04d}')
        os.makedirs(out)
        return out

    def _write(self, fname, data):
        with open(fname, 'a+') as fd:
            fd.write(data)

    def log(self, value):
        fname = os.path.join(self.logdir, 'out.log')
        self._write(fname, '{}\n'.format(value))

    def add_scalar(self, name, value, iteration):
        name = name.replace('/', '.')
        scalar_fname = os.path.join(self.logdir, f'{name}.csv')
        self._write(scalar_fname, f'{iteration}\t{value}\n')
