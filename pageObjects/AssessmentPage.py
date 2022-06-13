from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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
    textbox_section_name_id2 = "section_name2"
    dropdown_marks_per_question_xpath="(//select[@id='section_marks1'])[1]"
    dropdown_marks_per_question_xpath2="(//select[@id='section_marks2'])[1]"
    textbox_instruction_xpath="//div[@class='section']//div[@role='textbox']"
    textbox_instruction_xpath2="//div[@id='section2']//div[@role='textbox']"
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
    radio_class_select_classname="sectionsListInput"
    checkbox_rmkcs5_xpath="//input[@data-roll_number='RMKCS5']"
    checkbox_rmkcs04_xpath="//input[@data-roll_number='RMKCS04']"
    checkbox_rmkcs6_xpath="//input[@data-roll_number='RMKCS6']"
    button_send_id="sendQuestionsBtn"
    button_scheduled_xpath="//button[normalize-space()='Scheduled']"
    textbox_add_question_xpath = "//div[@class='col-sm-9']//div[@role='textbox']"
    input_add_image_id="quesImage"
    checkbox_topics_list_dynamic="//li[1]//input[@class='topicTagsInput']" #change no
    dropdown_blooms_id="selectBloomLevel"
    dropdown_difficulty_id="selectLevel"
    textbox_optionA_xpath="//div[@class='row pt-4']//div[@class='col-6 pl-0 pr-1']//div[@role='textbox']"
    textbox_optionB_xpath="//div[@class='row no-gutters w-100']//div[@role='textbox']"
    textbox_optionC_xpath="//div[@class='row no-gutters w-100']//div[@role='textbox']"
    textbox_optionD_xpath="//div[@class='col-6 pl-1 pr-0']//div[@class='row no-gutters']//div[@role='textbox']"
    checkbox_option_xpath="//input[@id='Radios1']"
    link_add_source_id="sourceBtn"
    textbox_source_id="sourceInput"
    button_save_section_id= "saveSection"
    button_add_question_id="addques"


    def __init__(self,driver):
        self.driver=driver

    def clickAssessment(self):
        self.driver.find_element(By.CLASS_NAME,self.element_assessment_classname).click()

    def clickCreateNewAssessment(self):
        self.driver.find_element(BY.XPATH,self.button_create_assessment_xpath).click()

    def clickObjectiveAssessment(self):
        self.driver.find_element(BY.LINK_TEXT,self.link_objective_xpath).click()

    def clickSubjectiveAssessment(self):
        self.driver.find_element(BY.LINK_TEXT,self.link_subjective_xpath).click()

    def addTitle(self,title):
        self.driver.find_element(BY.ID,self.textbox_add_title_id).clear()
        self.driver.find_element(BY.ID,self.textbox_add_title_id).send_keys(title)

    def addDescription(self,descrip):
        self.driver.find_element(BY.XPATH,self.textbox_description_box_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_description_box_xpath).send_keys(descrip)

    def selectSubject(self,sub):
        subject=Select(self.driver.find_element(BY.XPATH,self.dropdown_subject_xpath))
        subject.Select_by_visible_text(sub)

    def sectionName(self,sec):
        self.driver.find_element(By.ID,self.textbox_section_name_id).clear()
        self.driver.find_element(By.ID, self.textbox_section_name_id).send_keys(sec)

    def marksPerQuestion(self,marks):
        mar=Select(self.driver.find_element(BY.XPATH,self.dropdown_marks_per_question_xpath))
        mar.select_by_value('2.0')

    def secInstruction(self,instruction):
        self.driver.find_element(BY.XPATH,self.textbox_instruction_xpath).clear()
        self.driver.find_element(BY.XPATH,self.textbox_instruction_xpath).send_keys(instruction)

    def addNewSection(self):
        self.driver.find_element(BY.ID,self.button_add_new_section_id).click()

    def sectionName_02(self,sec):
        self.driver.find_element(By.ID,self.textbox_section_name_id2).clear()
        self.driver.find_element(By.ID, self.textbox_section_name_id2).send_keys(sec)

    def marksPerQuestion_02(self,marks):
        mar=Select(self.driver.find_element(BY.XPATH,self.dropdown_marks_per_question_xpath2))
        mar.select_by_value('2.0')

    def secInstruction_02(self,instruction):
        self.driver.find_element(BY.XPATH,self.textbox_instruction_xpath2).clear()
        self.driver.find_element(BY.XPATH,self.textbox_instruction_xpath2).send_keys(instruction)

    def deleteSection(self):
        self.driver.find_element(BY.ID,self.button_delete_above_section_id).click()

    def clickContinue(self):
        self.driver.find_element(BY.ID,self.button_continue_id).click()

    def clickAddQuestion(self):
        self.driver.find_element(BY.ID,self.button_add_question_id).click()

    def addquestion(self,ques):
        self.driver.find_element(BY.XPATH,self.textbox_add_question_xpath).clear()
        self.driver.find_element(BY.XPATH, self.textbox_add_question_xpath).send_keys(ques)

    def selectTopics(self):
        self.driver.find_element(BY.ID,self.element_topic_id).click()

    def inputOption(self,opta,optb,optc,optd):
        self.driver.find_element(BY.XPATH,self.textbox_optionA_xpath).clear()
        self.driver.find_element(BY.XPATH, self.textbox_optionA_xpath).send_keys(opta)
        self.driver.find_element(BY.XPATH, self.textbox_optionB_xpath).clear()
        self.driver.find_element(BY.XPATH, self.textbox_optionB_xpath).send_keys(optb)
        self.driver.find_element(BY.XPATH, self.textbox_optionC_xpath).clear()
        self.driver.find_element(BY.XPATH, self.textbox_optionC_xpath).send_keys(optc)
        self.driver.find_element(BY.XPATH, self.textbox_optionD_xpath).clear()
        self.driver.find_element(BY.XPATH, self.textbox_optionD_xpath).send_keys(optd)

    def selectOption(self):
        self.driver.find_element(BY.XPATH,self.checkbox_option_xpath).click()

    def selectBloom(self,bloom):
        blm=Select(self.driver.find_element(BY.ID,self.dropdown_blooms_id))
        blm.select_by_visible_text(bloom)

    def selectDifficulty(self,difficulty):
        dif=Select(self.driver.find_element(BY.ID,self.dropdown_difficult_id))
        dif.select_by_visible_text(difficulty)

    def addSource(self,source):
        self.driver.find_element(BY.LINK_TEXT,self.link_add_source_id).click()
        self.driver.find_element(BY.ID,self.textbox_source_id).clear()
        self.driver.find_element(BY.ID,self.textbox_source_id).send_keys(source)

    def clickSaveToSection(self):
        self.driver.find_element(BY.XPATH,self.button_save_to_section_xpath).click()

    def clickSaveAndSend(self):
        self.driver.find_element(BY.ID,self.button_save_and_send_id).click()

    def clickChooseQuestion(self):
        self.driver.find_element(BY.ID,self.element_choose_question_id).click()














