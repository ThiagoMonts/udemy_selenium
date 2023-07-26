from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get('https://www.infomoney.com.br/')

sleep(2)

#TABELA HIGH
#find_element_by_id
# dados1 = driver.find_element(By.ID, 'high').text
# print(dados1)

# #NOME DO FUNDO
# #find_element_by_tag_name
driver.get('https://statusinvest.com.br/fundos-imobiliarios/hglg11')
# dados2 = driver.find_element(By.TAG_NAME, 'h1').text
# print(dados2)

#VALOR ATUAL
#find_element_by_class_name
# dados3 = driver.find_element(By.CLASS_NAME, 'value').text
# print(dados3)

#MIN 52 SEMANAS
#find_elements_by_class_name
# dados4 = driver.find_elements(By.CLASS_NAME, 'value')[1].text
# print(dados4)

#P/VP
#find_elements_by_css_selector
# dados5 = driver.find_element(By.CSS_SELECTOR, '#main-2 > div.container.pb-7 > div:nth-child(5) > div > div:nth-child(2) > div > div:nth-child(1) > strong').text
# print(dados5)

#NUMERO DE COTISTAS
#find_element_by_xpath
dados6 = driver.find_element(By.XPATH, '//*[@id="main-2"]/div[2]/div[5]/div/div[6]/div/div[1]/strong').text
print(dados6)