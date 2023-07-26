from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.imdb.com/title/tt0120338/?ref_=fn_al_tt_1")

driver.minimize_window() # Minimiza a janela do navegador

driver.implicitly_wait(2) # seconds

driver.maximize_window() # Maximiza a janela do navegador

driver.implicitly_wait(2) # seconds

driver.get("https://empresas.americanas.com.br/produto/1611315933/iphone-11-apple-64gb-preto-tela-6-1-4g-camera-12mp-ios?chave=hmem_vitrine_13_2106")

driver.back() # Volta para a página anterior

driver.implicitly_wait(5) # seconds

driver.forward() # Avança para a página seguinte

driver.refresh() # Atualiza a página

driver.implicitly_wait(5) # seconds

driver.close() # Fecha a janela do navegador
