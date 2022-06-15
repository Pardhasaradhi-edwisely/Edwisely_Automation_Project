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
            assert True
        else:
            self.logger.info("Page Title Not Matched")
            self.driver.save_screenshot(".//Screenshots//" + "pageTitle.png")
            assert False
            self.driver.close()
        self.li = login(self.driver)
        self.username=XLUtils.readData(self.path,'Sheet1',2,2)
        self.li.facultyUsername(self.username)
        self.password=XLUtils.readData(self.path,'Sheet1',2,3)
        self.li.facultyPassword(self.password)
        self.li.submit_02()
        time.sleep(3)
        self.dashboard_title = self.driver.title
        self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.dashboard_title)
        if self.status == "True":
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_facultyLogin.png")
            self.logger.error("******Login Unsuccessful***")
            assert False
            self.driver.close()
        self.asses=assessment(self.driver)
        self.asses.clickAssessment()
        self.driver.implicitly_wait(10)
        self.assesTitle=self.driver.title
        print(self.assesTitle)
        self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.assesTitle)
        print(self.status)
        if self.status == "True":
            assert True
        else:
            assert False
            self.driver.close()
            self.screen=random_generator() + "image.png"
            self.driver.save_screenshot(".//Screenshots//" + self.screen)
        time.sleep(2)
        self.asses.clickCreateNewAssessment()
        self.asses.clickObjectiveAssessment()
        time.sleep(2)
        self.gettitle = self.driver.title
        """self.exp=XLUtils.readData(self.path,'Sheet1',2,7)
        if self.gettitle==self.exp:
            self.logger.info("***Successfully navigated to create new assesment page***")"""
        self.row=XLUtils.getRowCount(self.path,'Sheet1')
        print("row count",self.row)
        self.col=XLUtils.getColumnCount(self.path,'Sheet1')
        print("column count", self.col)
        for r in range(1,self.row+1):
            for c in range(1,self.col+1):
                if self.gettitle==XLUtils.readData(self.path,'Sheet1',r,c):
                    self.logger.info("successfully navigated to create new assessment page")
                    assert True

    @pytest.mark.sanity
    def test_validateAssessment(self,setup):
        self.driver = setup
        self.url=XLUtils.readData(self.path,'Sheet1', 2 ,1)
        print("page url",self.url)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.page_title=self.driver.title
        print(self.page_title)
        self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.page_title)
        print(self.status)
        self.log=LogGen.statusValidation(self,self.status,self.page_title,self.driver)
        self.logger.info(self.log)

























