from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()  # Usando a classe Options correta

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

driver.maximize_window()

driver.get_screenshot_as_file(r"C:\Users\thiag\Downloads\screenshot.png")

driver.close()