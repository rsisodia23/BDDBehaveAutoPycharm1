from selenium.webdriver.common.by import By

from features.pages.BaseParentPage import BaseParentP


class HomeP(BaseParentP):
    def __init__(self , driver):
        #self.driver = driver
        super().__init__(driver)

    homepage_myaccount_xpath = "//span[text()='My Account']"
    homepage_register_linktext = "Register"
    homepage_login_linktext = "Login"

    def click_on_hompage_myaccount(self):
        self.click_on_a_link_bylocator("homepage_myaccount_xpath" , self.homepage_myaccount_xpath)
        #self.driver.find_element(By.XPATH , self.homepage_myaccount_xpath).click()


    def click_on_a_register_link(self):
        self.click_on_a_link_bylocator("homepage_register_linktext", self.homepage_register_linktext)

    def click_on_a_login_link(self):
        self.click_on_a_link_bylocator("homepage_login_linktext", self.homepage_login_linktext)


    #def click_on_register_link(self):

