from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class login:
    textbox_rollno_classname="login_username__3thA9"
    button_continue_classname="login_loginButton__3pGmb"
    textbox_Studentpassword_classname="login_username__3thA9 form-control px-2 col-11"
    #checkbox_validation_xpath="//div[@class="recaptcha-checkbox-border"]"  recaptcha cannot be handled in selenium
    button_logout_xpath="//div[contains(text(),'Logout')]"
    button_submit_xpath="//button[normalize-space()='Submit']"
    textbox_facultyusername_id="inputEmail"
    textbox_facultypassword_id="inputPassword"
    button_submit_2_id="submit"

    def __init__(self,driver):
        self.driver=driver

    def studentRollno(self,rollno):
        self.driver.find_element(By.CLASS_NAME,self.textbox_rollno_classname).clear()
        self.driver.find_element(By.CLASS_NAME,self.textbox_rollno_classname).send_keys(rollno)

    def clickContinue(self):
        self.driver.find_element(By.CLASS_NAME,self.button_continue_classname).click()

    def password(self,stu_password):
        self.driver.find_element(By.CLASS_NAME,self.textbox_Studentpassword_classname).clear()
        self.driver.find_element(By.CLASS_NAME, self.textbox_Studentpassword_classname).send_keys(stu_password)

    def clickSubmit(self):
        self.driver.find_element(By.XPATH,self.button_submit_xpath).click()

    def facultyUsername(self,username):
        self.driver.find_element(By.ID,self.textbox_facultyusername_id).clear()
        self.driver.find_element(By.ID, self.textbox_facultyusername_id).send_keys(username)

    def facultyPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_facultypassword_id).clear()
        self.driver.find_element(By.ID, self.textbox_facultypassword_id).send_keys(password)

    def submit_02(self):
        self.driver.find_element(By.ID,self.button_submit_2_id).click()

class courses:








