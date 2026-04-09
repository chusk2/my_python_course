# 🐍 Guía Teórica: Python Básico

> Conceptos fundamentales: tipos de datos, print, f-strings, comentarios y operadores.

---

## 1. Tipos básicos de datos

Python tiene varios tipos de datos incorporados. Los más básicos son cuatro:

### 1.1 `int` — Números enteros

Representan números sin parte decimal: positivos, negativos o cero.

```python
edad = 25
temperatura = -3
puntuacion = 0
```

Las operaciones matemáticas entre enteros devuelven enteros (salvo la división `/`).

```python
print(10 + 3)   # 13
print(10 // 3)  # 3  (división entera)
print(10 % 3)   # 1  (resto o módulo)
```

---

### 1.2 `float` — Números decimales

Representan números con parte decimal (punto flotante).

```python
precio = 19.99
pi = 3.14159
altura = 1.75
```

> ⚠️ Python usa el **punto** (`.`) como separador decimal, nunca la coma.

```python
print(7 / 2)    # 3.5  (la división siempre da float)
print(0.1 + 0.2)  # 0.30000000000000004 (imprecisión de punto flotante, ¡normal!)
```

---

### 1.3 `str` — Cadenas de texto

Representan texto. Se escriben entre comillas simples `'...'` o dobles `"..."`.

```python
nombre = "Ana"
saludo = 'Hola, mundo'
frase = "Python es 'genial'"
```

Las cadenas son **inmutables**: no se pueden modificar una vez creadas, solo crear nuevas.

Operaciones básicas con strings:

```python
nombre = "Python"
print(len(nombre))         # 6 — longitud
print(nombre.upper())      # PYTHON — mayúsculas
print(nombre.lower())      # python — minúsculas
print(nombre[0])           # P — primer carácter (índice 0)
print(nombre[-1])          # n — último carácter
print("Py" + "thon")       # Python — concatenación
print("ja" * 3)            # jajaja — repetición
```

---

### 1.4 `bool` — Valores booleanos

Solo tienen dos posibles valores: `True` o `False` (con mayúscula inicial).

```python
tiene_trabajo = True
es_mayor_de_edad = False
```

Los booleanos son el resultado natural de comparaciones y condiciones:

```python
print(5 > 3)    # True
print(10 == 9)  # False
print(type(True))  # <class 'bool'>
```

> 💡 En Python, `True` equivale a `1` y `False` a `0` en contextos numéricos.

---

### 1.5 La función `type()`

Permite conocer el tipo de cualquier valor o variable:

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("hola"))   # <class 'str'>
print(type(True))     # <class 'bool'>
```

---

## 2. La función `print()`

`print()` muestra información en la consola. Es la herramienta más básica de salida en Python.

### Uso básico

```python
print("Hola, mundo")
print(42)
print(3.14)
print(True)
```

### Múltiples argumentos

Se pueden pasar varios valores separados por comas. Por defecto, `print()` los separa con un espacio:

```python
print("Mi nombre es", "Ana", "y tengo", 25, "años")
# Mi nombre es Ana y tengo 25 años
```

### Parámetros especiales

```python
# sep: cambia el separador entre argumentos
print("uno", "dos", "tres", sep="-")   # uno-dos-tres

# end: cambia el carácter final (por defecto es \n, salto de línea)
print("Hola", end=" ")
print("Mundo")   # Hola Mundo (en la misma línea)
```

---

## 3. F-strings (cadenas formateadas)

Las **f-strings** (introducidas en Python 3.6) permiten insertar variables y expresiones directamente dentro de una cadena de texto, de forma limpia y legible.

### Sintaxis

Se escribe una `f` (o `F`) antes de las comillas, y las expresiones van entre llaves `{}`:

```python
nombre = "Carlos"
edad = 30

print(f"Me llamo {nombre} y tengo {edad} años.")
# Me llamo Carlos y tengo 30 años.
```

### Expresiones dentro de llaves

Puedes poner cualquier expresión Python válida:

```python
a = 10
b = 3

print(f"La suma es {a + b}")          # La suma es 13
print(f"El doble de a es {a * 2}")    # El doble de a es 20
print(f"¿Es mayor? {a > b}")          # ¿Es mayor? True
```

### Formato de números

```python
precio = 9.5
print(f"El precio es {precio:.2f} €")   # El precio es 9.50 €
```

> 💡 `:.2f` indica: formato decimal con 2 cifras tras el punto.

---

## 4. Comentarios

Los comentarios son anotaciones en el código que **Python ignora completamente**. Sirven para explicar el código, dejar notas o desactivar líneas temporalmente.

### Comentarios de una línea

Se inician con `#`:

```python
# Esto es un comentario completo
edad = 25  # Esto es un comentario al final de una línea de código
```

### Comentarios de múltiples líneas

Python no tiene un operador oficial para comentarios multilínea, pero se usan cadenas de texto entre triple comilla (que Python evalúa pero no usa):

```python
"""
Este es un bloque de comentario
que ocupa varias líneas.
Se usa frecuentemente para documentar funciones.
"""
```

