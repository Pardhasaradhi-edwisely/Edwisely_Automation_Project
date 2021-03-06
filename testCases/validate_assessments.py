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
        self.log = LogGen.statusValidation(self, self.status, self.page_title, self.driver)
        self.logger.info(self.log)
        self.li = login(self.driver)
        self.username = XLUtils.readData(self.path, 'Sheet1', 2, 2)
        self.li.facultyUsername(self.username)
        self.password = XLUtils.readData(self.path, 'Sheet1', 2, 3)
        self.li.facultyPassword(self.password)
        self.li.submit_02()
        time.sleep(2)
        self.dashboard_title = self.driver.title
        self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.dashboard_title)
        self.log = LogGen.statusValidation(self, self.status, self.dashboard_title, self.driver)
        self.logger.info(self.log)
        self.ap = assessment(self.driver)
        self.ap.clickAssessment()
        self.driver.implicitly_wait(10)
        self.assesTitle = self.driver.title
        print(self.assesTitle)
        self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.assesTitle)
        print(self.status)
        self.log = LogGen.statusValidation(self, self.status, self.assesTitle, self.driver)
        self.logger.info(self.log)
        time.sleep(1)
        self.ap.clickCreateNewAssessment()
        self.ap.clickObjectiveAssessment()
        time.sleep(1)
        self.gettitle = self.driver.title
        print(self.gettitle)
        self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.gettitle)
        print(self.status)
        self.log = LogGen.statusValidation(self, self.status, self.gettitle, self.driver)
        self.logger.info(self.log)
        self.quesTitle = "AutoTitle " + ReadConfig.random_generator()
        print("Test Name", self.quesTitle)
        self.logger.info(self.quesTitle)
        self.ap.addTitle(self.quesTitle)
        self.ap.addDescription("Automation_test")
        self.sub = XLUtils.readData(self.path, 'Sheet1', 2, 8)
        self.ap.selectSubject(self.sub)
        print(self.sub)
        self.logger.info(self.sub)
        self.ap.sectionName("A")
        self.logger.info("Section-A")
        self.ap.marksPerQuestion()
        self.logger.info("Marks per question:2 Marks")
        self.ap.secInstruction("Autoamation_test")
        self.ap.addNewSection()
        self.logger.info("New section added")
        self.ap.sectionName02("B")
        self.logger.info("Section B")
        self.ap.marksPerQuestion02()
        self.logger.info("Marks per question: 4 Marks ")
        self.ap.secInstruction_02("Automation_test_02")
        self.ap.deleteSection()
        self.logger.info("Deleted above section")
        self.ap.clickContinue()
        time.sleep(2)
        self.tis = self.driver.title
        print(self.tis)
        self.status = XLUtils.dataValidation(self.path, 'Sheet1', self.tis)
        print(self.status)
        self.log = LogGen.statusValidation(self, self.status, self.tis, self.driver)
        self.logger.info(self.log)
        self.ap.clickAddQuestion()
        self.driver.implicitly_wait(10)
        self.ap.addquestion("Question_01")
        self.logger.info("Question added")
        self.ap.inputOption("opta", "optb", "optc", "optd")
        self.ap.selectOption()
        self.logger.info("Options Added and Selected")
        self.ap.addSource("test_Automation")
        self.ap.selectTopics()
        self.ap.chooseTopics()
        time.sleep(1)
        self.ap.choosetopicClose()
        self.logger.info("Topics Added")
        self.ap.selectBloom()
        self.logger.info("Blooms Added")
        self.ap.selectDifficulty()
        self.driver.implicitly_wait(10)
        self.ap.clickSaveToSection()
        self.ap.clickSaveAndSend()
        self.logger.info("Questions Creation Page is Verified")
        time.sleep(1)
        self.startTime = ReadConfig.getCustomStartDateAndTime()
        self.ap.startTime(self.startTime)
        self.endTime = ReadConfig.getCustomStartDateAndTime()
        self.ap.endTime(self.endTime)
        self.ap.setDuration()
        self.logger.info("Duration time is 2 mins")
        self.ap.classSelect()
        self.logger.info("selected section: 2 Section A")
        self.ap.selectStudents()
        self.logger.info("selected students are rmkcs5, rmkcs04, rmkcs04")
        self.ap.sendTest()


















































