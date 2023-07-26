from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

driver.implicitly_wait(3) # seconds

valorTabela = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div[8]/div/div[7]/div/div[2]/table/tbody/tr[3]/td[3]")[0].text

proventos = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div[8]/div/div[7]/div/div[1]/div[1]/div/div/strong")[0].text

volumeAluguel = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div[11]/div[2]/div[4]/div/div[1]/strong")[0].text

nomeAdministrador = driver.find_elements(By.XPATH, "/html/body/main/div[3]/div/div/div[3]/div/div[2]/div[1]/div/strong")[0].text

print(valorTabela)

print(proventos)

print(volumeAluguel)

print(nomeAdministrador)

