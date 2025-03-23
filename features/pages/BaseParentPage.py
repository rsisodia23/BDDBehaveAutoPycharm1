from selenium.webdriver.common.by import By


class BaseParentP():
    def __init__(self, driver):
        self.driver  = driver

    def get_element(self , locator_type,  locator_value):
        element = None
        if locator_type.lower().endswith("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.lower().endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.lower().endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        else:
            print("wronglocatortype")
        return element

    def click_on_a_link_bylocator(self, locator_type,  locator_value):
        linkurl = self.get_element(locator_type,  locator_value)
        linkurl.click()

