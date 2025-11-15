import time

from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from dotenv import load_dotenv
import os

load_dotenv()  # Load credentials from .env file


@given("I open zenportal login page")
def step_open_login_page(context):
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.open_login_page("https://www.zenclass.in/login")


@when("I login using valid credentials")
def step_login_valid(context):
    username = os.getenv("VALID_USERNAME")
    password = os.getenv("VALID_PASSWORD")
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)


@when("I login using valid username and invalid password")
def step_login_invalid(context):
    username = os.getenv("VALID_USERNAME")
    password = os.getenv("INVALID_PASSWORD")
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)


@when("I click on submit button")
def step_click_submit(context):
    context.login_page.click_submit()


@then("I should be directed to dashboard page")
def step_dashboard_page(context):
    assert "dashboard" in context.driver.current_url.lower(), "Dashboard not reached"


@then("I should receive an error message")
def step_error_message(context):
    error_text = context.login_page.get_error_message()
    assert "invalid" in error_text.lower() or "incorrect" in error_text.lower(), "Error not shown"


@then("username and password input boxes should be visible and enabled")
def step_validate_input_boxes(context):
    assert context.login_page.validate_input_boxes(), "Username/password boxes not visible or enabled"


@when("I click on logout button")
def step_click_logout(context):
    context.login_page.click_logout()


@then("I should be redirected to login page")
def step_redirect_login(context):
    time.sleep(4)
    assert "login" in context.driver.current_url.lower(), "Not redirected to login page"
    # context.driver.quit()
