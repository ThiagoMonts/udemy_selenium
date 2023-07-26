from selenium import webdriver #Importação da Biblioteca
from selenium.webdriver.common.by import By

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.infomoney.com.br/") #Site que irei acessar

# driver.implicitly_wait(3) # Delay para a página carregar completamente

# dados1 = driver.find_element(By.ID, 'high').text #Irá retornar o texto dentro deste elemento / element - Retorna um elemento único, a primeira ocorrência
# dados2 = driver.find_elements(By.ID,'high')[0].text #Irá retornar o texto dentro deste elemento / elements - Retorna uma lista de elementos

# print(dados1)
# print("-----")
# print(dados2)

driver.get("https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?chave=hmem_vitrine_13_2106")

driver.implicitly_wait(3) # seconds

dados3 = driver.find_element(By.XPATH, '//*[@id="rsyswpsdk"]/div/main/div[2]/div[1]/div/div[2]/h1').text

print(dados3)