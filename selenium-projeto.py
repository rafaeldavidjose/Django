from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import random
import string

service = Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
username = f"testuser_{random_suffix}"
email = f"{username}@test.com"
password = "TestPassword123!"

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
    
    driver.get("https://a22202078.pw.deisi.ulusofona.pt/portfolio/projetos/")
    time.sleep(2)

    driver.get("https://a22202078.pw.deisi.ulusofona.pt/portfolio/projetos/novo")
    time.sleep(2)

    driver.find_element(By.ID, "id_titulo").send_keys("Sistema de Gestão de Biblioteca")
    driver.find_element(By.ID, "id_descricao").send_keys("Aplicação web desenvolvida em Django para gestão completa de uma biblioteca universitária, incluindo catálogo de livros, sistema de empréstimos e gestão de utilizadores.")
    
    try:
        driver.find_element(By.ID, "id_link_github").send_keys("https://github.com/test/biblioteca-sistema")
    except NoSuchElementException:
        pass
    
    try:
        driver.find_element(By.ID, "id_link_video").send_keys("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    except NoSuchElementException:
        pass

    driver.find_element(By.ID, "id_conceitos_aplicados").send_keys("Programação Orientada a Objetos, Padrão MVC, Base de Dados Relacionais, Autenticação de Utilizadores, API REST")
    
    try:
        driver.find_element(By.ID, "id_aspetos_tecnicos").send_keys("Implementação usando Django Framework, PostgreSQL como base de dados, Bootstrap para interface responsiva, deployment em servidor Linux com Nginx")
    except NoSuchElementException:
        pass

    disciplina_select = wait.until(EC.presence_of_element_located((By.ID, "id_disciplina")))
    select_disciplina = Select(disciplina_select)
    try:
        select_disciplina.select_by_index(1)
    except:
        select_disciplina.select_by_index(0)

    try:
        tecnologias_select = driver.find_element(By.ID, "id_tecnologias")
        select_tecnologias = Select(tecnologias_select)
        if len(select_tecnologias.options) > 1:
            select_tecnologias.select_by_index(1)
            if len(select_tecnologias.options) > 2:
                select_tecnologias.select_by_index(2)
    except NoSuchElementException:
        pass

    driver.find_element(By.CSS_SELECTOR, "form input[type='submit']").click()
    time.sleep(2)

    view_details_links = driver.find_elements(By.XPATH, "//a[contains(text(), 'View Details')]")
    view_details_links[-1].click()
    time.sleep(2)

    edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Edit Project')]")))
    edit_button.click()
    time.sleep(2)

    titulo_field = driver.find_element(By.ID, "id_titulo")
    titulo_field.clear()
    titulo_field.send_keys("Sistema de Gestão de Biblioteca - Versão Atualizada")
    
    descricao_field = driver.find_element(By.ID, "id_descricao")
    descricao_field.clear()
    descricao_field.send_keys("Aplicação web desenvolvida em Django para gestão completa de uma biblioteca universitária, com funcionalidades avançadas de pesquisa, relatórios automáticos e integração com sistemas externos.")

    driver.find_element(By.CSS_SELECTOR, "form input[type='submit']").click()
    time.sleep(2)
    
    edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Edit Project')]")))
    edit_button.click()
    time.sleep(2)

    delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Delete Project')]")))
    delete_button.click()
    time.sleep(2)

    try:
        driver.get("https://a22202078.pw.deisi.ulusofona.pt/portfolio/logout/")
        WebDriverWait(driver, 3).until(EC.url_contains("logout"))
    except TimeoutException:
        pass
    
    print("✅ All project tests passed.")

finally:
    driver.quit()