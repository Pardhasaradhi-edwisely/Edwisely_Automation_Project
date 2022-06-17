from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("E:\\Edwisely_Automation\\chromedriver_win32\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.headless=False
options.add_experimental_option('excludeSwitches', ['enable-logging'])
import pytest
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(service=serv_obj,options = options)
    return driver

"""
def pytest_configure(config):
    config.metadata['project Name'] = 'Edwisely_Automation_Project'
    config.metadata['Module Name'] = 'login'
    config.metadata['QA'] = 'Pardha'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME",None)
    metadata.pop("Plugins",None)
"""
class TestSystem:
    def __init__(self):
        self.build_configuration = dict()


def pytest_configure(config):
    if hasattr(config, 'slaveinput'):  # slave
        return
    # we are on master node
    # create test system object, attach to config
    s = TestSystem()
    s.build_configuration['foo'] = 'bar'
    config.test_system = s


def pytest_configure_node(node):
    # this is the pendant of pytest_configure hook, but for worker nodes only
    # store serializable stuff from test system object in slaveinput
    node.slaveinput['test_system_serialized'] = node.config.test_system.build_configuration


def pytest_generate_tests(metafunc):
    if hasattr(metafunc.config, 'slaveinput'):  # we are in worker node
        # restore test system object using serialized data
        s = TestSystem()
        s.build_configuration = metafunc.config.slaveinput['test_system_serialized']
    else:  # master
        # simply get test system instance from config
        s = metafunc.config.test_system

    # generate tests
    if 'test_system' in metafunc.fixturenames:
        metafunc.parametrize('test_system', [s])

