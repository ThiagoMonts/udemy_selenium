from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)

driver.get("https://www.imdb.com/chart/top/")

linksFilmes = driver.find_element(By.TAG_NAME,"table").find_elements(By.TAG_NAME, "a")
links = []
planilha = []
linha = []

i = 0
contador = 0
while i < 500:
    links.append(linksFilmes[i].get_attribute("href"))
    i = i + 2

for linkAtual in links:
    driver.get(linkAtual)
    sleep(3)
    nomeFilme = driver.find_element(By.CSS_SELECTOR,"#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-f9e7f53-0.ifXVtO > section > div:nth-child(4) > section > section > div.sc-b5e8e7ce-0.dZsEkQ > div.sc-b5e8e7ce-1.kNhUtn > h1")
    nomeFilme = nomeFilme.text
    linha.append(nomeFilme)
    
    anoLancamento = driver.find_element(By.CSS_SELECTOR, "#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-f9e7f53-0.ifXVtO > section > div:nth-child(4) > section > section > div.sc-b5e8e7ce-0.dZsEkQ > div.sc-b5e8e7ce-1.kNhUtn > div > ul > li:nth-child(1)")
    anoLancamento = anoLancamento.text
    linha.append(anoLancamento)
    
    duracao = driver.find_element(By.CSS_SELECTOR, "#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-f9e7f53-0.ifXVtO > section > div:nth-child(4) > section > section > div.sc-b5e8e7ce-0.dZsEkQ > div.sc-b5e8e7ce-1.kNhUtn > div > ul > li:nth-child(3)")
    duracao = duracao.text
    linha.append(duracao)
    
    avaliacao = driver.find_elements(By.CLASS_NAME, "ipc-btn__text")[6].find_element(By.TAG_NAME, "span")
    avaliacao = avaliacao.get_attribute('innerText')
    linha.append(avaliacao)
    
    #https://www.microfocus.com/documentation/silk-test/200/en/silktestworkbench-help-en/SILKTEST-21EEFF3F-DIFFERENCEBETWEENTEXTCONTENTSINNERTEXTINNERHTML-REF.html
    try:
        descricao = driver.find_element(By.CSS_SELECTOR, "#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-f9e7f53-0.ifXVtO > section > div:nth-child(4) > section > section > div.sc-663f405c-2.lhDUmU > div.sc-663f405c-10.iWYzPQ > div.sc-663f405c-4.hQbEKe > div.sc-6cc92269-8.hmNIYl.sc-663f405c-11.kHBavT > p > span.sc-6cc92269-1.dzxjtm")
        descricao = descricao.get_attribute('innerText')
    except:
        descricao = "O dado não existe na página"
    linha.append(descricao)
    
    try:
        diretor = driver.find_element(By.CSS_SELECTOR, "#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-f9e7f53-0.ifXVtO > section > div:nth-child(4) > section > section > div.sc-663f405c-2.lhDUmU > div.sc-663f405c-10.iWYzPQ > div.sc-663f405c-4.hQbEKe > div.sc-b13e9d78-0.fgzezW > ul > li:nth-child(1) > div > ul > li > a") 
        diretor = diretor.get_attribute('innerText')
    except:
        diretor = "O dado não existe na página"
    linha.append(diretor)
    
    
    planilha.append(linha)
    linha = []
    contador = contador + 1
    
df = pd.DataFrame(planilha)
df.columns = ['Nome', 'Lançamento','Duração','Nota IMDB', 'Descrição' ,'Diretor']
df.to_excel("C:/Users/gusta/Downloads/filmes/rankFilmes.xlsx")
print("Salvei o arquivo")
    