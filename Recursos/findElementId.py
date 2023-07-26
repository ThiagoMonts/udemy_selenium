from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www.infomoney.com.br/")

driver.implicitly_wait(3) # seconds

dados1 = driver.find_element_by_id("high").text
dados2 = driver.find_elements_by_id("high")[0].text

print(dados1)
print("-----")
print(dados2)

driver.get("https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?chave=hmem_vitrine_13_2106")

driver.implicitly_wait(3) # seconds

dados3 = driver.find_element_by_id("product-name-default").text

print(dados3)