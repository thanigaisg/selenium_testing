import pytest


@pytest.mark.usefixtures('dataLoad')
class TestClass2:

    def test_editProfile(self, dataLoad):
        for item in dataLoad:
            print(item)
