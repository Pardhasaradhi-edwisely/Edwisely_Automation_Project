import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import login
from utilities.readData import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_yourcourses:
    logger = LogGen.loggen()
    path = ".\\TestData\\testdata.xlsx"

    def test_validateYourCourses(self,setup):
        self.url=XLUtils.readData(self.path,'Sheet1',2,1)
        self.driver.get(self.url)
        self.username=XLUtils.readData(self.path,'Sheet1',2,2)
        self.li.facultyUsername(self.username)
        self.password=XLUtils.readData(self.path,'Sheet1',2,3)
        self.li.facultyPassword(self.password)
        self.li.submit_02()
        time.sleep(2)
        self.page_title = self.driver.title
        print(self.page_title)
        if self.page_title == "RMK Nextgen | Dashboard":
            print("LOGIN SUCCESSFUL ")
            self.logger.info("*****Login Successful****")
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_facultyLogin.png")
            print('lOGIN UNSUCCESSFUL')
            self.logger.error("******Login Unsuccessful")

