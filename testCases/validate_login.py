import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import login
from utilities.readData import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
class Test_001_login:

    """
    depricated by data driven
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    url = ReadConfig.getApplicationUrl()
    """
    logger = LogGen.loggen()
    path = ".\\TestData\\testdata.xlsx"

    @pytest.mark.regression
    def test_validateTitlePage(self,setup):
        self.logger.info("******Test_001_login******")
        self.logger.info("********validate title of the page testcases******")
        self.driver = setup
        #data driven
        self.url = XLUtils.readData(self.path, 'Sheet1', 2, 1)
        self.driver.get(self.url)
        self.page_title = self.driver.title
        self.expected_title=XLUtils.readData(self.path,'Sheet1',2,4)
        if self.page_title == self.expected_title:
            print("TITLE MATCHED")
            self.logger.info("********Page Title matched")
        else:
            self.driver.save_screenshot(".//Screenshots//"+"test_validateTitlePage.png")
            print("TITLE NOT MATCHED")
            self.logger.error("*******page title not matched******")
        self.driver.close()

    @pytest.mark.regression
    def test_facultyLogin(self,setup):
        self.logger.info("*****faculty login test case*******")
        self.driver = setup
        self.li=login(self.driver)
        #data driven
        self.url=XLUtils.readData(self.path,'Sheet1',2,1)
        self.driver.get(self.url)
        self.username=XLUtils.readData(self.path,'Sheet1',2,2)
        self.li.facultyUsername(self.username)
        self.password=XLUtils.readData(self.path,'Sheet1',2,3)
        self.li.facultyPassword(self.password)
        self.li.submit_02()
        time.sleep(3)
        self.page_title = self.driver.title
        print(self.page_title)
        if self.page_title == "RMK Nextgen | Dashboard":
            print("LOGIN SUCCESSFUL ")
            self.logger.info("*****Login Successful****")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_facultyLogin.png")
            print('lOGIN UNSUCCESSFUL')
            self.logger.error("******Login Unsuccessful")
        self.driver.close()