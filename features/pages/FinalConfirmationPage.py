from selenium.webdriver.common.by import By


class FinalConfPage():

    def __init__(self, driver):
        self.driver = driver

    finalconfdiaplaymsg_xpath = "// *[ @ id = 'content'] / h1"

    def registrtnconf_finaldisplaymsgassert(self):

        return self.driver.find_element(By.XPATH, self.finalconfdiaplaymsg_xpath).is_displayed()