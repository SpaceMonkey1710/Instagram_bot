from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from secrets import password, username

import requests, pickle, json, os, random
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains


class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')

        self.driver.get("https://www.instagram.com")

        sleep(5)

        login_link = self.driver.find_element_by_name("username")
        login_link.click()
        print('found name')

        sleep(3)

        username_input = self.driver.find_element_by_css_selector("input[name='username']")
        password_input = self.driver.find_element_by_css_selector("input[name='password']")
        print('pressed input')

        username_input.send_keys(username)
        password_input.send_keys(password)
        print('inserted username/password')

        login_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        print('hit login button')

        sleep(3)

        save_password_button = self.driver.find_element_by_xpath("//button[@type='button']")
        save_password_button.click()
        print('hit "not now" button')

        sleep(5)

        notification_button = self.driver.find_element_by_css_selector('button.aOOlW:nth-child(2)')
        notification_button.click()
        print('notification "not now"')

        sleep(5)

    def get_unfollowers(self):
        wait = WebDriverWait(self.driver, 10)

        profile = self.driver.find_element_by_css_selector('.gmFkV')
        profile.click()
        print('Opened profile')
        following_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/following')]")))
        following_list.click()  # IT clicks the following and gives window of following list
        print("CLicked following list")

        numfollows = self.driver.find_element_by_css_selector('li.Y8-fY:nth-child(3) > a:nth-child(1) > span:nth-child(1)').text
        numfollows = int(numfollows.replace(" ", ""))
        estimated_time = numfollows / 6 * 2 / 60
        print('The number of follows is {}, estimated time is {:.2f} min'.format(numfollows, estimated_time) )
        fBody = self.driver.find_element_by_css_selector("div[class='isgrP']")
        scrolling_times = round((numfollows / 4))
        scroll = 0
        while scroll <= scrolling_times:
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                fBody)
            sleep(2)
            scroll += 1
            print('{} out of {}'.format(scroll, scrolling_times))



my_bot = Instabot(username, password)
my_bot.get_unfollowers()