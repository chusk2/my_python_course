# 🏋️ Ejercicios: Python Básico

> Tipos de datos · print · f-strings · comentarios · operadores aritméticos, de comparación y lógicos

**Niveles:** 🟢 Básico (1–10) · 🟡 Medio (11–16) · 🔴 Avanzado (17–20)

---

## 🟢 Ejercicios Básicos

---

### Ejercicio 1 — Tipos de datos y `type()`

Crea cuatro variables, una de cada tipo básico (`int`, `float`, `str`, `bool`), con valores que representen información sobre una persona ficticia. Luego muestra el valor y el tipo de cada variable con `print()`.

**Ejemplo de salida esperada:**
```
28 <class 'int'>
1.75 <class 'float'>
Laura <class 'str'>
True <class 'bool'>
```

<details>
<summary>💡 Pista</summary>

Usa la función `type()` dentro del `print()`. Puedes pasar dos argumentos separados por coma.

</details>

<details>
<summary>✅ Solución</summary>

```python
# Variables con información de una persona
edad = 28           # int: número entero
altura = 1.75       # float: número decimal
nombre = "Laura"    # str: cadena de texto
activo = True       # bool: valor lógico

# Mostramos el valor y el tipo de cada una
print(edad, type(edad))
print(altura, type(altura))
print(nombre, type(nombre))
print(activo, type(activo))
```

</details>

---

## 📊 Resumen de ejercicios

| Nº  | Nivel   | Concepto principal                         |
|-----|---------|---------------------------------------------|
| 1   | 🟢      | Tipos de datos + `type()`                  |
| 2   | 🟢      | F-strings básicas                           |
| 3   | 🟢      | Operadores aritméticos                      |
| 4   | 🟢      | Comentarios                                 |
| 5   | 🟢      | Operadores de comparación                   |
| 6   | 🟢      | Operador `not`                              |
| 7   | 🟢      | Operador `and`                              |
| 8   | 🟢      | Operador `or`                               |
| 9   | 🟢      | `print()` con `sep` y `end`                |
| 10  | 🟢      | Potencia y módulo                           |
| 11  | 🟡      | F-strings con formato decimal `:.2f`        |
| 12  | 🟡      | `and` + `or` combinados                     |
| 13  | 🟡      | Conversión de tipos + comparación           |
| 14  | 🟡      | Métodos de string + f-strings               |
| 15  | 🟡      | Divisibilidad con `%` y `and`              |
| 16  | 🟡      | Fórmula matemática + rango con `and`        |
| 17  | 🔴      | Validación de datos con lógica compuesta    |
| 18  | 🔴      | F-strings avanzadas con alineación          |
| 19  | 🔴      | Lógica compleja: `and`, `or`, `not`         |
| 20  | 🔴      | Problema real con condiciones compuestas    |

---

*¡Completa los ejercicios en orden y consulta las pistas antes de ver la solución!*
