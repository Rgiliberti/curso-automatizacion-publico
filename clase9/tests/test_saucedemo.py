"""Pruebas automatizadas de SauceDemo: login, catálogo y carrito.

Cada test recibe su propio navegador (fixture `driver` de conftest.py),
así la falla de uno no afecta a los demás.
"""
from utils import selectores
from utils.helpers import esperar_todos_visibles, esperar_visible, login


# ---------- 1. Login ----------

def test_login_exitoso(driver):
    """Con credenciales válidas se llega al inventario."""
    login(driver)  # incluye la espera explícita de /inventory.html

    assert '/inventory.html' in driver.current_url, f'URL inesperada: {driver.current_url}'
    assert driver.title == 'Swag Labs', f'Título de la pestaña inesperado: {driver.title}'
    titulo = esperar_visible(driver, selectores.TITULO_SECCION).text
    assert titulo == 'Products', f'Título de sección inesperado: {titulo}'


# ---------- 2. Navegación y catálogo ----------

def test_catalogo_inventario(driver):
    """El inventario muestra título, productos y los elementos principales de la interfaz."""
    login(driver)

    # Título de la página
    titulo = esperar_visible(driver, selectores.TITULO_SECCION).text
    assert titulo == 'Products', f'Título de sección inesperado: {titulo}'

    # Productos visibles (al menos uno)
    productos = esperar_todos_visibles(driver, selectores.PRODUCTOS)
    assert len(productos) > 0, 'No hay productos visibles'

    # Elementos importantes de la interfaz: menú, filtro de orden y carrito
    assert driver.find_element(*selectores.BOTON_MENU).is_displayed(), 'No se ve el menú'
    assert driver.find_element(*selectores.FILTRO_ORDEN).is_displayed(), 'No se ve el filtro de orden'
    assert driver.find_element(*selectores.ICONO_CARRITO).is_displayed(), 'No se ve el carrito'

    # Nombre y precio del primer producto (buscados dentro de su tarjeta)
    primero = productos[0]
    nombre = primero.find_element(*selectores.NOMBRE_PRODUCTO).text
    precio = primero.find_element(*selectores.PRECIO_PRODUCTO).text
    assert nombre != '', 'El primer producto no tiene nombre'
    assert precio.startswith('$'), f'Precio con formato inesperado: {precio}'


# ---------- 3. Carrito ----------

def test_agregar_producto_al_carrito(driver):
    """Agregar el primer producto incrementa el contador y el producto aparece en el carrito."""
    login(driver)
    # TODO: agregar el primer producto, verificar contador = 1 y que aparezca en el carrito
    assert ...
