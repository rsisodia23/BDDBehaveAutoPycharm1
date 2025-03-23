from selenium import webdriver
from utilities import ConfigReader

def before_scenario(context, driver):
    browser = ConfigReader.read_configuration("basic info" , "browser")

    if browser == 'chrome':
        context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    context.driver.get(  ConfigReader.read_configuration("basic info" , "url") )

def after_scenario(context, driver):
    context.driver.quit()
