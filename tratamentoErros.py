from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# driver.get("https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s20-fe-128gb-cloud-navy-4g-6gb-ram-tela-65-cam-tripla-selfie-32mp/p/155629800/te/tcsp/")

driver.get("https://www.magazineluiza.com.br/jogo-de-copos-de-vidro-45ml-6-pecas-copo-americano-color-dose/p/226542700/ud/coco/")

driver.implicitly_wait(3) # seconds

#avaliacao = driver.find_element(By.CLASS_NAME, "js-rating-value").text

try:
    avaliacao = driver.find_element(By.CLASS_NAME, "js-rating-value").text
except:
    avaliacao = "Não avaliado"

print(avaliacao)