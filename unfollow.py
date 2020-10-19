from selenium import webdriver
from time import sleep

from secrets import password, username


class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
        self.username = username
        self.password = password


    def signIn(self):
        sleep(3)
        self.driver.get("https://www.instagram.com")
        sleep(3)
        login_link = self.driver.find_element_by_name("username")
        login_link.click()
        print('Found name')

        username_input = self.driver.find_element_by_css_selector("input[name='username']")
        password_input = self.driver.find_element_by_css_selector("input[name='password']")
        print('Pressed input')

        username_input.send_keys(username)
        password_input.send_keys(password)
        print('Inserted username/password')

        login_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        print('Hit login button')

        sleep(3)

        save_password_button = self.driver.find_element_by_xpath("//button[@type='button']")
        save_password_button.click()
        print('Hit "not now" button')

        sleep(5)

        notification_button = self.driver.find_element_by_css_selector('button.aOOlW:nth-child(2)')
        notification_button.click()
        print('Notification "not now"')

    # Note: Instagram suspects accounts for mass unfollowing, so it's
    # better not to exceed ~500 accounts per 24 hours
    def unfollow(self, account):
        self.driver.get('https://www.instagram.com/' + account + '/')
        sleep(2)  # not necessary
        try:
            unfollowButton = self.driver.find_element_by_css_selector('._6VtSN')

            unfollowButton.click()
            sleep(2)
            unfollowConfirmation = self.driver.find_element_by_css_selector('button.aOOlW:nth-child(1)')
            unfollowConfirmation.click()
            print(account,"is unfollowed")
            sleep(10)

        except:
            print("You're not following " + account)


    def closeBrowser(self):
            self.driver.quit()


    def __exit__(self, exc_type, exc_value, traceback):
        self.closeBrowser()

# compare follows/followers lists to find out
# who hasn't followed back and write 'unfollow.txt' with them

follows_list = []
followers_list = []

with open("follows.txt", 'r') as f:
    for line in f:
        name = line.strip('\n')
        follows_list.append(name)

with open("followers.txt", 'r') as f:
    for line in f:
        name = line.strip('\n')
        followers_list.append(name)

s = set(followers_list)
unfollow_list = [x for x in follows_list if x not in s]
estimated_time = len(unfollow_list) * 4 / 60 + len(unfollow_list) / 5

with open('unfollow.txt', 'w') as f:
    for i in range(len(unfollow_list)):
        line = unfollow_list[i] + '\n'
        f.write(line)

print("There's {} users to unsubscribe".format(len(unfollow_list)))
print("Estimated time is {} min".format(estimated_time))
print(unfollow_list)

my_bot = Instabot(username, password)
my_bot.signIn()

with open('unfollow.txt', 'r') as file:
    count = 0
    for name in file:
        count += 1
        account = name[1:]
        print("{} out of {}".format(count, len(unfollow_list)))
        my_bot.unfollow(account)

my_bot.closeBrowser()