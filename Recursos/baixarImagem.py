from selenium import webdriver
import urllib.request

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www.imdb.com/title/tt0120338/mediaindex?ref_=tt_pv_mi_sm")

driver.implicitly_wait(3) # seconds

divImagens = driver.find_element_by_id("media_index_thumbnail_grid")
primeiraImagem = divImagens.find_elements_by_tag_name("img")[0]
atributoSrc = primeiraImagem.get_attribute("src")
print(atributoSrc)

try:
  urllib.request.urlretrieve(atributoSrc,r"C:\Users\gusta\Documents\imagensBaixadas\teste.jpg")
  print("Imagem Baixada")
except:
  print("Ocorreu um erro")