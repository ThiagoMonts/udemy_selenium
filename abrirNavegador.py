from selenium import webdriver #Importação da Biblioteca

#from selenium.webdriver.common.by import By

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com.br")