"""Configuración compartida por todos los tests (pytest carga este archivo solo).

- Fixture `driver`: un navegador nuevo por test, así los tests son independientes.
- Si un test falla: captura de pantalla en reports/capturas/ y adjunta al reporte HTML.
"""
import logging
from datetime import datetime
from pathlib import Path

import pytest

from utils.helpers import crear_driver

CARPETA_PROYECTO = Path(__file__).resolve().parent
CARPETA_CAPTURAS = CARPETA_PROYECTO / 'reports' / 'capturas'

logger = logging.getLogger('saucedemo')


@pytest.fixture
def driver():
    """Abre Chrome antes del test y lo cierra después, pase lo que pase."""
    navegador = crear_driver()
    logger.info('Navegador abierto')
    yield navegador
    navegador.quit()
    logger.info('Navegador cerrado')


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    """Se ejecuta al terminar cada fase de un test; si falló, guarda la evidencia."""
    reporte = yield
    navegador = item.funcargs.get('driver')
    # Solo nos interesa la fase 'call' (el cuerpo del test) y solo si falló
    if reporte.when == 'call' and reporte.failed and navegador is not None:
        CARPETA_CAPTURAS.mkdir(parents=True, exist_ok=True)
        momento = datetime.now().strftime('%Y%m%d_%H%M%S')
        archivo = CARPETA_CAPTURAS / f'{item.name}_{momento}.png'
        navegador.save_screenshot(str(archivo))
        # En el log va la ruta relativa al proyecto (sin datos de la máquina local)
        logger.error('Falló %s. Captura guardada en %s', item.name, archivo.relative_to(CARPETA_PROYECTO))

        # Adjuntar la misma captura dentro del reporte HTML de pytest-html
        pytest_html = item.config.pluginmanager.getplugin('html')
        if pytest_html is not None:
            extras = getattr(reporte, 'extras', [])
            extras.append(pytest_html.extras.image(navegador.get_screenshot_as_base64()))
            reporte.extras = extras
    return reporte
