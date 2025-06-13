from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    driver.get('https://a22202078.pw.deisi.ulusofona.pt/portfolio')
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Architecture").click()
    time.sleep(2)
    assert "Technical Presentation" in driver.page_source

    driver.find_element(By.LINK_TEXT, "Projects").click()
    time.sleep(2)
    assert "My Projects" in driver.page_source

    driver.find_element(By.LINK_TEXT, "Tools").click()
    time.sleep(2)
    assert "Technologies Used" in driver.page_source or "Technologies" in driver.page_source

    driver.find_element(By.LINK_TEXT, "CV").click()
    time.sleep(2)
    assert "Curriculum Vitae" in driver.page_source

    print("✅ All navigation tests passed.")

finally:
    driver.quit()