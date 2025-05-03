import pytest


@pytest.fixture
def test_value() -> int :
    return 1


def test_compute_value(test_value):
    print(test_value)