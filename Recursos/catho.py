from time import sleep
from selenium import webdriver

linksVagas = []

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www.catho.com.br")

driver.maximize_window()

driver.find_element_by_name("q").send_keys("Engenharia de Computação")

sleep(2)

#aceitar cookies
driver.find_element_by_css_selector("#__next > div.style__OverlayBlock-sc-uz9wat-0.fzodIi > section > div > div:nth-child(3) > div:nth-child(1) > button").click()

sleep(2)

driver.find_element_by_name("submit").click()

sleep(2)

driver.find_element_by_id("salary").click()

sleep(2)

#seleciona a opcao a partir de 3 mil
opcaoSalario = driver.find_element_by_id("downshift-3-item-4")
opcaoSalario.click()
#driver.find_element_by_id("downshift-3-item-4").click()

elementosVagas = driver.find_elements_by_tag_name("h2")

for elementoAtual in elementosVagas:
    elementoLink = elementoAtual.find_element_by_tag_name("a")
    textoLink = elementoLink.get_attribute("href")
    linksVagas.append(textoLink)
    print(textoLink)

for linkAtual in linksVagas:
    driver.get(linkAtual)
    print(driver.find_element_by_tag_name("h2").text)
    sleep(2)




















#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")