from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

driver.implicitly_wait(3) # seconds

nomeFii = driver.find_elements_by_tag_name("h1")[0].text

valorAtual = driver.find_elements_by_tag_name("strong")[0].text

tabelaRendimentos = driver.find_elements_by_tag_name("table")[0].text

tabelaResultados = driver.find_elements_by_tag_name("table")[1].text

print(nomeFii)
print(valorAtual)
print(tabelaRendimentos)
print(tabelaResultados)

#Exemplos de tags HTML
#https://www.homehost.com.br/blog/tutoriais/tags-html/