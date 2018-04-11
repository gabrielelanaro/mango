import pytest
import mango
from mango.base import Param, ValidationError

def test_validation():

    class Model(mango.Model):
        batch_size = Param(int, default=32)

    m = Model()
    with pytest.raises(ValidationError):
        m.batch_size = 0.1


def test_creation():

    class Model(mango.Model):
        batch_size = Param(int)

    with pytest.raises(ValueError):
        m = Model()

    with pytest.raises(ValueError):
        m = Model(batch_size=32, hello=3)
