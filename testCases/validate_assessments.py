import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import login
from pageObjects.AssessmentPage import assessment
from utilities.readData import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_assessment:
    logger = LogGen.loggen()
    path = ".\\TestData\\testdata.xlsx"

    @pytest.mark.regression
    def test_validateAssessmentTitle(self,setup):
        self.logger.info("**** Test_002_assessment ****")
        self.logger.info("**** TC_01 Validate Assessment Page ****")
        self.driver = setup
        self.url=XLUtils.readData(self.path,'Sheet1', 2 ,1)
        print("page url",self.url)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.page_title=self.driver.title
        print(self.page_title)
        self.status = XLUtils.dataValidation(self.path,'Sheet1', self.page_title)
        print(self.status)
        self.log = LogGen.statusValidation(self,self.status, self.page_title, self.driver)
        self.logger.info(self.log)
        self.li = login(self.driver)
        self.username=XLUtils.readData(self.path,'Sheet1',2,2)
        print("username:",self.username)
        self.li.facultyUsername(self.username)
        self.password=XLUtils.readData(self.path,'Sheet1',2,3)
        print("Password: *******")
        self.li.facultyPassword(self.password)
        self.li.submit_02()
        time.sleep(3)
        self.dashboard_title = self.driver.title
        print(self.dashboard_title)
        self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.dashboard_title)
        print(self.status)
        self.log = LogGen.statusValidation(self, self.status, self.dashboard_title, self.driver)
        self.logger.info(self.log)
        self.asses=assessment(self.driver)
        self.asses.clickAssessment()
        self.driver.implicitly_wait(10)
        self.assesTitle=self.driver.title
        print(self.assesTitle)
        self.status=XLUtils.dataValidation(self.path,'Sheet1',self.assesTitle)
        print(self.status)
        self.log = LogGen.statusValidation(self, self.status, self.assesTitle, self.driver)
        self.logger.info(self.log)

    @pytest.mark.sanity
    def test_CreateObjectiveAssessment(self,setup):
        self.logger.info("**** Test_002_Assessment ****")
        self.logger.info("**** TC_02 Validate Create Objective Assessment ****")
        self.driver = setup
        self.url=XLUtils.readData(self.path,'Sheet1', 2 ,1)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.page_title=self.driver.title
        self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.page_title)
        if self.status == "True":
            self.li = login(self.driver)
            self.username = XLUtils.readData(self.path, 'Sheet1', 2, 2)
            self.li.facultyUsername(self.username)
            self.password = XLUtils.readData(self.path, 'Sheet1', 2, 3)
            self.li.facultyPassword(self.password)
            self.li.submit_02()
            time.sleep(3)
            self.dashboard_title = self.driver.title
            self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.dashboard_title)
            if self.status == "True":
                self.asses = assessment(self.driver)
                self.asses.clickAssessment()
                self.driver.implicitly_wait(10)
                self.assesTitle = self.driver.title
                print(self.assesTitle)
                self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.assesTitle)
                print(self.status)
                self.log = LogGen.statusValidation(self, self.status, self.assesTitle, self.driver)
                self.logger.info(self.log)
                time.sleep(2)
                self.asses.clickCreateNewAssessment()
                self.asses.clickObjectiveAssessment()
                time.sleep(2)
                self.gettitle = self.driver.title
                print(self.gettitle)
                self.status=XLUtils.dataValidation(self.path,'Sheet1',self.gettitle)
                print(self.status)
                self.log=LogGen.statusValidation(self,self.status,self.gettitle,self.driver)
                self.logger.info(self.log)
                




























