def pytest_addoption(parser):
    parser.addoption('--browser', default='Firefox')
    parser.addoption('--env', default='Windows')
    parser.addoption('--url', default='test')