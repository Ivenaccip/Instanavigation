import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
# Code extraction
import pyautogui
import subprocess
#code Linea Argument
import sys
from datetime import datetime
from sqlalchemy import create_engine
import mysql.connector

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

    scroll_amount = 600  # Cantidad de píxeles para desplazarse hacia abajo
    try:
        driver.execute_script(f"window.scrollTo(0, {scroll_amount});")
        sleep(1)  # Esperar un poco para que la página reaccione al desplazamiento
    except Exception as e:
        print("Error with scroll:", e)

    try:
    # Esperar y encontrar todos los elementos div con las clases especificadas
        current_date = datetime.now().strftime("%d-%m-%Y")
        elements = WebDriverWait(driver, 8).until(
        EC.presence_of_all_elements_located((By.XPATH, '//img[@class = "stories__img"]'))
    )
        for index, element in enumerate(elements, start=1):  # Iterar a través de cada elemento encontrado
            sleep(5)
            driver.execute_script("arguments[0].click();", element)  # Hacer clic utilizando JavaScript
            print("Clicked on an element")
            pyautogui.moveTo(480, 607)
            pyautogui.rightClick()
            pyautogui.press('down')
            pyautogui.press('down')
            
            # Presionar 'enter' para abrir el diálogo de guardar
            pyautogui.press('enter')

            # Esperar a que el diálogo de guardar se abra (ajusta este tiempo según sea necesario)
            sleep(2)

            filename = f"{datetime.now().strftime('%d-%m-%Y')}_{index}_{username}"

            # Escribir el nombre del archivo
            pyautogui.write(f'{filename}')
            
            # Presionar 'enter' para guardar la imagen
            pyautogui.press('enter')
            
            # Esperar a que la imagen se guarde antes de continuar
            sleep(1)
                # SQL para insertar datos
            insert_query = """
            INSERT INTO id_obj_download (Object_ID, Type, Link, Extract_text, Fecha, Profile)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            insert_data = (filename, 'Ig-Post', str(index), None, datetime.now().date(), username)

            # Ejecutar la consulta
            cursor.execute(insert_query, insert_data)

            # Confirmar la transacción
            conn.commit()
    except Exception as e:
        print("Xpath didn't find:", e)

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
# Selenium driver and configurations
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
  "download.default_directory": "/home/kroonadmin/Documents/new/Instanavigation",  # Especifica tu directorio de descargas aquí.
  "download.prompt_for_download": False,  # Desactiva el diálogo de confirmación de descarga.
  "download.directory_upgrade": True,  # Permite que Chrome cree el directorio si no existe.
  "safebrowsing.enabled": True,  # Mantiene activado el SafeBrowsing de Chrome.
  "profile.default_content_setting_values.automatic_downloads": 1  # Permitir descargas automáticas para múltiples archivos sin confirmación
})
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))  # Cambia 'ruta_del_geckodriver' por la ruta real del geckodriver

conn = mysql.connector.connect(
#Conexion SQL
    host = 'localhost',
    user = 'office',
    password = 'Kroon111',
    database = 'alpha_test'
)

cursor = conn.cursor()

try:
    if len(sys.argv) > 1:
        profile = sys.argv[1]
        if profile.startswith(prefix):
            profile = profile[len(prefix):].replace('/','')
        else:
            raise ValueError("Error conversion HTML to user")
        consentimiento(profile)
except:
    print("No Argument Line Command")
    # Cerrar el navegador
sleep(8)
driver.quit()

cursor.close()
conn.close()