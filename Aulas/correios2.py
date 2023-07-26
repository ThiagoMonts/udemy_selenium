from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from time import sleep
import pandas as pd
#pip3 install xlsxwriter
import xlsxwriter

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

df = pd.read_excel (r'C:\Users\thiag\Downloads\03 Extração de dados\fretes.xlsx')

precos = []
prazos = []

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www2.correios.com.br/sistemas/precosprazos/")

for index, row in df.iterrows():

  driver.find_element(By.NAME, "cepOrigem").send_keys(str(row['origem']))

  sleep(1)

  driver.find_element(By.NAME, "cepDestino").send_keys(str(row['destino']))

  sleep(1)

  Select(driver.find_element(By.NAME, "servico")).select_by_index(15)

  sleep(1)

  Select(driver.find_element(By.NAME, "embalagem1")).select_by_index(2)

  driver.find_element(By.NAME, "Altura").send_keys(int(row['altura']))

  driver.find_element(By.NAME, "Largura").send_keys(int(row['largura']))

  driver.find_element(By.NAME, "Comprimento").send_keys(int(row['comprimento']))

  driver.find_element(By.NAME, "peso").send_keys(int(row['peso']))

  driver.find_element(By.NAME, "ckValorDeclarado").click()

  sleep(1)

  driver.find_element(By.NAME, "valorDeclarado").send_keys(str(row['valor']))

  sleep(1)

  driver.find_element(By.NAME, "Calcular").click()

  driver.switch_to.window(driver.window_handles[1])

  tempoEntrega = driver.find_elements(By.CLASS_NAME, "destaque")[0].find_element(By.TAG_NAME, "td").text

  preco = driver.find_elements(By.CLASS_NAME, "destaque")[1].find_element(By.TAG_NAME, "td").text

  prazos.append(tempoEntrega)
  precos.append(preco)

  sleep(2)

  driver.close()
  driver.switch_to.window(driver.window_handles[0])
  driver.refresh()


data = {'origem': df.iloc[:,0], 'destino': df.iloc[:,1], 'altura': df.iloc[:,2], 'largura': df.iloc[:,3], 'comprimento': df.iloc[:,4], 'peso': df.iloc[:,5], 'valor': df.iloc[:,6], 'prazo': prazos, 'precos': precos} 
df2 = pd.DataFrame(data)

df2.to_excel('output.xlsx', engine='xlsxwriter')  	
print(df2)