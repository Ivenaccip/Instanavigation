import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# Code extraction
import pyautogui
import subprocess
# SQL
from sqlalchemy import create_engine
#code Linea Argument
import sys

def handle_consent_popup():
    # Esperar hasta 10 segundos para que aparezca el cuadro de diálogo
    wait = WebDriverWait(driver, 4)
    try:
        popup_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.fc-dialog.fc-choice-dialog")))
        
        # Verificar si el cuadro de diálogo está presente
        if popup_element.is_displayed():
            # Encontrar y hacer clic en el botón de consentimiento
            consent_button = driver.find_element(By.CSS_SELECTOR, "button.fc-button.fc-cta-consent.fc-primary-button")
            consent_button.click()
    except:
        print("No se encontró el popup de consentimiento o hubo un error al interactuar con él.")

def consentimiento(profile_url):
    # Extraer el nombre de usuario del enlace de Instagram
    username = profile_url.split("https://www.instagram.com/")[-1].strip('/')

    # Reemplazar espacios con guiones bajos
    safe_filename = username.replace(" ", "_")
    
    # Crear el nuevo URL para instanavigation
    url = f"https://instanavigation.com/user-profile/{username}/"
    
    driver.get(url)
    handle_consent_popup()
    handle_not_found_popup()
    sleep(1)
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)
    except Exception as e:
        print("Error with scroll:", e)
    try:
        # Encontrar el elemento div con las clases especificadas y hacer clic en él
        element = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.profile-publications__btn:nth-child(3)")))

        element.click()
        print("click")
        sleep(2)
    except Exception as e:
        print("Xpath didn't find")
        sleep(2)
    # Presionar 'ctrl' + 'u' para abrir el código fuente de la página
    pyautogui.hotkey('ctrl', 'u')
    pyautogui.hotkey('ctrl', 's')
    print(safe_filename)
    sleep(1)
    pyautogui.write(safe_filename)
    sleep(1)
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'w')

def carga_de_perfil(profile_link):
    url = f"https://instanavigation.com/"
    try:
        driver.get(url)
    except UnexpectedAlertPresentException:
        alert = driver.switch_to.alert
        print(alert.text)
        alert.dismiss()
        driver.refresh()
    sleep(1)
    handle_consent_popup()

    # Insertar el valor de 'profile' en el campo de búsqueda
    search_input = driver.find_element(By.CSS_SELECTOR, 'input.header-search__inp.w-100.h-100')
    search_input.send_keys(profile_link)

    # Dar click en el botón de búsqueda
    search_button = driver.find_element(By.CSS_SELECTOR, 'button.header-search__btn')
    search_button.click()

    try:
        # Verificar si el elemento 'spinner-border' está presente
        spinner_present = EC.presence_of_element_located((By.CSS_SELECTOR, "div.spinner-border"))
        if WebDriverWait(driver, 4).until(spinner_present):
            # Esperar hasta que el elemento 'spinner-border' desaparezca
            WebDriverWait(driver, 4).until_not(spinner_present)
    except UnexpectedAlertPresentException:
        try:
            alert = driver.switch_to.alert
            print(alert.text)  # O manejar el alerta de la forma que quieras
            alert.accept()
            # ... (posiblemente refresca la página u otras operaciones)
        except NoAlertPresentException:
            pass  # Ignora la excepción y no hace nada
    except Exception as e:
        print(f"Otro error ocurrió: {e}")
    sleep(1)

def handle_not_found_popup():
    try:
        # Esperar hasta 10 segundos para que aparezca el popup con el mensaje específico
        popup_element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Profile was not found. Try refreshing the page!']"))
        )
        
        # Si encontramos el popup, damos click en el botón "OK" y recargamos la página
        if popup_element.is_displayed():
            ok_button = driver.find_element(By.XPATH, "//button[text()='OK']")  # Asume que el botón tiene el texto "OK"
            ok_button.click()
            driver.refresh()
    except:
        print("No se encontró el popup de perfil no encontrado o hubo un error al interactuar con él.")

#prefix
prefix = "https://www.instagram.com/"
# Iniciar el navegador Firefox con Selenium
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))  # Cambia 'ruta_del_geckodriver' por la ruta real del geckodriver

try:
    if len(sys.argv) > 1:
        profile = sys.argv[1]
        if profile.startswith(prefix):
            profile = profile[len(prefix):].replace('/','')
        else:
            raise ValueError("Error conversion HTML to user")
        k = 0  
        while k < 2:  # Intentamos cargar el perfil hasta 2 veces
            carga_de_perfil(profile)
            k += 1
        consentimiento(profile)
except:
    print("No Argument Line Command")
    # Cerrar el navegador
sleep(8)
driver.quit()

