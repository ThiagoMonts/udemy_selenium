from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www.imdb.com/title/tt0120338/?ref_=fn_al_tt_1")

driver.minimize_window()

driver.implicitly_wait(2) # seconds

driver.maximize_window()

driver.implicitly_wait(2) # seconds

driver.get("https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?chave=hmem_vitrine_13_2106")

driver.back()

driver.implicitly_wait(5) # seconds

driver.forward()

driver.refresh()

driver.implicitly_wait(5) # seconds

driver.close()
