from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time


TARGET_ACCOUNT = INSTAGRAM ACCOUNT YOU WANT TO TARGET
USERNAME = YOUR INSTAGRAM EMAIL
PASSWORD = YOUR INSTAGRAM PASSWORD

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        model = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", model)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


    def logout(self):
        profile_img = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img')
        profile_img.click()

        time.sleep(1)
        log_out = self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div')
        log_out.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
bot.logout()