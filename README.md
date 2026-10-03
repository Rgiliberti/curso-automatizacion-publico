# Curso de Automation Testing

Ejercicios resueltos del curso de Automation Testing (Módulo 1: Fundamentos).

> El material del curso (PDFs, consignas) es privado y no se incluye en este repositorio.

| Clase | Tema | Ejercicios |
|---|---|---|
| [Clase 1](clase1/) | Introducción al Automation Testing | `test.py`: verificación del entorno |
| [Clase 2](clase2/) | Fundamentos de Python (parte 1) | Datos personales, 10 números pares, calculadora lineal |
| [Clase 3](clase3/) | Fundamentos de Python (parte 2) y Git | Calculadora modular con funciones y excepciones |
| [Clase 4](clase4/) | Introducción a Pytest | Suite de pruebas, markers y reporte HTML |

## Cómo ejecutar

```bash
# Clases 1 a 3
python clase1/test.py
python clase2/actividad1_datos_personales.py
python clase3/calculadora.py

# Clase 4 (correr desde la carpeta clase4, donde está pytest.ini)
cd clase4
python -m pytest -v
python -m pytest -m smoke
python -m pytest -m exception
python -m pytest --html=report.html --self-contained-html
```

