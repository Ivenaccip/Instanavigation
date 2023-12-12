from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pyautogui

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
pyautogui.hotkey('ctrl', 'u')
pyautogui.hotkey('ctrl', 's')
sleep(1)
pyautogui.write('google')
sleep(2)
pyautogui.press('enter')
sleep(1)
driver.quit()