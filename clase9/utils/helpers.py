"""Funciones auxiliares para las pruebas de SauceDemo.

Lo que se repite entre tests vive acá: crear el navegador, esperar elementos
y hacer login. Así los tests quedan cortos y legibles.
"""
import os

from selenium import webdriver

URL = 'https://www.saucedemo.com/'
USUARIO = 'standard_user'
CLAVE = 'secret_sauce'


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


# TODO: funciones de espera explícita (elemento visible, clickeable, cambio de URL)


def login(driver):
    """Abre SauceDemo, ingresa con el usuario válido y espera a llegar al inventario."""
    ...  # TODO: completar usuario y clave, clic en Login y esperar /inventory.html
