import mango
import mango.reporters as reporters

from mango.loaders import SimpleLoader
from mango.reporters.tensorboard import TensorboardReporter
from mango.trainer import SimpleTrainer
from .models import StupidModel
from .datasets import StupidDataset

class Test(mango.Experiment):
    reporter = reporters.CombinedReporter([
        reporters.TextReporter(),
        reporters.LogReporter('logs'),
        reporters.tensorboard.TensorboardReporter()
    ])
    dataset = StupidDataset()
    model = StupidModel(
        const=1.0,
        reporter=reporter
    )
    loader = SimpleLoader(dataset)
    trainer = SimpleTrainer(model, loader)
