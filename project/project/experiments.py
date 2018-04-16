import mango
import mango.reporters as reporters

from mango.loaders.minibatch import MiniBatchLoader
from mango.reporters.tensorboard import TensorboardReporter
from mango.trainer import SimpleTrainer
from .models import StupidModel
from .datasets import StupidDataset

class Test(mango.Experiment):

    dataset = StupidDataset()
    model = StupidModel(
        const=1.0,
        reporter=reporters.CombinedReporter([
            reporters.TextReporter(),
            reporters.LogReporter('logs'),
            reporters.tensorboard.TensorboardReporter()
        ])
    )
    loader = MiniBatchLoader(dataset, batch_size=32)
    trainer = SimpleTrainer(model, loader)
