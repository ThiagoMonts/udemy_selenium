from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.imdb.com/")

driver.find_element(By.NAME, "q").send_keys("Titanic")

driver.implicitly_wait(2) # seconds

driver.find_element(By.ID, "suggestion-search-button").click()
