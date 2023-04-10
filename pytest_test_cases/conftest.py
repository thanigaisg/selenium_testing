import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ("Thanigaivel", "S G", "test@selenium.com")


@pytest.fixture(params=["chrome", "firefox", "IE"])
def crossBrowser(request):
    return request.param