from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

from secrets import password, username



follows_list = []
followers_list = []

with open("follows.txt", 'r') as f:
    for line in f:
        name = line.strip('\n')
        follows_list.append(name)
print(follows_list)

with open("followers.txt", 'r') as f:
    for line in f:
        name = line.strip('\n')
        followers_list.append(name)
print(followers_list)

s = set(followers_list)
unfollow_list = [x for x in follows_list if x not in s]

print("There's {} motherfuckers to unsubscribe".format(len(unfollow_list)))
print(unfollow_list)




class Instabot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

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
        profile = self.driver.find_element_by_css_selector('.gmFkV')
        profile.click()
        print('Opened profile')

    def unfollow(self):
        wait = WebDriverWait(self.driver, 10)
        for name in range(len(unfollow_list)):
            sleep(3)
            search_field = self.driver.find_element_by_xpath('//div[@class="LWmhU _0aCwM"]')
            search_field.click()
            search_field.send_keys(name, Keys.ENTER)





my_bot = Instabot(username, password)
my_bot.unfollow()
