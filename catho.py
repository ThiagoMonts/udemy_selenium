from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


linksVagas = []

driver.get("https://www.catho.com.br")

driver.maximize_window()

driver.find_element(By.NAME, "q").send_keys("Engenharia de Computação")

sleep(2)

#aceitar cookies
driver.find_element(By.CSS_SELECTOR, "#__next > div.style__OverlayBlock-sc-uz9wat-0.fzodIi > section > div > div:nth-child(3) > div:nth-child(1) > button").click()

sleep(2)

driver.find_element(By.NAME, "submit").click()

sleep(2)

driver.find_element(By.ID, "salary").click()

sleep(2)

#seleciona a opcao a partir de 3 mil
opcaoSalario = driver.find_element(By.ID, "downshift-3-item-4")
opcaoSalario.click()
#driver.find_element_by_id("downshift-3-item-4").click()

elementosVagas = driver.find_elements(By.TAG_NAME, "h2")

for elementoAtual in elementosVagas:
    elementoLink = elementoAtual.find_element(By.TAG_NAME, "a")
    textoLink = elementoLink.get_attribute("href")
    linksVagas.append(textoLink)
    print(textoLink)

for linkAtual in linksVagas:
    driver.get(linkAtual)
    print(driver.find_element(By.TAG_NAME, "h2").text)
    sleep(2)




















#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")