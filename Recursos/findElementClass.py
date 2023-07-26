from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

driver.implicitly_wait(3) # seconds

dados0 = driver.find_element_by_class_name("value").text

dados1 = driver.find_elements_by_class_name("value")[0].text

dados2 = driver.find_elements_by_class_name("value")[3].text

dados3 = driver.find_elements_by_class_name("value")[4].text

print(dados0)
print(dados1)
print(dados2)
print(dados3)
