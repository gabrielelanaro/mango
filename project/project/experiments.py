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
    train_loader = IndexedLoader(dataset)
    test_loader = IndexedLoader(dataset)
    trainer = mango.ScikitTrainer(model, train_loader, test_loader)
