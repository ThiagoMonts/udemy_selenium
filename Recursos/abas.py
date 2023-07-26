from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

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






