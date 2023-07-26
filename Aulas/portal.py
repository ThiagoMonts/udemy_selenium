from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, Chrome

#Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

opts = ChromeOptions()

#esta opcao serve para nao fechar o navegador apos a execucao do script
opts.add_experimental_option("detach", True)
servico=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=servico, options=opts)

driver.get("https://www.portaldatransparencia.gov.br/beneficios/consulta?paginacaoSimples=true&tamanhoPagina=&offset=&direcaoOrdenacao=asc&colunasSelecionadas=linkDetalhamento%2ClinguagemCidada%2CmesAno%2Cvalor")
driver.maximize_window()
sleep(2)

#clica no botao de UF
driver.find_element(By.CSS_SELECTOR,"#id-box-filtro > div > div > ul > li:nth-child(4) > div > button").click()
sleep(2)

#clica no estado desejado
driver.find_element(By.CSS_SELECTOR,"#id-box-filtro > div > div > ul > li:nth-child(4) > div > div > div > div.gaveta__corpo > div.btn-group > ul > li:nth-child(28) > a > label > input[type=checkbox]").click()
sleep(2)

#inseri os filtros
driver.find_element(By.CSS_SELECTOR,"#id-box-filtro > div > div > ul > li:nth-child(4) > div > div > div > div.gaveta__corpo > div.btn-group > ul > li:nth-child(2) > input").click()
sleep(2)

#clica no botao de cidade
driver.find_element(By.CSS_SELECTOR,"#id-box-filtro > div > div > ul > li:nth-child(5) > div > button").click()
sleep(2)
driver.find_element(By.NAME, "nomeMunicipio").send_keys("Campinas")
sleep(2)

#clica no botao de adicionar cidade
driver.find_element(By.CSS_SELECTOR,"#id-box-filtro > div > div > ul > li:nth-child(5) > div > div > div > div.gaveta__corpo > input").click()
sleep(2)

#consulta
elementoBotao = driver.find_element(By.ID, "box-filtros-aplicados-com-botao").find_element(By.TAG_NAME, "button")
elementoBotao.click()
sleep(2)

#clica na paginacao completa
paginaCompleta = driver.find_element(By.CLASS_NAME, "botao__gera_paginacao_completa").find_element(By.TAG_NAME, "button")
paginaCompleta.click()
sleep(2)

paginasFim = False

while paginasFim == False:
    tabela = driver.find_element(By.ID, "lista").find_element(By.TAG_NAME, "tbody")
    for linhaAtual in tabela.find_elements(By.TAG_NAME, "tr"):
        print(linhaAtual.text)
    sleep(2)
    try:
        proximaPagina = driver.find_element(By.ID, "lista_next").find_element(By.TAG_NAME, "a")
        proximaPagina.click()
        sleep(2)
    except:
        paginasFim = True

