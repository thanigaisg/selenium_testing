import pytest

@pytest.mark.xfail
def test_e2e_first_testcase():
    print("Hi!")
    var = "Hi"
    assert var == "Hi", "Specified string matches"


@pytest.mark.sanity
def test_second_testcase(setup):
    print("Good Morning!!")
    assert True, "Test Passed"


def test_fixtureParams(crossBrowser):
    print(crossBrowser)