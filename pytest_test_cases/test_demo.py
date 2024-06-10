import pytest

def test_equal():
    a = 4
    b = 5
    assert a+1 == b, "Test Passed"
    assert a == b, "Test Failed, 'a' is not equal to 'b'"

def test_name():
    name = "selenium"
    assert name.capitalize() == "Selenium", "Test Passed, string.capitilize worked"

def test_lamba_map():
    assert list(map(lambda a:pow(a,3), [1,2,3])) == [1,8,27], "Test Passed, lambda and map function worked"


