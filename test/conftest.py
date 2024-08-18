import pytest
from .environment import Environment

test_environment = Environment('test1', 'test')


@pytest.fixture
def environment():
    return test_environment
