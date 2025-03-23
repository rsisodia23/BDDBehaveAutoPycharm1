from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
#import register
from  features.steps import register
from features.steps import shareddata
from features.pages.Homepage import HomeP

@given(u'I am on login page')
def step_impl(context):
    homepageobj = HomeP(context.driver)
    homepageobj.click_on_hompage_myaccount()
    #context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    homepageobj.click_on_a_login_link()
    #context.driver.find_element(By.LINK_TEXT, "Login").click()

@when(u'I enter valid email address and password')
def step_impl(context):
    #email1 =  shareddata.em
    email1 = 'RS202503231215@gmail.com'
    context.driver.find_element(By.ID, "input-email").send_keys(email1)
    context.driver.find_element(By.ID, "input-password").send_keys("123456789")

@when(u'I enter valid email address as "{emailid}" and password as "{password}"')
def step_impl(context, emailid, password):
    context.driver.find_element(By.ID, "input-email").send_keys(emailid)
    context.driver.find_element(By.ID, "input-password").send_keys(password)

@when(u'I enter email address  and password from below datatable')
def step_impl(context):
    for row in context.table:
        context.driver.find_element(By.ID, "input-email").clear()
        context.driver.find_element(By.ID, "input-email").send_keys(row['email'])
        context.driver.find_element(By.ID, "input-password").clear()
        context.driver.find_element(By.ID, "input-password").send_keys(row['password'])
    #raise NotImplementedError(u'STEP: When I enter email address  and password from below datatable')



@when(u'i click on login button')
def step_impl(context):
    #print("Step for login button click")
    context.driver.find_element(By.XPATH, "//input[@value='Login']").click()

@then(u'I should get logged in')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    #if context.driver.find_element(By.LINK_TEXT, "Logout").is_displayed():
     #   context.driver.find_element(By.LINK_TEXT, "Logout").click()
    assert context.driver.find_element(By.LINK_TEXT, 'Logout').is_displayed()


    #assert context.driver.find_element(By.XPATH, "//*[@id='content']/h2[1]").text__eq__("My Account")
    input("enter some")

