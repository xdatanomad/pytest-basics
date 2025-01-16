import pytest
from gitallica.core import Gitallica

@pytest.mark.basic
@pytest.mark.red
def test_add():
    g = Gitallica()
    assert g.add(1, 2) == 3
    assert g.add(-1, 1) == 0
    assert g.add(-1, -1) == -2

@pytest.mark.advanced
@pytest.mark.red
def test_subtract():
    g = Gitallica()
    assert g.subtract(1, 2) == -1
    assert g.subtract(-1, 1) == -2
    assert g.subtract(-1, -1) == 0
