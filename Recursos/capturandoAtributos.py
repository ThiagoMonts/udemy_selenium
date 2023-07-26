from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

elementoAImagem = driver.find_elements_by_class_name("navbar-brand")[0]
elementoImg = elementoAImagem.find_element_by_tag_name("img")
atributoSrc = elementoImg.get_attribute("src")
print(atributoSrc)

driver.get("https://www.melhorcambio.com/dolar-hoje")

elementoCotacao = driver.find_element_by_id("comercial")
valorCotacao = elementoCotacao.get_attribute("value")
classeElemento = elementoCotacao.get_attribute("class")
tipoElemento = elementoCotacao.get_attribute("type")

print(valorCotacao)
print(classeElemento)
print(tipoElemento)

driver.close()