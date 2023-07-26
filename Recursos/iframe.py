from selenium import webdriver
import pandas as pd
#pip3 install pandas

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/derivativos/ajustes-do-pregao/")

driver.switch_to.frame("bvmf_iframe")

tabela = driver.find_element_by_id("tblDadosAjustes")

m = []

for linha in tabela.find_elements_by_tag_name("tr"):
    linhaDados = []
    for coluna in linha.find_elements_by_tag_name("td"):
        linhaDados.append(coluna.text)
    m.append(linhaDados)

df = pd.DataFrame(m)
print(df)

