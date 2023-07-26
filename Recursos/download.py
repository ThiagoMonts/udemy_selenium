from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\gusta\Documents\dadosDownload",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome(chrome_options=options,executable_path=r"C:\Users\gusta\Documents\driver\chromedriver.exe")

driver.get("https://www.opera.com/pt-br/download")

spanBotao = driver.find_element_by_xpath("/html/body/main/section[1]/div/div/div[1]/div/span")
linkBotao = spanBotao.find_element_by_tag_name("a")
linkBotao.click()



