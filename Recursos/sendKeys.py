from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www.imdb.com/")

driver.implicitly_wait(3) # seconds

driver.find_elements_by_name("q")[0].send_keys("Titanic" + Keys.RETURN)



