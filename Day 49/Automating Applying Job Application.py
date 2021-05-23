from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time


ACCOUNT_EMAIL = YOUR LOGIN EMAIL
ACCOUNT_PASSWORD = YOUR LOGIN PASSWORD
PHONE = YOUR PHONE NUMBER


chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)


driver.get("https://www.linkedin.com/jobs/search/?geoId=106300413&keywords=python%20developer&location=Maharashtra%2C%20India")


time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()
time.sleep(5)


email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)


time.sleep(5)


jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")


for job in jobs:
    print("called")
    job.click()
    time.sleep(2)

    #Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        #If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_css_selector("footer button")

        #If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        #Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    #If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()