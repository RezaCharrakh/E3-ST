import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """Initialize the WebDriver."""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
