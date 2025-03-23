from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I am on search page')
def step_impl(context):
    #print("Step for search page")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")

@when(u'I enter valid product on search bar')
def step_impl(context):
    #print("this is step for valid product search")
    context.driver.find_element(By.NAME, "search").send_keys("HP")


@when(u'i click on search button')
def step_impl(context):
    #print("this is step for search button")
    context.driver.find_element(By.XPATH, "//div[@id='search']//button").click()


@then(u'Product details should displayed')
def step_impl(context):
    #print("this is step for product display")
    assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    context.driver.quit()


@when(u'I enter invalid product on search bar')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("HONDAAA")


@then(u'i should get a proper warning message of no valid product')
def step_impl(context):
    assert context.driver.find_element(By.XPATH , "//*[@id='content']/p[2]").is_displayed()
    input("enter something to close the broweser")
    #print(context.driver.find_element(By.XPATH, "//*[@id='content']/p[2]").text)
