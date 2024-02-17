import time
from testpage import OperationsHelpers
import logging
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"
    testpage.driver.close()


def test_step2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("claudius.maximus")
    testpage.enter_pass("977547308c")
    testpage.click_login_button()
    assert testpage.get_user() == "Home"


def test_step3(browser):
    logging.info("Test3 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("claudius.maximus")
    testpage.enter_pass("977547308c")
    testpage.click_login_button()
    testpage.click_new_post_btn()
    testpage.title_post("The Mysterious World of Underwater Caves")
    testpage.description_post("Exploring fascinating underground places")
    testpage.content_post("Today we embarked on an exciting journey into the depths of underwater caves, where an incredible world of mysterious inhabitants and stunning landscapes unfolds. Underwater, there are many mysteries and treasures waiting to be uncovered and explored.")
    time.sleep(testdata['sleep_time'])
    testpage.click_save_post_btn()
    assert testpage.success_save_post() == "Today we embarked on an exciting journey into the depths of underwater caves, where an incredible world of mysterious inhabitants and stunning landscapes unfolds. Underwater, there are many mysteries and treasures waiting to be uncovered and explored."


def test_step4(browser):
    logging.info("Test3 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("claudius.maximus")
    testpage.enter_pass("977547308c")
    testpage.click_login_button()
    testpage.click_contact_btn()
    testpage.contact_name("Sirozha")
    testpage.contact_email("sirozha16@mail.ru")
    testpage.contact_content("Good job")
    testpage.click_contact_us_btn()
    time.sleep(testdata['sleep_time'])

    assert testpage.contact_alert() == "Form successfully submitted"