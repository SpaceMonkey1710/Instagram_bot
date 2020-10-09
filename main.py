from time import sleep
from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'E:\\Projects\\Instagram_bot\\geckodriver.exe')
browser.get('https://wwww.instagram.com/')
sleep(5)
browser.close()

# driver = webdriver.Firefox('geckodriver.exe')

