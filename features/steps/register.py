from os import waitpid

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from features.pages import Homepage
from features.pages.Homepage import HomeP
from features.pages.RegisterPage import RegisterP
from features.pages.FinalConfirmationPage import  FinalConfPage
from utilities.emailidgenerator import emailid
from utilities import  emailidgenerator
from features.steps import  shareddata

#print(emailidgenerator.new_email())
class register_email():
    def __init__(self):
        self.emailid = emailid

    emailid = emailidgenerator.new_email()
    emailid1 = emailid

@given(u'I am on Register page')
def step_impl(context):
    homepage = HomeP(context.driver)

    homepage.click_on_hompage_myaccount()
            #context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    homepage.click_on_a_register_link()
             #context.driver.find_element(By.LINK_TEXT, "Register").click()



@when(u'I enter all mandatory details')
def step_impl(context):
    registerpageObj = RegisterP(context.driver)
    registerpageObj.enter_firstname_registerpg("RS")
    #context.driver.find_element(By.ID, "input-firstname").send_keys("RS")
    registerpageObj.enter_lastname_registerpg("LS")
        #context.driver.find_element(By.ID, "input-lastname").send_keys("LS")

    em = register_email.emailid
        #context.email = "RS" + datetime.now().strftime("%Y%m%d%H%M") + "@gmail.com"
    shareddata.em = em
    registerpageObj.enter_email_registerpg(em)

        #context.driver.find_element(By.ID, "input-email").send_keys(context.email)
    registerpageObj.enter_telephone_registerpg("123456")
    #context.driver.find_element(By.ID, "input-telephone").send_keys("123456")
    registerpageObj.enter_password_registerpg("123456789")
    registerpageObj.enter_password_confirm_registerpg("123456789")
        #context.driver.find_element(By.ID, "input-password").send_keys("123456789")
        #context.driver.find_element(By.ID, "input-confirm").send_keys("123456789")
    registerpageObj.check_policy_confirm_registerpg()
    #context.driver.find_element(By.XPATH, "//input[@name='agree']").click()
    print(em)

    #input("entercome")




@when(u'i click on continue button')
def step_impl(context):
    registerpageObj = RegisterP(context.driver)
    context.finalpageobj = registerpageObj.click_continue_button_registerpg()
 #   context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()



@then(u'I should get registerd successfully')
def step_impl(context):
    #finalconfObj = FinalConfPage(context.driver)
    assert context.finalpageobj.registrtnconf_finaldisplaymsgassert()
    #assert context.driver.find_element(By.XPATH, "// *[ @ id = 'content'] / h1").is_displayed()
    input("entercome")
