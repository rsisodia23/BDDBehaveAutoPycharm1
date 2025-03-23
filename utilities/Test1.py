from datetime import  datetime
from behave import *

print("hello1")
#print(context.email)
email = "RS" + datetime.now().strftime("%Y%m%d%H%M") + "@gmail.com"
#print(email)

locator_type = "1_XPATH"
if locator_type == "LINK_TEXT":
    print ("ll")
            #linkurl = self.driver.find_element(By.LINK_TEXT, locator_value)
elif locator_type.lower().endswith("_id"):
    print("id")

            #linkurl = self.driver.find_element(By.ID, locator_value)
elif locator_type.lower().endswith("_xpath"):
    print('xp')
            #linkurl = self.driver.find_element(By.XPATH, locator_value)