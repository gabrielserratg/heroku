from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("/app/googlechrome/bin/google-chrome")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("/app/.chromedriver/bin/chromedriver"), chrome_options=chrome_options)

driver.get("https://www.twitch.tv/gabriel_nerd_br")
print(driver.page_source)
print("Funcionando!!")
