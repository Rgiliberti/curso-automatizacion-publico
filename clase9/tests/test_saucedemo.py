"""Pruebas automatizadas de SauceDemo: login, catálogo y carrito.

Cada test recibe su propio navegador (fixture `driver` de conftest.py),
así la falla de uno no afecta a los demás.
"""

from utils.helpers import login


# ---------- 1. Login ----------

def test_login_exitoso(driver):
    """Con credenciales válidas se llega al inventario."""
    login(driver)
    # TODO: validar URL /inventory.html, título "Swag Labs" y sección "Products"
    assert ...


# ---------- 2. Navegación y catálogo ----------

def test_catalogo_inventario(driver):
    """El inventario muestra título, productos y los elementos principales de la interfaz."""
    login(driver)
    # TODO: título "Products", al menos un producto visible, menú y filtro visibles,
    #       nombre y precio del primer producto
    assert ...


# ---------- 3. Carrito ----------

def test_agregar_producto_al_carrito(driver):
    """Agregar el primer producto incrementa el contador y el producto aparece en el carrito."""
    login(driver)
    # TODO: agregar el primer producto, verificar contador = 1 y que aparezca en el carrito
    assert ...
