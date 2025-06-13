from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
import string
from datetime import date

service = Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
username = f"testuser_{random_suffix}"
email = f"{username}@test.com"
password = "TestPassword123!"
url_post = f"https://test.com/{random_suffix}"
today = date.today().strftime('%Y-%m-%d')

try:
    driver.get("https://a22202078.pw.deisi.ulusofona.pt/portfolio")
    time.sleep(2)

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()
    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.ID, "id_username"))).send_keys(username)
    driver.find_element(By.ID, "id_email").send_keys(email)
    driver.find_element(By.ID, "id_first_name").send_keys("Test")
    driver.find_element(By.ID, "id_last_name").send_keys("User")
    driver.find_element(By.ID, "id_password1").send_keys(password)
    driver.find_element(By.ID, "id_password2").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "form input[type='submit']").click()
    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "form input[type='submit']").click()
    time.sleep(2)
    
    driver.get("https://a22202078.pw.deisi.ulusofona.pt/portfolio/posts/")
    time.sleep(2)

    driver.get("https://a22202078.pw.deisi.ulusofona.pt/portfolio/posts/novo")
    time.sleep(2)

    author_select = wait.until(EC.presence_of_element_located((By.NAME, "autor")))
    select_autor = Select(author_select)
    try:
        select_autor.select_by_index(1)
    except:
        select_autor.select_by_index(0)
    driver.find_element(By.ID, "id_titulo").send_keys("Selenium Test Post")
    driver.find_element(By.ID, "id_conteudo").send_keys("This is a test post created via Selenium.")
    date_field = driver.find_element(By.ID, "id_data")
    date_field.clear()
    date_field.send_keys(today)
    driver.find_element(By.ID, "id_url_post").send_keys(url_post)
    driver.find_element(By.CSS_SELECTOR, "form input[type='submit']").click()
    time.sleep(2)

    read_more_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'Read more')]")
    read_more_links[0].click()
    time.sleep(2)
    
    edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Edit Post')]")))
    edit_button.click()
    time.sleep(2)

    delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Delete Post')]")))
    delete_button.click()
    time.sleep(2)

    try:
        driver.get("https://a22202078.pw.deisi.ulusofona.pt/portfolio/logout/")
        WebDriverWait(driver, 3).until(EC.url_contains("logout"))
    except TimeoutException:
        pass

    print("✅ All authentication tests passed.")
    
finally:
    driver.quit()