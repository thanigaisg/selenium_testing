import pytest


@pytest.mark.sanity
def test_third_testcase():
    var = "Selenium"
    assert var == "Selenium", "String match"


@pytest.mark.skip
def test_e2e_fourth_testcase():
    var = "Selenium"
    assert var == "Selenium Learner!", "Test failed because of strings do not match"