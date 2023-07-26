from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www.imdb.com/")

driver.implicitly_wait(3) # seconds

campoBusca = driver.find_elements_by_name("q")[0]

campoBusca.send_keys("Titanic")


