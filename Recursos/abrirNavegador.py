from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

#driver = selenium.Firefox(executable_path=r"C:\Users\gusta\Documents\driver\....exe)

driver.get("https://www.google.com.br")