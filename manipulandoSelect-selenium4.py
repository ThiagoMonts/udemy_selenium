from selenium import webdriver
from selenium.webdriver.support.ui import Select

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

opts = ChromeOptions()
#esta opcao serve para nao fechar o navegador apos a execucao do script
opts.add_experimental_option("detach", True)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)

driver.get("https://www.imdb.com/title/tt0120338/videogallery/")

elementoSelect = Select(driver.find_element(By.NAME, 'sort'))

elementoSelect.select_by_value('expiration')

driver.implicitly_wait(2) # seconds

elementoSelect = Select(driver.find_element(By.NAME, 'sort'))

elementoSelect.select_by_visible_text('Date')

Select(driver.find_element(By.NAME, 'sort')).select_by_index(1)

#Documentacao
#https://selenium-python.readthedocs.io/api.html
