"""Configuración compartida por todos los tests (pytest carga este archivo solo).

- Fixture `driver`: un navegador nuevo por test, así los tests son independientes.
"""
import logging

import pytest

from utils.helpers import crear_driver

logger = logging.getLogger('saucedemo')


@pytest.fixture
def driver():
    """Abre Chrome antes del test y lo cierra después, pase lo que pase."""
    navegador = crear_driver()
    logger.info('Navegador abierto')
    yield navegador
    navegador.quit()
    logger.info('Navegador cerrado')


# TODO: captura de pantalla automática cuando un test falla
