import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path="C:/barryjava/chromedriver.exe")
browser.get('http://10.115.58.83/maPage.html')
print('Title: %s' % browser.title)
time.sleep(10)
browser.quit()