### Buenas prácticas con comentarios

- Comenta el **por qué**, no el **qué** (el código ya dice qué hace).
- Mantén los comentarios actualizados con el código.
- No comentes lo obvio: `x = 5  # asigna 5 a x` no aporta valor.

```python
# ✅ Buen comentario
descuento = precio * 0.1  # Aplicamos el 10% de descuento por ser cliente VIP

# ❌ Comentario innecesario
x = x + 1  # suma 1 a x
```

---

## 5. Operadores

### 5.1 Operadores aritméticos

Realizan operaciones matemáticas:

| Operador | Nombre            | Ejemplo   | Resultado |
|----------|-------------------|-----------|-----------|
| `+`      | Suma              | `5 + 3`   | `8`       |
| `-`      | Resta             | `5 - 3`   | `2`       |
| `*`      | Multiplicación    | `5 * 3`   | `15`      |
| `/`      | División          | `5 / 3`   | `1.666...`|
| `//`     | División entera   | `5 // 3`  | `1`       |
| `%`      | Módulo (resto)    | `5 % 3`   | `2`       |
| `**`     | Potencia          | `5 ** 3`  | `125`     |

```python
print(2 ** 10)   # 1024
print(17 % 5)    # 2
print(7 // 2)    # 3
```

---

### 5.2 Operadores de comparación

Comparan dos valores y devuelven `True` o `False`:

| Operador | Significado       | Ejemplo    | Resultado |
|----------|-------------------|------------|-----------|
| `==`     | Igual a           | `5 == 5`   | `True`    |
| `!=`     | Distinto de       | `5 != 3`   | `True`    |
| `>`      | Mayor que         | `5 > 3`    | `True`    |
| `<`      | Menor que         | `5 < 3`    | `False`   |
| `>=`     | Mayor o igual que | `5 >= 5`   | `True`    |
| `<=`     | Menor o igual que | `3 <= 5`   | `True`    |

> ⚠️ No confundir `=` (asignación) con `==` (comparación de igualdad).

```python
x = 10
print(x == 10)   # True
print(x != 5)    # True
print(x > 20)    # False
```

---

### 5.3 Operadores lógicos

Combinan o modifican condiciones booleanas:

#### `and` — Y lógico

Devuelve `True` solo si **ambas** condiciones son verdaderas.

```python
edad = 20
tiene_carnet = True

puede_conducir = edad >= 18 and tiene_carnet
print(puede_conducir)  # True
```

Tabla de verdad de `and`:

| A       | B       | A and B |
|---------|---------|---------|
| True    | True    | True    |
| True    | False   | False   |
| False   | True    | False   |
| False   | False   | False   |

---

#### `or` — O lógico

Devuelve `True` si **al menos una** condición es verdadera.

```python
es_estudiante = False
es_jubilado = True

tiene_descuento = es_estudiante or es_jubilado
print(tiene_descuento)  # True
```

Tabla de verdad de `or`:

| A       | B       | A or B  |
|---------|---------|---------|
| True    | True    | True    |
| True    | False   | True    |
| False   | True    | True    |
| False   | False   | False   |

---

#### `not` — Negación lógica

Invierte el valor booleano.

```python
llueve = False
print(not llueve)   # True

acceso_denegado = True
print(not acceso_denegado)  # False
```

---

### 5.4 Combinando operadores lógicos

Python evalúa los operadores lógicos en este orden de precedencia: primero `not`, luego `and`, y finalmente `or`. Se pueden usar paréntesis para controlar el orden:

```python
a = 5
b = 10
c = 15

# ¿b está entre a y c?
resultado = a < b and b < c
print(resultado)  # True

# Forma compacta (Python lo permite)
print(a < b < c)  # True

# Combinando and y or
es_adulto = True
tiene_entrada = False
es_vip = True

puede_entrar = es_adulto and (tiene_entrada or es_vip)
print(puede_entrar)  # True
```

---

## 6. Resumen visual

```
TIPOS DE DATOS
┌──────────┬──────────────────────────────┬──────────────────────┐
│  Tipo    │  Descripción                 │  Ejemplo             │
├──────────┼──────────────────────────────┼──────────────────────┤
│  int     │  Número entero               │  42, -7, 0           │
│  float   │  Número decimal              │  3.14, -0.5          │
│  str     │  Cadena de texto             │  "hola", 'mundo'     │
│  bool    │  Valor lógico                │  True, False         │
└──────────┴──────────────────────────────┴──────────────────────┘

OPERADORES
┌──────────────┬────────────────────────────────────────────────┐
│  Tipo        │  Operadores                                    │
├──────────────┼────────────────────────────────────────────────┤
│  Aritméticos │  + - * / // % **                              │
│  Comparación │  == != > < >= <=                              │
│  Lógicos     │  and  or  not                                 │
└──────────────┴────────────────────────────────────────────────┘
```

---

*Guía preparada para acompañar los ejercicios Python básico (`ejercicios_tipos_operadores.pdf`).*
