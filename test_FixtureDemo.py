import pytest

from BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class FixtureDemo(BaseClass):
    def test_demo1(self):
        log = self.getlogger()
        log.info()
        print("Demo 1 execute once")

    def test_demo2(self):
        print("Demo 2 execute once")

    def test_demo3(self):
        print("Demo 3 execute once")

    def test_demo4(self):
        print("Demo 4 execute once")