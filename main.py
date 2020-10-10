from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep

'''options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\geckodriver\geckodriver.exe')
driver.get("http://www.instagram.com/")
print ("Headless Firefox Initialized")
driver.quit()''' # working start in case of fail

browser = webdriver.Firefox(executable_path=r'C:\geckodriver\geckodriver.exe')
browser.implicitly_wait(5) # устанавливаем пятисекундную задержку
# Если Selenium не может найти элемент, он ждет, чтобы все загрузилось и пытается снова

browser.get('https://www.instagram.com/')
browser.implicitly_wait(5)
# Следующие строки говорят боту найти ссылку с текстом Log in и кликнуть по ней.
login_link = browser.find_element_by_name("username")
login_link.click()
print('found name')

sleep(3)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")
print('pressed input')

username_input.send_keys("among_us.russia")
password_input.send_keys("TrySomethingNew")
print('inserted username/password')

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()
print('hit login button')

sleep(3)

save_password_button = browser.find_element_by_xpath("//button[@type='button']")
save_password_button.click()
print('hit "not now" button')

sleep(3)

notification_button = browser.find_element_by_css_selector('button.aOOlW:nth-child(2)')
notification_button.click()
print('notification "not now"')


sleep(10)

#browser.close()