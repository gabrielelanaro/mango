import mango

class MockTrainer(mango.Trainer):
    
    param_int = mango.Param(int, default=1)
    param_float = mango.Param(float, default=1.0)
    param_string = mango.Param(str, default='hello')

    def train(self):
        pass

class Exp(mango.Experiment):

    trainer = MockTrainer()    


def test_parameters():
    
    exp = Exp()
    exp.set_parameters({'trainer.param_int': '12'})

    assert exp.trainer.param_int == 12