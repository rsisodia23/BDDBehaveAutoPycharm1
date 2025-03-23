from selenium.webdriver.common.by import By

from features.pages.FinalConfirmationPage import FinalConfPage


class RegisterP():
    def __init__(self , driver):
        self.driver = driver

    firstname_ID = "input-firstname"
    lastname_ID = "input-lastname"
    email_ID = "input-email"
    telephone_ID= "input-telephone"
    password_ID = "input-password"
    password_confirm_ID = "input-confirm"
    policy_confirm_XPATH = "//input[@name='agree']"

    regispage_continue_xpath = "//input[@value='Continue']"

    def enter_firstname_registerpg(self, firstname):
        self.driver.find_element(By.ID, self.firstname_ID).send_keys(firstname)

    def enter_lastname_registerpg(self, lastname):
        self.driver.find_element(By.ID, self.lastname_ID).send_keys(lastname)

    def enter_email_registerpg(self, email):
        self.driver.find_element(By.ID, self.email_ID).send_keys(email)


    def enter_telephone_registerpg(self, telephone):
        self.driver.find_element(By.ID, self.telephone_ID).send_keys(telephone)

    def enter_password_registerpg(self, password):
        self.driver.find_element(By.ID, self.password_ID).send_keys(password)

    def enter_password_confirm_registerpg(self, password_confirm):
        self.driver.find_element(By.ID, self.password_confirm_ID).send_keys(password_confirm)

    def check_policy_confirm_registerpg(self):
        self.driver.find_element(By.XPATH, self.policy_confirm_XPATH).click()

    def click_continue_button_registerpg(self):
       self.driver.find_element(By.XPATH, self.regispage_continue_xpath).click()
       return FinalConfPage(self.driver)