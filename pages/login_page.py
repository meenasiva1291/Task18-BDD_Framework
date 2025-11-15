
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # ----------- LOCATORS -----------
    USERNAME_INPUT = (By.XPATH,"//input[@placeholder='Enter your mail']")
    PASSWORD_INPUT = (By.XPATH,"//input[@placeholder='Enter your password ']")
    SUBMIT_BUTTON = (By.XPATH,"//button[text()='Sign in']")
    ERROR_MESSAGE = (By.XPATH,"//p[text()='Incorrect password!']")
    POPUP = (By.XPATH,"//button[@class='custom-close-button']")
    PROFILE_ICON = (By.ID, "profile-click-icon")  # The small dropdown icon in your screenshot
    LOGOUT_BUTTON = (By.XPATH, "//div[contains(text(),'Log out')]")

    def __init__(self, driver):
        self.driver = driver

    # ----------- PAGE ACTIONS -----------

    def open_login_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(2)


    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text

    def validate_input_boxes(self):
        username_field = self.driver.find_element(*self.USERNAME_INPUT)
        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        return username_field.is_displayed() and username_field.is_enabled() \
            and password_field.is_displayed() and password_field.is_enabled()

    def click_logout(self):
        self.driver.find_element(*self.POPUP).click()
        # Step 1: Click profile icon to open dropdown
        wait = WebDriverWait(self.driver, 10)
        profile_icon = wait.until(EC.element_to_be_clickable(self.PROFILE_ICON))
        profile_icon.click()

        # Step 2: Click on "Log out" menu item
        logout_button = wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
        logout_button.click()
