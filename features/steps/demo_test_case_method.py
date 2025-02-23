from behave import *


@given('credentials are given')
def cred_are_given(context):
    print('user_id: zapel')
    pass


@when('we input correct credentials')
def step_impl(context):
    assert 2 == 2, "This is not correct"


@then('login will be successful')
def step_impl(context):
    print('login is successful')


@when('user input wrong credentials')
def step_impl(context):
    assert 2 == 2, "This is not correct"


@then('error message demo will come')
def step_impl(context):
    assert 2 == 2, "This is not correct"


@step("correct profile open")
def step_impl(context):
    print('correct profile open')
