
import time
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://cvenligne.com')
print('Title: %s' % browser.title)



time.sleep(40)
browser.quit()