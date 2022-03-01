import pytest

@pytest.mark.sanity
@pytest.mark.skip
def test_firstprogram():
    print("Hello Ayush , Welcome in Pytest")

def test_FirstName():
    print("Ayush")

@pytest.mark.sanity
def test_SecondName():
    print("Srivastava")


