import time
# virtualenv myVirtualPython
#  ou
# python -m venv myVirtualPython
#
# pip install -U selenium
# pip install webdriver-manager
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get('http://10.115.57.132/additione.html')
#browser.get('http://10.115.57.130:8080/MapageF.html')
#browser.get('./maPage.html')


def testInput( idChamp, idBouton, idResultat, entree, sortie ):
    elem = browser.find_element(By.ID, idChamp )  # Find the search box
    elem.clear()
    elem.send_keys( entree )

    if idBouton != '':
        bouton = browser.find_element(By.ID, idBouton )
        bouton.click()
    else:
        elem.send_keys( Keys.RETURN )

    div = browser.find_element(By.ID, idResultat)
    result = div. get_attribute( 'innerHTML' )

    print( 'test : ' + entree, '=>', result,  end ='\t' )
    if result == sortie:
        print( 'OK' )
    else: 
        print( 'KO' )


def testaddition(testadd, resultat):
    
    elem = browser.find_element(By.NAME, 'saisie')
    elem.clear()
    elem.send_keys(testadd)
    
    #bouton = browser.find_element(By.NAME, 'raz')
    #bouton.click()
    
    bouton = browser.find_element(By.NAME, 'add')
    bouton.click()
    
    div = browser.find_element(By.NAME, 'resultat')
    result = div. get_attribute( 'innerHTML' )
    print(result)
    if result == resultat :
        print('OK')
    else :
        print('KO')
        
testaddition('15', '15,00&nbsp;€')


def testraz( teraz, resultat):
    elem = browser.find_element(By.NAME, 'saisie')
    elem.clear()
    elem.send_keys(teraz)

    bouton = browser.find_element(By.NAME, 'raz')
    bouton.click()
    
    div = browser.find_element(By.NAME, 'resultat')
    result = div. get_attribute( 'innerHTML' )



def lireResultat(somme):
    elem = browser.find_element(By.ID, 'saisie')
    elem.clear()
    elem.send_keys(somme)

def clickADD():
    bouton = browser.find_element(By.ID, 'add')
    bouton.send_keys()
    
def clickRAZ():
    bouton= browser.find_element(By.ID, 'raz')
    bouton.send_keys()
    
    
time.sleep(40)
browser.quit()