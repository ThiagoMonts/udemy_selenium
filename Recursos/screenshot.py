from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://statusinvest.com.br/fundos-imobiliarios/knri11")

driver.maximize_window()

driver.get_screenshot_as_file(r"C:\Users\gusta\Documents\imagensBaixadas\screenshot.png")

driver.close()