# Pre-entrega · Automation Testing — Romina Giliberti

Automatización de login, navegación del catálogo y carrito de compras en [SauceDemo](https://www.saucedemo.com/)
con Python, Pytest y Selenium WebDriver.

## Propósito

Validar de forma automática los flujos esenciales de la tienda demo SauceDemo:

1. **Login**: con credenciales válidas se llega al inventario.
2. **Navegación y catálogo**: la página de inventario muestra el título correcto, productos visibles y los
   elementos principales de la interfaz (menú, filtro de orden, carrito).
3. **Carrito**: al agregar un producto el contador se incrementa y el producto aparece en el carrito.

## Tecnologías

| Herramienta | Uso |
|---|---|
| Python 3 | Lenguaje de programación |
| Pytest | Framework de testing (fixtures y hooks) |
| Selenium WebDriver 4 | Automatización del navegador Chrome |
| pytest-html | Reporte HTML de la ejecución |
| Git y GitHub | Control de versiones |

## Estructura del proyecto

```text
clase9/
├── tests/
│   └── test_saucedemo.py   # Casos de prueba: login, catálogo y carrito
├── utils/
│   ├── helpers.py          # Driver, esperas explícitas y login
│   └── selectores.py       # Selectores de la página (ID, NAME, CSS)
├── reports/
│   ├── reporte.html        # Reporte HTML de la última ejecución
│   ├── ejecucion.log       # Log de la última ejecución
│   └── capturas/           # Capturas automáticas de los tests que fallan
├── conftest.py             # Fixture del navegador y captura de pantalla ante fallos
├── pytest.ini              # Configuración de pytest (reporte HTML y logs)
└── requirements.txt        # Dependencias
```

## Instalación

Requisitos: Python 3.8 o superior y Google Chrome. No hace falta descargar ChromeDriver:
Selenium Manager baja automáticamente el que corresponde a la versión de Chrome instalada.

```bash
git clone https://github.com/Rgiliberti/curso-automatizacion-publico.git
cd curso-automatizacion-publico/clase9
pip install -r requirements.txt
```

## Cómo ejecutar las pruebas

Desde la carpeta `clase9/`:

```bash
pytest
```

`pytest.ini` ya agrega `-v --html=reports/reporte.html --self-contained-html`, así que el comando anterior equivale a:

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html --self-contained-html
```

Otras formas útiles:

```bash
pytest -k carrito          # solo los tests cuyo nombre contiene "carrito"
pytest -k login            # solo el test de login
```

Para correr sin abrir la ventana de Chrome (modo headless):

```powershell
# PowerShell
$env:HEADLESS = "1"; pytest
```

```bash
# Git Bash / Linux / macOS
HEADLESS=1 pytest
```

## Casos de prueba

| Test | Qué valida |
|---|---|
| `test_login_exitoso` | URL `/inventory.html`, título de la pestaña "Swag Labs" y título de sección "Products" |
| `test_catalogo_inventario` | Título "Products", al menos un producto visible, menú, filtro de orden y carrito visibles, nombre y precio del primer producto |
| `test_agregar_producto_al_carrito` | Carrito vacío al inicio, contador = 1 después de agregar y producto listado en `/cart.html` |

## Decisiones de diseño

- **Tests independientes**: la fixture `driver` abre un navegador nuevo para cada test y lo cierra al terminar,
  aunque el test falle. Ningún test depende del estado que deja otro.
- **Solo esperas explícitas** (`WebDriverWait` + `expected_conditions`): cada paso espera exactamente lo que necesita
  (visibilidad, que sea clickeable, cambio de URL). No se usa `implicitly_wait` para no mezclar ambos tipos de espera.
- **Selectores centralizados** en `utils/selectores.py`, siguiendo la regla ID → NAME → CSS → XPath.
  Si la página cambia, se corrige en un solo lugar.

## Evidencias

- **Reporte HTML**: `reports/reporte.html` (autocontenido; se abre con doble clic en el navegador).
- **Logs de ejecución**: `reports/ejecucion.log`, con cada paso de cada test; también se ven dentro del reporte HTML.
- **Capturas ante fallos**: si un test falla, `conftest.py` guarda una captura en `reports/capturas/<test>_<fecha>.png`
  y la adjunta en el reporte HTML junto al error.

## Resultado de la última ejecución

```text
tests/test_saucedemo.py::test_login_exitoso PASSED
tests/test_saucedemo.py::test_catalogo_inventario PASSED
tests/test_saucedemo.py::test_agregar_producto_al_carrito PASSED

3 passed
```
