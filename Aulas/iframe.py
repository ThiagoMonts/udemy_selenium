from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/derivativos/ajustes-do-pregao/")

driver.switch_to.frame("bvmf_iframe")

tabela = driver.find_element(By.ID, "tblDadosAjustes")

m = []

for linha in tabela.find_elements(By.TAG_NAME, "tr"):
    linhaDados = []
    for coluna in linha.find_elements(By.TAG_NAME, "td"):
        linhaDados.append(coluna.text)
    m.append(linhaDados)

df = pd.DataFrame(m)
print(df)

