from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www.imdb.com/title/tt0120338/videogallery/")

elementoSelect = Select(driver.find_element_by_name("sort"))

elementoSelect.select_by_value('expiration')

driver.implicitly_wait(2) # seconds

elementoSelect = Select(driver.find_element_by_name("sort"))

elementoSelect.select_by_visible_text('Date')

Select(driver.find_element_by_name("sort")).select_by_index(1)

#Documentacao
#https://selenium-python.readthedocs.io/api.html
