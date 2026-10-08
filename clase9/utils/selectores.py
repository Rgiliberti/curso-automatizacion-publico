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

# Página de inventario
TITULO_SECCION = (By.CSS_SELECTOR, '.title')
PRODUCTOS = (By.CSS_SELECTOR, '.inventory_item')
NOMBRE_PRODUCTO = (By.CSS_SELECTOR, '.inventory_item_name')
PRECIO_PRODUCTO = (By.CSS_SELECTOR, '.inventory_item_price')
BOTON_AGREGAR = (By.CSS_SELECTOR, 'button[id^="add-to-cart"]')
BOTON_MENU = (By.ID, 'react-burger-menu-btn')
FILTRO_ORDEN = (By.CSS_SELECTOR, 'select.product_sort_container')

# Carrito (ícono del encabezado y página del carrito)
ICONO_CARRITO = (By.CSS_SELECTOR, '.shopping_cart_link')
CONTADOR_CARRITO = (By.CSS_SELECTOR, '.shopping_cart_badge')
NOMBRES_EN_CARRITO = (By.CSS_SELECTOR, '.cart_item .inventory_item_name')
