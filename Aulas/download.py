from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Importando corretamente a classe Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()  # Usando a classe Options correta

options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\thiag\Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.opera.com/pt-br/download")

spanBotao = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/div[1]/div/span")
linkBotao = spanBotao.find_element(By.TAG_NAME, "a")
linkBotao.click()



