import time

from behave import *

from helper.selenium_helper import SeleniumHelper
from locators import locators

LOGIN_URL = "https://wwww.facebook.com/login/"


@when('input wrong credentials')
def step_impl(context):
    SeleniumHelper(context.driver).open_page(LOGIN_URL)
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_login, "laz@gmail.com")
    SeleniumHelper(context.driver).insert_text_in_input_field(locators.input_field_password, "fisher")
    SeleniumHelper(context.driver).click(locators.button_login)


@then('error message will come')
def step_impl(context):
    SeleniumHelper(context.driver).wait_till_element_is_present(locators.link_login_error_message)
    time.sleep(5)
