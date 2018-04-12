import mango
from mango.reporters.text import TextReporter

def test_meta():

    class Model(mango.Model):

        hello = mango.Param(int)

    class Exp(mango.Experiment):
        reporter = TextReporter()
        model = Model(hello=1)

    assert Exp.parameters() == {'model': {'hello': 1}}

    TextReporter().add_parameters(Exp.parameters())
