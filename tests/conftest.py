import pytest
from selenium import webdriver

from data.tests_data import Routes


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="browser name"
    )


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = webdriver.Firefox() if browser.lower() == "firefox" else webdriver.Chrome()
    driver.get(Routes.main_page)
    yield driver
    driver.quit()
