import pytest
from pytest_test_cases.BaseClass import BaseClass


@pytest.mark.usefixtures('setup')
class TestClass1(BaseClass):

    def test_fixture1(self):
        log = self.getLogger()
        print("I will be executing during fixtures 1")
        log.info("I will be executing during fixtures 1")

    def test_fixture2(self):
        log = self.getLogger()
        print("I will be executing during fixtures 2")
        log.info("I will be executing during fixtures 2")

    def test_fixture3(self):
        log = self.getLogger()
        print("I will be executing during fixtures 3")
        log.info("I will be executing during fixtures 3")