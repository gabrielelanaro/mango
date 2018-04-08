import tensorboardX
import torch
import numpy as np
import os

class TensorboardReporter:

    def __init__(self, logdir='runs'):
        self.logdir = self._create_dirs(logdir)
        self._writer = tensorboardX.SummaryWriter(self.logdir)

    def add_scalar(self, name, scalar, global_step):
        self._writer.add_scalar(name, scalar, global_step)

    def add_embedding(self, name, embedding, labels=None, images=None, iteration=0):
        embedding = np.array(embedding).astype('float')
        self._writer.add_embedding(torch.FloatTensor(embedding),
                                   metadata=labels,
                                   global_step=iteration)

    def add_histogram(self, name, data, iteration, bins='auto'):
        values = np.array(data).astype('float')
        self._writer.add_histogram(name, torch.FloatTensor(values), global_step=iteration, bins=bins)

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
