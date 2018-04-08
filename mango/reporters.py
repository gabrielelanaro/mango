import os
import time

class TextReporter:

    def add_scalar(self, name, value, iteration):
        print(f"{name}: {value} [it={iteration}]")


class LogReporter:

    def __init__(self, name, basedir='logs'):
        self.basedir = 'logs'
        self.logdir = self._create_dirs(os.path.join(self.basedir, name))


    def _create_dirs(self, logdir):
        if not os.path.exists(logdir):
            version = 0
        else:
            subdirs = os.path.listdir(logdir)
            version = max(int(d) for d in subdirs if d.isdigit()) + 1

        out = os.path.join(logdir, f'{version:4d}')
        os.mkdirs(out)
        return out

    def _write(self, name, data):
        with open(os.path.join(self.logdir, f'{name}.csv'), 'a') as fd:
            fd.write(data)

    def add_scalar(self, name, value, iteration):
        name = name.replace('/', '.')
        self._write(name, f'{iteration}\t{value}\n')


class CombinedReporter:

    def __init__(self, reporters):
        self.reporters = reporters

    def add_scalar(self, name, value, iteration):
        [r.add_scalar(name, value, iteration) for r in self.reporters]
