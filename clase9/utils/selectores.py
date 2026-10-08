"""Selectores de SauceDemo usados por los tests.

Cada selector es una tupla (estrategia, valor) lista para usar con
driver.find_element(*SELECTOR) o con las esperas de utils/helpers.py.
Si la página cambia, se corrige acá una sola vez.
Orden de preferencia (regla de oro): ID -> NAME -> CSS corto -> XPath.
"""
from selenium.webdriver.common.by import By

# Página de login
CAMPO_USUARIO = (By.ID, 'user-name')
CAMPO_CLAVE = (By.NAME, 'password')
BOTON_LOGIN = (By.CSS_SELECTOR, 'input[type="submit"]')

# TODO: selectores de la página de inventario y del carrito
