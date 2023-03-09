# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

chrome.refresh()

# navigam catre un url
chrome.get('https://www.mega-image.ro/')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

#vrem sa dam click pe buttonul accept de la cookies
chrome.find_element(By.XPATH, '//button[@data-testid="cookie-popup-accept"]').click()
sleep(3)

#vrem sa dam click pe buttonul contul meu
chrome.find_element(By.XPATH, '//button[@data-testid="header-myhub-toggle"]').click()
sleep(3)

#vrem sa introducem un email invalid
chrome.find_element(By.XPATH, '//input[@data-testid="input-field"]').send_keys('abec1234')
sleep(3)

#vrem sa dam click pe buttonul continua
chrome.find_element(By.XPATH, '//button[@data-testid="submit-button"]').click()
sleep(3)


# vrem sa verificam mesajul de eroare pentru un email invalid
mesaj_eroare = chrome.find_element(By.XPATH, '//p[@data-testid="form-error-message"]').text
assert mesaj_eroare == 'Te rugam sa introduci un format valid'
sleep(3)

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')