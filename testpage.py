from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])


class TestSearchLocatorsPosts:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])


class TestSearchLocatorsContact:
    ids = dict()
    with open('locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])


class OperationsHelpers(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator} ")
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get tex from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    # ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description="login form")

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description="password form")

    def title_post(self, word):
        self.enter_text_into_field(TestSearchLocatorsPosts.ids['LOCATOR_TITLE_FIELD'], word, description="title form")

    def description_post(self, word):
        self.enter_text_into_field(TestSearchLocatorsPosts.ids['LOCATOR_DESCRIPTION_FIELD'], word,
                                   description="description form")

    def content_post(self, word):
        self.enter_text_into_field(TestSearchLocatorsPosts.ids['LOCATOR_TEXT_FIELD'], word, description="content form")

    def contact_name(self, word):
        logging.info("input contact name")
        name_contact = self.find_element(TestSearchLocatorsContact.ids['LOCATOR_NAME_FIELD'])
        name_contact.clear()
        return name_contact.send_keys(word)

    def contact_email(self, word):
        logging.info("input contact email")
        email_contact = self.find_element(TestSearchLocatorsContact.ids['LOCATOR_EMAIL_FIELD'])
        email_contact.clear()
        return email_contact.send_keys(word)

    def contact_content(self, word):
        logging.info("input contact content")
        content_contact = self.find_element(TestSearchLocatorsContact.ids['LOCATOR_CONTENT_FIELD'])
        content_contact.clear()
        return content_contact.send_keys(word)

    # CLICK

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description="login")

    def click_new_post_btn(self):
        self.click_button(TestSearchLocatorsPosts.ids['LOCATOR_NEW_POST'], description="click new post")

    def click_save_post_btn(self):
        self.click_button(TestSearchLocatorsPosts.ids['LOCATOR_SAVE_BTN'], description="save post")

    def click_contact_btn(self):
        self.click_button(TestSearchLocatorsContact.ids['LOCATOR_CONTACT_BTN'], description="contact button")

    def click_contact_us_btn(self):
        self.click_button(TestSearchLocatorsContact.ids['LOCATOR_CONTACT_US_BTN'], description="contact us button")

    # GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'])

    def get_user(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_USER_FIELD'])

    def success_save_post(self):
        return self.get_text_from_element(TestSearchLocatorsPosts.ids['LOCATOR_POST'])