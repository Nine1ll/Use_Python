from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&authuser=0&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("포켓몬")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
        except:
            break
    last_height = new_height

counts = 1
images = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
for image in images:
    try:
        image.click()
        time.sleep(2)
        image_url = driver.find_element(By.CSS_SELECTOR,".n3VNCb.KAlRDb").get_attribute("src")
        urllib.request.urlretrieve(image_url, str(counts)+".jpg")
        counts = counts + 1
    except:
        pass

driver.close()
