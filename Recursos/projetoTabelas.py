from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://br.investing.com/commodities/crude-oil-historical-data")

try:
    driver.find_element_by_id("onetrust-accept-btn-handler").click()
except:
    print("Não existe alerta!")

driver.implicitly_wait(2) # seconds

try:
    driver.find_element_by_css_selector("#PromoteSignUpPopUp > div.right > i").click()
except:
    print("Não existe alerta!")

driver.find_element_by_id("widgetFieldDateRange").click()

dataInicial = driver.find_element_by_id("startDate")
dataFim = driver.find_element_by_id("endDate")

dataInicial.clear()
dataFim.clear()

dataInicial.send_keys("10/01/2019")
dataFim.send_keys("01/01/2021")

driver.find_element_by_id("applyBtn").click()

dados = []
dadosTabela = driver.find_element_by_id("curr_table")

for linha in dadosTabela.find_elements_by_tag_name("tr"):
    linhaDados = []
    for coluna in linha.find_elements_by_tag_name("td"):
        linhaDados.append(coluna.text)
        dados.append(linhaDados)

df = pd.DataFrame(dados)
df = df.iloc[1: , :]

df.columns = ['Data', 'Ultimo', 'Abertura', 'Maxima', 'Minima', 'Vol', 'Var%']

print(df)

# saving the dataframe 
df.to_csv("dadosOil.csv") 


