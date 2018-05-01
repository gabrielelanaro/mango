import mango
import mango.reporters as reporters

from mango.loaders import SimpleLoader, MiniBatchLoader
from mango.reporters.tensorboard import TensorboardReporter
from mango.trainer import SimpleTrainer, MiniBatchTrainer

from project.models import StupidModel
from project.datasets import StupidDataset


class SimpleTest(mango.Experiment):
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


class MiniBatch(mango.Experiment):
    reporter = reporters.TextReporter()
    dataset = StupidDataset()
    model = StupidModel(
        const=1.0
    )
    loader = MiniBatchLoader(dataset, batch_size=32)
    trainer = MiniBatchTrainer(model, loader)
