# Selectores de la Calculadora Modular

Selectores CSS que se van a usar en los tests de UI con Selenium.
Todos fueron verificados en la consola de DevTools y apuntan a un único elemento.

| Elemento | Atributo usado | Selector CSS |
|---|---|---|
| Título principal | id | `#titulo-principal` |
| Párrafo introductorio | id | `#descripcion` |
| Formulario | id | `#form-calculadora` |
| Campo Número 1 | id | `#num1` |
| Campo Número 1 (alternativo) | name | `input[name="num1"]` |
| Campo Número 2 | id | `#num2` |
| Campo Número 2 (alternativo) | name | `input[name="num2"]` |
| Grupo de operaciones | id | `#grupo-operacion` |
| Radio Sumar | id | `#op-sumar` |
| Radio Restar | id | `#op-restar` |
| Radio Multiplicar | id | `#op-multiplicar` |
| Radio Dividir | id | `#op-dividir` |
| Radio Dividir (alternativo) | name + value | `input[name="operacion"][value="dividir"]` |
| Todas las operaciones | name | `input[name="operacion"]` (devuelve 4 elementos) |
| Operación seleccionada | name + estado | `input[name="operacion"]:checked` |
| Botón Calcular | id | `#btn-calcular` |
| Botón Calcular (alternativo) | class | `.btn.btn-primario` |

## Criterio

- Se prioriza `id` porque es único y no depende del diseño.
- Los selectores por `name` sirven de respaldo y coinciden con lo que recibe el backend.
- No se usan rutas largas ni `nth-child`, que se rompen ante cambios de estructura.

## Cómo verificar un selector

En DevTools → Console:

```js
document.querySelector('#num1').style.border = '2px solid red';
document.querySelectorAll('input[name="operacion"]').length; // 4
```

Si el elemento se marca en rojo, el selector es correcto. Si `querySelector` devuelve `null`, no encuentra nada.
