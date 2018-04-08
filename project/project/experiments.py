import mango
import mango.reporters as reporters

from .models import StupidModel
from .datasets import StupidDataset

class Base(mango.Experiment):

    dataset = StupidDataset()
    model = StupidModel(reporters.CombinedReporter([
        reporters.TextReporter(),
        reporters.LogReporter('base')
    ]))
    trainer = mango.CrossValidationTrainer(model, dataset)
