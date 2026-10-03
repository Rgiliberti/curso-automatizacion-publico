# Clase 5 — Calculadora Modular (HTML + CSS)

Vista estática de la calculadora, preparada para automatizarla más adelante con Selenium.
No tiene JavaScript: la lógica ya está probada con Pytest en la [Clase 4](../clase4/).

## Archivos

| Archivo | Contenido |
|---|---|
| `index.html` | Estructura de la página: encabezado y formulario |
| `estilos.css` | Hoja de estilos externa |
| `selectors.md` | Tabla de selectores para los tests de UI |
| `README.md` | Esta guía |

## Cómo ejecutar

No hace falta servidor: abrí `index.html` en el navegador (doble clic, o Ctrl + O desde el navegador).

## Cómo verificar

1. Abrí DevTools con F12 (o clic derecho → Inspeccionar).
2. En **Elements**, revisá que cada campo, radio y botón tenga un `id` único.
3. En **Console**, probá cada selector de `selectors.md`:

   ```js
   document.querySelector('#num1').style.border = '2px solid red';
   ```

   Si el borde se pinta de rojo, el selector es correcto.
4. Con el modo dispositivo (ícono 📱) comprobá que el formulario se vea bien en móvil.

## Checklist de requisitos

- [x] `h1#titulo-principal` con párrafo introductorio
- [x] `form#form-calculadora` con `action="#"` y `method="post"`
- [x] Inputs `#num1` y `#num2` con `name` igual al `id`
- [x] Radios sumar, restar, multiplicar y dividir con `name="operacion"`
- [x] Botón `#btn-calcular`
- [x] Cada input con su `<label for="...">`
- [x] Bloque centrado, tipografía del sistema, botón `#0275d8` con hover más oscuro, bordes redondeados y sombra
- [x] Sin JavaScript
