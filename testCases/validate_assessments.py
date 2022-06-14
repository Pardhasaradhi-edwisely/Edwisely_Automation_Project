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
    def test_validateAssessmentPage(self,setup):
        self.logger.info("***Test_002_assessment***")
        self.logger.info("***Validate Assessment Page***")
        self.driver = setup
        self.url=XLUtils.readData(self.path,'Sheet1', 2 ,1)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.page_title=self.driver.title
        print(self.page_title)
        self.expected_title=XLUtils.readData(self.path,'Sheet1',2,4)
        if self.page_title==self.expected_title:
            self.logger.info("***Title Matched***")
            assert True
        else:
            self.logger.info("***Title UnMatched***")
            assert False
        self.li = login(self.driver)
        self.username=XLUtils.readData(self.path,'Sheet1',2,2)
        self.li.facultyUsername(self.username)
        self.password=XLUtils.readData(self.path,'Sheet1',2,3)
        self.li.facultyPassword(self.password)
        self.li.submit_02()
        time.sleep(3)
        self.page_title = self.driver.title
        print(self.page_title)
        self.exp_login_page_title=XLUtils.readData(self.path,'Sheet1',2,5)
        if self.page_title == self.exp_login_page_title:
            print("LOGIN SUCCESSFUL ")
            self.logger.info("*****Login Successful****")
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_facultyLogin.png")
            print('lOGIN UNSUCCESSFUL')
            self.logger.error("******Login Unsuccessful")
            assert False
            self.driver.close()
        self.asses=assessment(self.driver)
        self.asses.clickAssessment()
        self.driver.implicitly_wait(10)
        self.assesTitle=self.driver.title
        print(self.assesTitle)
        self.row=XLUtils.getRowCount(self.path,'Sheet1')
        print("row count",self.row)
        self.col=XLUtils.getColumnCount(self.path,'Sheet1')
        print("column count", self.col)
        for r in range(1,self.row+1):
            for c in range(1,self.col+1):
                if self.assesTitle==XLUtils.readData(self.path,'Sheet1',r,c):
                    self.logger.info("**Assessment title page matched**")
                    assert True


    @pytest.mark.sanity
    def test_CreateObjectiveAssessment(self,setup):
        self.logger.info("***Test_002_assessment***")
        self.logger.info("***validate create objective assessment***")
        self.driver = setup
        self.url=XLUtils.readData(self.path,'Sheet1', 2 ,1)
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.page_title=self.driver.title
        self.expected_title=XLUtils.readData(self.path,'Sheet1',2,4)
        if self.page_title==self.expected_title:
            assert True
        else:
            assert False
            self.driver.close()
        self.li = login(self.driver)
        self.username=XLUtils.readData(self.path,'Sheet1',2,2)
        self.li.facultyUsername(self.username)
        self.password=XLUtils.readData(self.path,'Sheet1',2,3)
        self.li.facultyPassword(self.password)
        self.li.submit_02()
        time.sleep(3)
        self.page_title = self.driver.title
        self.exp_login_page_title=XLUtils.readData(self.path,'Sheet1',2,5)
        if self.page_title == self.exp_login_page_title:
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "loginpage.png")
            assert False
            self.driver.close()
        self.asses=assessment(self.driver)
        self.asses.clickAssessment()
        self.driver.implicitly_wait(10)
        self.assesTitle=self.driver.title
        self.exp=XLUtils.readData(self.path,"Sheet1",2,6)
        if self.assesTitle==self.exp:
            assert True
        else:
            assert False
            self.driver.close()
            self.driver.save_screenshot(".//Screenshots//" + "assessmentTitle.png")
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



























