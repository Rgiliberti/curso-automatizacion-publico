import pytest
from calculator import sumar, restar, multiplicar, dividir


# ---------- Fixtures ----------

@pytest.fixture
def numeros_enteros():
    return 20, 5


@pytest.fixture
def numeros_decimales():
    return 0.1, 0.2


# ---------- Sumar ----------

@pytest.mark.smoke
def test_sumar_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert sumar(a, b) == 25


@pytest.mark.smoke
def test_sumar_decimales(numeros_decimales):
    a, b = numeros_decimales
    assert sumar(a, b) == pytest.approx(0.3)


@pytest.mark.smoke
@pytest.mark.parametrize("a, b, esperado", [
    (1, 2, 3),
    (-1, -1, -2),
    (2.5, 0.5, 3.0),
    (0, 0, 0),
])
def test_sumar_varios(a, b, esperado):
    assert sumar(a, b) == esperado


@pytest.mark.smoke
@pytest.mark.exception
def test_sumar_texto_y_numero():
    with pytest.raises(TypeError):
        sumar("a", 1)


# ---------- Restar ----------

def test_restar_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert restar(a, b) == 15


def test_restar_decimales(numeros_decimales):
    a, b = numeros_decimales
    assert restar(b, a) == pytest.approx(0.1)


@pytest.mark.parametrize("a, b, esperado", [
    (5, 3, 2),
    (3, 5, -2),
    (-1, -1, 0),
    (2.5, 0.5, 2.0),
])
def test_restar_varios(a, b, esperado):
    assert restar(a, b) == esperado


@pytest.mark.exception
def test_restar_texto_y_numero():
    with pytest.raises(TypeError):
        restar("a", 1)


# ---------- Multiplicar ----------

def test_multiplicar_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == 100


def test_multiplicar_decimales(numeros_decimales):
    a, b = numeros_decimales
    assert multiplicar(a, b) == pytest.approx(0.02)


@pytest.mark.exception
def test_multiplicar_dos_textos():
    with pytest.raises(TypeError):
        multiplicar("a", "b")


# ---------- Dividir ----------

def test_dividir_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 4


def test_dividir_decimales(numeros_decimales):
    a, b = numeros_decimales
    assert dividir(a, b) == pytest.approx(0.5)


@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ValueError) as excinfo:
        dividir(1, 0)
    assert "No se puede dividir por cero" in str(excinfo.value)
