from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

TWITTER_URL = "https://x.com/i/flow/login"
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
SPEEDTEST_URL = "https://www.speedtest.net/"
TRUE_UP = 100
TRUE_DOWN = 100

chrome_opts = webdriver.ChromeOptions()
chrome_opts.add_experimental_option("detach", True)


class internet_complaint_bot:
    def __init__(self):
        self.chrome_opts = webdriver.ChromeOptions()
        self.chrome_opts.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_opts)
        self.upload = 0
        self.download = 0

    def check_internet_speed(self):
        self.driver.get(SPEEDTEST_URL)

        time.sleep(1.5)
        cookie_accept = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        cookie_accept.click()

        go = self.driver.find_element(By.CSS_SELECTOR, value=".start-button .js-start-test")
        go.click()

        time.sleep(40)
        self.download = float(self.driver.find_element(By.CSS_SELECTOR, value=".result-data .download-speed").text)
        self.upload = float(self.driver.find_element(By.CSS_SELECTOR, value=".result-data .upload-speed").text)
        print(self.download, self.upload)

    def tweet_complaint(self):
        if self.download <= TRUE_DOWN and self.upload <= TRUE_UP:
            self.driver.get(TWITTER_URL)
            time.sleep(3)
            username = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                                                '/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label'
                                                                '/div/div[2]/div/input')
            username.send_keys(USERNAME)
            next1 = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                             'div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')
            next1.click()
            time.sleep(2)
            password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                                'div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div'
                                                                '/label/div/div[2]/div[1]/input')
            password.send_keys(PASSWORD)
            time.sleep(1)
            submit = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div'
                                                              '[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/'
                                                              'button')
            submit.click()

            time.sleep(3)

            tweet_content = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div'
                                                                     '/div/div/div/div[3]/div/div[2]/div[1]/div/div/div'
                                                                     '/div[2]/div[1]/div/div/div/div/div/div/div/div/'
                                                                     'div/div/div/div[1]/div/div/div/div/div/div[2]/'
                                                                     'div/div/div/div')
            tweet_content.send_keys(f"Hey Internet Provider, why is my internet speed {self.download} down/"
                                    f"{self.upload} up, when I pay for {TRUE_DOWN} down/{TRUE_UP} up!")

            time.sleep(1)
            post = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/'
                                                            'div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/'
                                                            'div[2]/div/div/div/button')
            post.click()


complaint = internet_complaint_bot()
complaint.check_internet_speed()
complaint.tweet_complaint()
