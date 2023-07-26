from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

#driver.get("https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?chave=hmem_vitrine_13_2106")

#driver.implicitly_wait(3) # seconds

#driver.find_element_by_id("btn-buy").click()

#Outra forma de fazer
#botao = driver.find_element_by_id("btn-buy")
#botao.click()

driver.get("https://www.imdb.com/")

driver.find_elements_by_name("q")[0].send_keys("Titanic")

driver.implicitly_wait(2) # seconds

driver.find_element_by_id("suggestion-search-button").click()