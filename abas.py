from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://br.gearbest.com/cell-phones/pp_009571511665.html?wid=1349303")

driver.implicitly_wait(3) # seconds

#https://www.geeksforgeeks.org/execute_script-driver-method-selenium-python/
driver.execute_script("window.open()")

# Switch to the newly opened tab
driver.switch_to.window(driver.window_handles[1])

driver.get("https://www.melhorcambio.com/dolar-hoje")

driver.implicitly_wait(3) # seconds

driver.switch_to.window(driver.window_handles[0])

driver.close()






