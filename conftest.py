'''
Conftest files is used when we have to used same type of fixture in different pytest files.

'''

import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will executed before the test case starts")
    yield
    print("I will ve executing at last.")