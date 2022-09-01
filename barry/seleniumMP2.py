import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

testNom = 'kamel malade'

browser = webdriver.Chrome(executable_path="C:/barryjava/chromedriver.exe")
browser.get('http://10.115.58.83:8080/maPage1.html')

elem = browser.find_element(By.NAME, 'nom')  # Find the search box
elem.send_keys('kamel malade' )
elem = browser.find_element(By.NAME, 'bouton')  # Find the search box

elem.click()

div = browser.find_element(By.ID, 'resultat')
result = div.get_attribute('innerHTML')

if result == testNom.upper():
    print('OK')
else :
    print('KO')
    
assert result == testNom.upper()
    
elem = browser.find_element
time.sleep(1)
browser.quit()