"""Pytest Unit Test Config.

How to test these examples:

$ pytest
..                      [100%]
2 passed in 0.01s

$ pytest --fail ok
F                       [100%]
================================ FAILURES ===================================
______________________________ test_example _________________________________

example = False

    def test_example(example):
>       assert example
E       assert False

test/test_example.py:6: AssertionError
========================== short test summary info ==========================
FAILED test/test_example.py::test_arg_example - assert False
1 failed, 1 passed in 0.10s

$ pytest --fail foo
!!!!!!!!!!!!! _pytest.outcomes.Exit: '--fail 'ok' to fail test !!!!!!!!!!!!!!!
1 passed in 0.34s
"""
import pytest


def pytest_addoption(parser):
    """Adding pytest argument."""
    pytest_arg: str = "fail"
    parser.addoption("--" + pytest_arg, action="store")


@pytest.fixture(scope="session")
def arg_example(request):
    """Getting the pytest argument and its' value."""
    fail = request.config.option.fail
    res: bool

    if not fail:  # pass test if no param
        res = True
    elif fail == "ok":  # fail test if 'fail ok'
        res = False
    else:  # abort testing otherwise
        pytest.exit("'--fail 'ok' to fail test")

    return res

@pytest.fixture
def test_cases():
    """Get list of test cases and expected output."""
    test_cases = [(0,True), (1, False)]

    return test_cases