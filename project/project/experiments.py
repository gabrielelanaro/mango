import mango
import mango.reporters as reporters
from mango.reporters.tensorboard import TensorboardReporter

from .models import StupidModel
from .datasets import StupidDataset

class Test(mango.Experiment):

    dataset = StupidDataset()
    model = StupidModel(
        const=0.0,
        reporter=reporters.CombinedReporter([
            reporters.TextReporter(),
            reporters.LogReporter('logs'),
            reporters.tensorboard.TensorboardReporter()
        ])
    )
    loader = MiniBatchLoader(dataset)
    trainer = mango.SimpleTrainer(model, loader)
