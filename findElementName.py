from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.imdb.com/")

driver.implicitly_wait(3)

campoBusca = driver.find_element(By.NAME, "q")

campoBusca.send_keys("Titanic")
