from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from time import sleep

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www2.correios.com.br/sistemas/precosprazos/")

driver.find_element(By.NAME, "cepOrigem").send_keys("31630900")

sleep(1)

driver.find_element(By.NAME, "cepDestino").send_keys("35400000")

sleep(1)

#pac
Select(driver.find_element(By.NAME, "servico")).select_by_index(15)

sleep(1)

Select(driver.find_element(By.NAME, "embalagem1")).select_by_index(2)

driver.find_element(By.NAME, "Altura").send_keys("10")

driver.find_element(By.NAME, "Largura").send_keys("10")

driver.find_element(By.NAME, "Comprimento").send_keys("15")

driver.find_element(By.NAME, "peso").send_keys("3")

driver.find_element(By.NAME, "ckValorDeclarado").click()

sleep(1)

driver.find_element(By.NAME, "valorDeclarado").send_keys("300000")

sleep(1)

driver.find_element(By.NAME, "Calcular").click()

driver.switch_to.window(driver.window_handles[1])

tempoEntrega = driver.find_elements(By.CLASS_NAME, "destaque")[0].find_element(By.TAG_NAME, "td").text

print(tempoEntrega)

preco = driver.find_elements(By.CLASS_NAME, "destaque")[1].find_element(By.TAG_NAME, "td").text

print(preco)