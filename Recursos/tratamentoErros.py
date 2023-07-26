import selenium.webdriver

driver = selenium.webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

#driver.get("https://www.magazineluiza.com.br/smartphone-samsung-galaxy-s20-fe-128gb-cloud-navy-4g-6gb-ram-tela-65-cam-tripla-selfie-32mp/p/155629800/te/tcsp/")

driver.get("https://www.magazineluiza.com.br/jogo-de-copos-de-vidro-45ml-6-pecas-copo-americano-color-dose/p/226542700/ud/coco/")

driver.implicitly_wait(3) # seconds

#avaliacao = driver.find_element_by_class_name("js-rating-value").text

try:
    avaliacao = driver.find_element_by_class_name("js-rating-value").text
except:
    avaliacao = "Não avaliado"

print(avaliacao)