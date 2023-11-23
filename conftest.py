import pytest
from selene import browser


@pytest.fixture()
def window_size():
    browser.config.window_width = 1080
    browser.config.window_height = 1690
    yield
    browser.quit()
