import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import logging
from SendReportEmail import sendmail

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browserr = testdata['browser']


# Опции только для хрома
# options = webdriver.ChromeOptions()


@pytest.fixture()  # @pytest.fixture(scope='session') Сразу для всех тестов без закрытия сайта
def browser():
    if browserr == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def send_email():
    yield
    sendmail()

@pytest.fixture()
def login():
    try:
        response = requests.post(url="https://test-stand.gb.ru/gateway/login",
                                 data={'username': testdata['login'], 'password': testdata['passwd']})
        response_json = response.json()
        token = response_json.get('token')
    except:
        logging.exception("Get token exception")
        token = None
    logging.debug(f"Return token success")
    return token

