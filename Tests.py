import pytest

def test_add():
    assert 2+2==4
    print("Addition is scuccessful")

@pytest.mark.parametrize("input, expected", [(1, 2), (2, 3), (3, 4)])
def test_increment(input, expected):
    assert input + 1 == expected



def test_unuse():
    pytest.skip("Skipped")
    print("This method is of no use")