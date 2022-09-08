from selenium import webdriver
from selenium.webdriver.common.by import By
import time

website = "https://twitter.com/TwitterSupport?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
driver = webdriver.Chrome("D:\Downloads\chromedriver")
driver.get(website)
driver.maximize_window()
# Get the initial scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(5)
    # Calculate new scroll height and compare it with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # if the new and last height are equal, it means that there isn't any new page to load, so we stop scrolling
        break
    else:
        last_height = new_height
driver.quit()
