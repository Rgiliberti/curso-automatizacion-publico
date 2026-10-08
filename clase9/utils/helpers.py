"""Funciones auxiliares para las pruebas de SauceDemo.

Lo que se repite entre tests vive acá: crear el navegador, esperar elementos
y hacer login. Así los tests quedan cortos y legibles.
"""
import os

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import selectores

URL = 'https://www.saucedemo.com/'
USUARIO = 'standard_user'
CLAVE = 'secret_sauce'
TIEMPO_MAXIMO = 10  # segundos que aguanta cada espera explícita


def crear_driver():
    """Abre Chrome listo para las pruebas y lo devuelve.

    Con la variable de entorno HEADLESS=1 corre sin abrir la ventana.
    No configura implicitly_wait: el proyecto usa solo esperas explícitas.
    """
    opciones = webdriver.ChromeOptions()
    opciones.add_argument('--window-size=1366,900')
    # Evita el aviso de "contraseña filtrada" de Chrome, que tapa la página
    opciones.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False,
        'profile.password_manager_leak_detection': False,
    })
    if os.environ.get('HEADLESS') == '1':
        opciones.add_argument('--headless=new')
    return webdriver.Chrome(options=opciones)


def esperar_visible(driver, selector, tiempo=TIEMPO_MAXIMO):
    """Espera a que el elemento se vea en pantalla y lo devuelve."""
    return WebDriverWait(driver, tiempo).until(
        EC.visibility_of_element_located(selector), f'No se vio el elemento {selector} en {tiempo} s')


def esperar_todos_visibles(driver, selector, tiempo=TIEMPO_MAXIMO):
    """Espera a que se vean los elementos que coinciden con el selector y devuelve la lista."""
    return WebDriverWait(driver, tiempo).until(
        EC.visibility_of_all_elements_located(selector), f'No se vieron elementos {selector} en {tiempo} s')


def esperar_clickeable(driver, selector, tiempo=TIEMPO_MAXIMO):
    """Espera a que el elemento se pueda clickear y lo devuelve."""
    return WebDriverWait(driver, tiempo).until(
        EC.element_to_be_clickable(selector), f'El elemento {selector} no se pudo clickear en {tiempo} s')


def esperar_url(driver, fragmento, tiempo=TIEMPO_MAXIMO):
    """Espera a que la URL actual contenga el fragmento indicado."""
    WebDriverWait(driver, tiempo).until(
        EC.url_contains(fragmento), f'La URL no llegó a contener {fragmento} en {tiempo} s')


def escribir(driver, selector, texto):
    """Espera el input, borra lo que tenga y escribe el texto."""
    campo = esperar_visible(driver, selector)
    campo.clear()
    campo.send_keys(texto)


def login(driver):
    """Abre SauceDemo, ingresa con el usuario válido y espera a llegar al inventario."""
    driver.get(URL)
    escribir(driver, selectores.CAMPO_USUARIO, USUARIO)
    escribir(driver, selectores.CAMPO_CLAVE, CLAVE)
    esperar_clickeable(driver, selectores.BOTON_LOGIN).click()
    # Espera explícita: después del clic, la URL tiene que cambiar a /inventory.html
    esperar_url(driver, '/inventory.html')
