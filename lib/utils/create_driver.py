from argparse import ArgumentParser
from selenium.webdriver import Chrome, Firefox, Ie

def browser_instance():
    parser = ArgumentParser()
    parser.add_argument('--browser', default='chrome')
    parser.add_argument('--url', default='test')
    parser.add_argument('--env', default='Windows')

    options, args = parser.parse_known_args()
    browser_type = options.browser.lower()
    url_info = options.url.lower()
    env_info = options.env.lower()

    if browser_type == 'Firefox':
        driver = Firefox('browser/geckodriver.exe')
    elif browser_type == 'chrome':
        driver = Chrome('browser/chromedriver.exe')
    else:
        print('---- Invalid Option ----')
        return None

    driver.maximize_window()
    driver.implicitly_wait(30)

    if url_info == 'test':
        driver.get('http://demo.guru99.com/v4/')
    else:
        print('---- Invalid URL ----')

    return driver
