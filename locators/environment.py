from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_all(context):
    print("this is before all call")


def before_feature(context, feature):
    print("this is before feature")


def after_feature(context, feature):
    print("this is after feature")


def before_scenario(context, scenario):
    print("Chrome driver execute")
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()


def after_scenario(context, scenario):
    print("Chrome driver closed")
    context.driver.close()
