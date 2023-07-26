from selenium import webdriver #Importação da Biblioteca
from selenium.webdriver.common.by import By

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

driver.implicitly_wait(3) # seconds

nomeFii = driver.find_elements(By.TAG_NAME, "h1")[0].text

valorAtual = driver.find_elements(By.TAG_NAME, "strong")[0].text

tabelaRendimentos = driver.find_elements(By.TAG_NAME, "table")[0].text

tabelaResultados = driver.find_elements(By.TAG_NAME, "table")[1].text

print(nomeFii)
print(valorAtual)
print(tabelaRendimentos)
print(tabelaResultados)

#Exemplos de tags HTML
#https://www.homehost.com.br/blog/tutoriais/tags-html/