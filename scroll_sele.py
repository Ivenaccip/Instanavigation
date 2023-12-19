from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Inicializar el navegador
driver = webdriver.Chrome()  # O el navegador que estés utilizando

# Abrir la página web
driver.get("https://www.bol.com/nl/nl/")

sleep(5)

# Definir la cantidad de scrolls que deseas realizar
cantidad_scrolls = 3

for _ in range(cantidad_scrolls):
    # Hacer scroll hacia abajo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Esperar a que la página se cargue después del scroll
    # Puedes ajustar este tiempo según la velocidad de carga de tu página
    driver.implicitly_wait(3)  # Espera 5 segundos
    
# Realizar otras operaciones después de hacer scroll, si es necesario

# Cerrar el navegador al finalizar
driver.quit()
