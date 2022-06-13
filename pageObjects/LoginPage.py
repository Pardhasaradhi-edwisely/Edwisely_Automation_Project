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

class assessment:
    element_assessment_classname="row no-gutters"
    label_your_assessment_id="courseName"
    button_create_assessment_xpath="//a[normalize-space()='Create New Assessment']"
    link_objective_xpath="//a[normalize-space()='Objective']"
    link_subjective_xpath="//a[normalize-space()='Subjective']"
    textbox_add_title_id="title-objective"
    textbox_description_box_xpath="(//div[@role='textbox'])[1]"
    dropdown_subject_xpath="(//select[@id='subject'])[1]"
    textbox_section_name_id="section_name1"
    dropdown_marks_per_question_xpath="(//select[@id='section_marks1'])[1]"
    textbox_instruction_xpath="//div[@class='section']//div[@role='textbox']"
    button_add_new_section_id="btnAdd"
    button_delete_above_section_id="btnDeleteSection"
    button_continue_id="createAssessmentBtn"
    label_create_assessment_xpath="//h5[normalize-space()='Create Questions']"
    element_choose_question_id="chooseques"
    dynamic_units_list_xpath="//li[@class='getUnitsLi'][1]//input[@class='getUnitsInput']"  #change no
    dynamic_checkbox_list_xpath="//li[@class='chooseQuestionsLi pl-3 pr-2 py-2'][1]//input[@type='checkbox']" #change no
    element_topic_id="subject-modal-div"
    button_save_to_section_xpath="//button[normalize-space()='Save to Section']"
    dynamic_question_panel_xpath="//div[@class='addingQues p-1']//div[@class='row'][1]"  #change no
    button_save_and_exit_id="btnSaveExit"
    button_save_and_send_id="btnSaveSend"
    textbox_start_time_id="starttime"
    textbox_end_time_id="endtime"
    toggle_auto_release_results_id="releaseSwitch"
    textbox_hours_classname="durationHours pl-1"
    textbox_minutes_classname="durationMinutes pl-1"
    toggle_nba_analysis_xpath="//input[@class='custom-control-input' and @id='nbaSwitch']"
    toggle_collect_feedback_xpath="//input[@class='custom-control-input' and @id='feedbackSwitch']"










