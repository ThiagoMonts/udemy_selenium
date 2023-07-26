from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.imdb.com/title/tt0120338/mediaindex?ref_=tt_pv_mi_sm")

driver.implicitly_wait(3) # seconds

divImagens = driver.find_element(By.ID, "media_index_thumbnail_grid")
primeiraImagem = divImagens.find_elements(By.TAG_NAME, "img")[0]
atributoSrc = primeiraImagem.get_attribute("src")
print(atributoSrc)

try:
  urllib.request.urlretrieve(atributoSrc,r"C:\Users\thiag\Downloads\teste.jpg")
  print("Imagem Baixada")
except:
  print("Ocorreu um erro")