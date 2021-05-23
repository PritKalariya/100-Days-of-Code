from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


ACCOUNT_EMAIL = YOUR_LOGIN_EMAIL
ACCOUNT_PASSWORD = YOUR_LOGIN_PASSWORD


chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)


driver.get("https://www.linkedin.com/jobs/search/?geoId=106300413&keywords=python%20developer&location=Maharashtra%2C%20India")


sign_in_button = driver.find_element_by_link_text("nav__button-secondary")
time.sleep(3)
sign_in_button.click()
time.sleep(5)


email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)


sign_in = driver.find_element_by_id("login__form_action_container")
sign_in.click()
time.sleep(3)


# Retreive all search results and add to a list.
jobs = driver.find_element_by_class_name("jobs-search-results__list-item")


# For each job in the job lsit, click the save button, scroll down to the bottom of the right hand pane and then click the follow button
for job in jobs:
    job.click()
    time.sleep(4)
    save_button = driver.find_element_by_class_name("jobs-save-button")
    save_button.click()
    time.sleep(2)

    # Click the right hand pane and scroll down to the bottom of the page to reveal the follow button
    job_detail = driver.find_element_by_class_name("jobs-search__right-rail")
    job_detail.click()

    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)
    time.sleep(2)

    # Exception handling for instances in which the company does not have a follo button
    try:
        follow = driver.find_elements_by_class_name("follow")
        follow.clik()
        time.sleep(2)
    except NoSuchElementException:
        continue