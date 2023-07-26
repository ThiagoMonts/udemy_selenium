from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#exemplo 1

# driver.get("https://www.e-crvsp.sp.gov.br")

# driver.implicitly_wait(3) # seconds

# framePagina = driver.find_elements(By.TAG_NAME, "frame")[1]

# driver.switch_to.frame(framePagina)

# driver.find_element(By.NAME, "codigo").send_keys("informe um cpf válido")
# driver.find_element(By.NAME, "senha").send_keys("123")

#exemplo 2

driver.get("https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/renda-variavel/empresas-listadas.htm")

driver.implicitly_wait(3) # seconds

driver.switch_to.frame("bvmf_iframe")

botao = driver.find_element(By.CSS_SELECTOR, "#accordionName > div > app-companies-home-filter-name > form > div > div:nth-child(4) > button")
botao.click()

dados = driver.find_elements(By.CLASS_NAME, "card-body")
sigla = dados[0].find_element(By.TAG_NAME, "h5").text
nome = dados[0].find_element(By.CLASS_NAME, "card-title").text
descricao = dados[0].find_element(By.CLASS_NAME, "card-text").text
print(sigla)
print(nome)
print(descricao)
