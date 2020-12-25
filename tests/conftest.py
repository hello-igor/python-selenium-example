import pytest
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(executable_path='C:\Igor\projects\moodle-e2e-automation\.venv\Scripts\chromedriver.exe')
    request.cls.driver = driver
    driver.get('https://sandbox.moodledemo.net/login/index.php')
    driver.implicitly_wait(10)
    yield
    driver.quit()