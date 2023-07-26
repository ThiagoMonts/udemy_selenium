from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://br.investing.com/commodities/crude-oil-historical-data")

try:
    driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
except:
    print("Não existe alerta!")

driver.implicitly_wait(2) # seconds

try:
    driver.find_element(By.CSS_SELECTOR, "#PromoteSignUpPopUp > div.right > i").click()
except:
    print("Não existe alerta!")

driver.find_element(By.CLASS_NAME, "DatePickerWrapper_icon__lXNHQ").click()

dataInicial = driver.find_element(By.ID, "startDate")
dataFim = driver.find_element(By.ID, "endDate")

dataInicial.clear()
dataFim.clear()

dataInicial.send_keys("10/01/2019")
dataFim.send_keys("01/01/2021")

driver.find_element(By.ID, "applyBtn").click()

dados = []
dadosTabela = driver.find_element(By.ID, "curr_table")

for linha in dadosTabela.find_elements(By.TAG_NAME, "tr"):
    linhaDados = []
    for coluna in linha.find_elements(By.TAG_NAME, "td"):
        linhaDados.append(coluna.text)
        dados.append(linhaDados)

df = pd.DataFrame(dados)
df = df.iloc[1: , :]

df.columns = ['Data', 'Ultimo', 'Abertura', 'Maxima', 'Minima', 'Vol', 'Var%']

print(df)

# saving the dataframe 
df.to_csv("dadosOil.csv") 


