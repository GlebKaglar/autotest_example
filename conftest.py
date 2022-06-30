import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language: ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-hans')


@pytest.fixture(scope='function')
def browser(request):
    language_selected = request.config.getoption('language')  # Получаем параметр language из командной строки
    link = f'http://selenium1py.pythonanywhere.com/{language_selected}/catalogue/coders-at-work_207/'
    print('\nStart Chrome browser for test...')
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    browser.get(link)
    yield browser
    print('\nQuit browser')
    browser.quit()
