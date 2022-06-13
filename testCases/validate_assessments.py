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


