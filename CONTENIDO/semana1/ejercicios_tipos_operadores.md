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

### Ejercicio 2 — Tu primera f-string

Declara tres variables: tu nombre (str), tu edad (int) y tu altura en metros (float). Usa una f-string para imprimir una presentación completa en una sola línea.

**Ejemplo de salida esperada:**
```
Hola, me llamo Marcos, tengo 22 años y mido 1.80 metros.
```

<details>
<summary>💡 Pista</summary>

Recuerda que la f-string empieza con `f"..."` y las variables van entre llaves `{variable}`.

</details>

<details>
<summary>✅ Solución</summary>

```python
# Datos personales
nombre = "Marcos"
edad = 22
altura = 1.80

# F-string para presentación completa
print(f"Hola, me llamo {nombre}, tengo {edad} años y mido {altura} metros.")
```

</details>

---

### Ejercicio 3 — Operadores aritméticos básicos

Declara dos variables numéricas enteras `a = 15` y `b = 4`. Calcula e imprime: la suma, la resta, la multiplicación, la división exacta, la división entera y el resto.

**Ejemplo de salida esperada:**
```
Suma: 19
Resta: 11
Multiplicación: 60
División: 3.75
División entera: 3
Resto: 3
```

<details>
<summary>💡 Pista</summary>

Recuerda: `/` es división normal (da float), `//` es división entera, `%` es el resto.

</details>

<details>
<summary>✅ Solución</summary>

```python
a = 15
b = 4

# Operaciones aritméticas básicas
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Resto:", a % b)
```

</details>

---

### Ejercicio 4 — Comentarios explicativos

Escribe un programa que calcule el área de un rectángulo (base × altura). El código debe incluir al menos tres comentarios: uno explicando qué hace el programa, uno por cada variable importante y uno describiendo la operación.

<details>
<summary>💡 Pista</summary>

Los comentarios van precedidos de `#`. Pueden estar en su propia línea o al final de una línea de código.

</details>

<details>
<summary>✅ Solución</summary>

```python
# Programa para calcular el área de un rectángulo

base = 8    # Longitud de la base en metros
altura = 5  # Longitud de la altura en metros

# Calculamos el área multiplicando base por altura
area = base * altura

print(f"El área del rectángulo es {area} m²")
```

</details>

---

### Ejercicio 5 — Comparaciones simples

Declara dos variables numéricas y muestra por pantalla el resultado (True o False) de las seis comparaciones posibles: `==`, `!=`, `>`, `<`, `>=`, `<=`.

**Ejemplo de salida esperada (con x=7, y=10):**
```
¿Son iguales? False
¿Son distintos? True
¿x mayor que y? False
¿x menor que y? True
¿x mayor o igual? False
¿x menor o igual? True
```

<details>
<summary>💡 Pista</summary>

Puedes usar f-strings para hacer el código más limpio.

</details>

<details>
<summary>✅ Solución</summary>

```python
x = 7
y = 10

# Comparamos los dos valores con cada operador
print(f"¿Son iguales? {x == y}")
print(f"¿Son distintos? {x != y}")
print(f"¿x mayor que y? {x > y}")
print(f"¿x menor que y? {x < y}")
print(f"¿x mayor o igual? {x >= y}")
print(f"¿x menor o igual? {x <= y}")
```

</details>

---

### Ejercicio 6 — Operador `not`

Crea una variable booleana `luz_encendida = False`. Imprime su valor original y luego su valor negado con `not`. Añade un comentario explicando qué hace `not`.

<details>
<summary>✅ Solución</summary>

```python
luz_encendida = False

# not invierte el valor booleano: True pasa a False y viceversa
print(f"¿Luz encendida? {luz_encendida}")
print(f"¿Luz apagada? {not luz_encendida}")
```

</details>

---

### Ejercicio 7 — Operador `and`

Crea dos variables booleanas: `tiene_dni = True` y `es_mayor_de_edad = True`. Usa `and` para determinar si una persona puede votar (necesita ambas condiciones). Prueba también con `es_mayor_de_edad = False` y observa el resultado.

<details>
<summary>✅ Solución</summary>

```python
tiene_dni = True
es_mayor_de_edad = True  # Cambia a False para ver el otro resultado

# Para votar se necesitan las DOS condiciones a la vez
puede_votar = tiene_dni and es_mayor_de_edad

print(f"¿Tiene DNI? {tiene_dni}")
print(f"¿Es mayor de edad? {es_mayor_de_edad}")
print(f"¿Puede votar? {puede_votar}")
```

</details>

---

### Ejercicio 8 — Operador `or`

Una tienda ofrece descuento a clientes que sean estudiantes o jubilados. Crea dos variables booleanas y usa `or` para determinar si el cliente tiene derecho al descuento.

<details>
<summary>✅ Solución</summary>

```python
es_estudiante = False
es_jubilado = True

# Basta con que se cumpla UNA de las dos condiciones
tiene_descuento = es_estudiante or es_jubilado

print(f"¿Es estudiante? {es_estudiante}")
print(f"¿Es jubilado? {es_jubilado}")
print(f"¿Tiene descuento? {tiene_descuento}")
```

</details>

---

### Ejercicio 9 — `print()` con `sep` y `end`

Sin usar f-strings, imprime con un solo `print()` los números 1, 2 y 3 separados por guiones (`1-2-3`). Luego imprime dos mensajes distintos en la misma línea usando el parámetro `end`.

<details>
<summary>💡 Pista</summary>

Usa `sep="-"` para cambiar el separador y `end=" "` para evitar el salto de línea.

</details>

<details>
<summary>✅ Solución</summary>

```python
# Separador personalizado entre los argumentos
print(1, 2, 3, sep="-")

# end=" " evita el salto de línea, el siguiente print continúa en la misma línea
print("Hola", end=" ")
print("Mundo")
```

</details>

---

### Ejercicio 10 — Potencia y módulo

Escribe un programa que calcule: la potencia de 2 elevado a 8, y si un número dado es par o impar usando el operador módulo `%`. Muestra los resultados con f-strings y comentarios.

<details>
<summary>💡 Pista</summary>

Un número es par si `numero % 2 == 0`.

</details>

<details>
<summary>✅ Solución</summary>

```python
# Potencia: 2 elevado a 8
resultado_potencia = 2 ** 8
print(f"2 elevado a 8 es: {resultado_potencia}")

numero = 17

# El operador % da el resto de la división; si es 0, el número es par
es_par = numero % 2 == 0
print(f"¿El número {numero} es par? {es_par}")
```

</details>

---

## 🟡 Ejercicios de Nivel Medio

---

### Ejercicio 11 — Precio con IVA y formato decimal

Declara una variable `precio_sin_iva = 49.9` y calcula el precio final aplicando un 21% de IVA. Muestra el resultado formateado con exactamente 2 decimales usando una f-string.

**Ejemplo de salida esperada:**
```
Precio sin IVA: 49.90 €
IVA (21%): 10.48 €
Precio final: 60.38 €
```

<details>
<summary>💡 Pista</summary>

En una f-string, usa `{valor:.2f}` para mostrar un float con 2 decimales.

</details>

<details>
<summary>✅ Solución</summary>

```python
precio_sin_iva = 49.9
iva = 0.21  # 21% expresado como decimal

# Calculamos el importe del IVA y el precio final
importe_iva = precio_sin_iva * iva
precio_final = precio_sin_iva + importe_iva

# Mostramos todo con 2 decimales usando :.2f en la f-string
print(f"Precio sin IVA: {precio_sin_iva:.2f} €")
print(f"IVA (21%): {importe_iva:.2f} €")
print(f"Precio final: {precio_final:.2f} €")
```

</details>

---

### Ejercicio 12 — Combinando `and` y `or`

Un parque de atracciones permite entrar a una atracción si el visitante mide más de 1.40 m, O si mide menos pero va acompañado de un adulto. Declara variables para la altura y si va acompañado, y calcula si puede acceder. Explica la lógica con comentarios.

<details>
<summary>✅ Solución</summary>

```python
altura = 1.35           # Altura del visitante en metros
acompanado = True       # ¿Va acompañado de un adulto?

# Condición 1: altura suficiente para entrar solo
altura_suficiente = altura >= 1.40

# Condición 2: aunque no llegue a la talla, puede entrar si va acompañado
puede_entrar = altura_suficiente or acompanado

print(f"Altura: {altura} m")
print(f"¿Altura suficiente? {altura_suficiente}")
print(f"¿Va acompañado? {acompanado}")
print(f"¿Puede entrar a la atracción? {puede_entrar}")
```

</details>

---

### Ejercicio 13 — Conversión entre tipos y operaciones mixtas

Tenemos la nota de un examen como string: `nota_str = "7"`. Conviértela a `int`, calcula si es suficiente para aprobar (nota >= 5) y muestra un mensaje completo con f-string indicando la nota y si está aprobado o no.

<details>
<summary>💡 Pista</summary>

Usa `int(nota_str)` para convertir el string a entero. El resultado de `nota >= 5` será un `bool`.

</details>

<details>
<summary>✅ Solución</summary>

```python
nota_str = "7"  # La nota llega como texto (str)

# Convertimos el string a entero para poder operar con él
nota = int(nota_str)

# Comprobamos si la nota es aprobado (5 o más)
aprobado = nota >= 5

print(f"Nota obtenida: {nota}")
print(f"¿Aprobado? {aprobado}")
```

</details>

---

### Ejercicio 14 — Operaciones con strings

Dado un nombre completo como `"ana garcia lopez"`, muestra: su longitud, la versión en mayúsculas, y una frase que lo use con la primera letra de cada palabra en mayúscula. Todo con f-strings y comentarios.

<details>
<summary>💡 Pista</summary>

Los métodos de string útiles aquí son `.upper()`, `.title()` y `len()`.

</details>

<details>
<summary>✅ Solución</summary>

```python
nombre_completo = "ana garcia lopez"

# Calculamos la longitud del nombre
longitud = len(nombre_completo)

# Versión en mayúsculas
en_mayusculas = nombre_completo.upper()

# Capitaliza la primera letra de cada palabra (estilo título)
en_titulo = nombre_completo.title()

print(f"Nombre original: {nombre_completo}")
print(f"Número de caracteres: {longitud}")
print(f"En mayúsculas: {en_mayusculas}")
print(f"Formato título: {en_titulo}")
```

</details>

---

### Ejercicio 15 — Divisibilidad con `and` y `%`

Escribe un programa que determine si un número es divisible por 3 y por 5 al mismo tiempo (es decir, divisible por 15). Pruébalo con los números 30, 45 y 12. Usa comentarios para explicar el criterio.

<details>
<summary>💡 Pista</summary>

Un número es divisible por N cuando `numero % N == 0`.

</details>

<details>
<summary>✅ Solución</summary>

```python
# Un número es divisible por 15 si su resto al dividir por 3 Y por 5 es 0
numero = 30

divisible_por_3 = numero % 3 == 0
divisible_por_5 = numero % 5 == 0

# Deben cumplirse LAS DOS condiciones simultáneamente
divisible_por_15 = divisible_por_3 and divisible_por_5

print(f"Número: {numero}")
print(f"¿Divisible por 3? {divisible_por_3}")
print(f"¿Divisible por 5? {divisible_por_5}")
print(f"¿Divisible por 15? {divisible_por_15}")
```

</details>

---

### Ejercicio 16 — Índice de Masa Corporal (IMC)

Calcula el IMC de una persona dada su masa (kg) y altura (m) usando la fórmula `IMC = peso / altura²`. Muestra el resultado con 1 decimal, el peso, la altura y si el IMC está en el rango considerado normal (entre 18.5 y 25).

<details>
<summary>💡 Pista</summary>

Para elevar al cuadrado usa `**2`. Para el rango puedes usar `18.5 <= imc <= 25` o el operador `and`.

</details>

<details>
<summary>✅ Solución</summary>

```python
peso = 70.0    # Peso en kilogramos
altura = 1.75  # Altura en metros

# Fórmula del IMC: peso dividido entre la altura al cuadrado
imc = peso / altura ** 2

# Rango normal según la OMS: entre 18.5 y 24.9
imc_normal = 18.5 <= imc <= 25

print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.1f}")
print(f"¿IMC en rango normal? {imc_normal}")
```

</details>

---

## 🔴 Ejercicios de Nivel Avanzado (para este bloque)

---

### Ejercicio 17 — Verificador de contraseña

Dada una contraseña como string, verifica con operadores lógicos y de comparación si cumple estas tres reglas simultáneamente:
1. Tiene más de 8 caracteres.
2. Contiene al menos un dígito (puedes asumir que lo sabes de antemano con una variable bool).
3. No es igual a `"password"` ni a `"12345678"`.

Muestra el resultado de cada regla por separado y si la contraseña es válida en conjunto.

<details>
<summary>💡 Pista</summary>

Usa `len()` para la longitud. Para la condición 3, combina `!=` con `and`.

</details>

<details>
<summary>✅ Solución</summary>

```python
contrasena = "MiClave99"
tiene_digito = True  # Simulamos que hemos comprobado si tiene algún número

# Regla 1: longitud mínima de 8 caracteres
regla_longitud = len(contrasena) > 8

# Regla 2: debe contener al menos un dígito
regla_digito = tiene_digito

# Regla 3: no puede ser una contraseña común/débil
regla_no_comun = contrasena != "password" and contrasena != "12345678"

# La contraseña es válida si cumple LAS TRES reglas
es_valida = regla_longitud and regla_digito and regla_no_comun

print(f"Contraseña: {contrasena}")
print(f"¿Longitud > 8? {regla_longitud}")
print(f"¿Contiene dígito? {regla_digito}")
print(f"¿No es contraseña común? {regla_no_comun}")
print(f"¿Contraseña válida? {es_valida}")
```

</details>

---

### Ejercicio 18 — Factura detallada

Crea un programa que genere una factura de compra. Declara: nombre del producto, cantidad (int), precio unitario (float) y si el cliente tiene tarjeta de fidelización (bool). Si tiene tarjeta, aplica un 5% de descuento sobre el total. Muestra una factura bien formateada con f-strings usando `:>10.2f` para alinear los números a la derecha.

**Ejemplo de salida:**
```
=== FACTURA ===
Producto:         Auriculares
Cantidad:                   2
Precio unidad:         29.99 €
Subtotal:              59.98 €
Descuento (5%):         3.00 €
TOTAL:                 56.98 €
```

<details>
<summary>💡 Pista</summary>

El especificador de formato `{valor:>10.2f}` alinea el número a la derecha en un campo de 10 caracteres con 2 decimales.

</details>

<details>
<summary>✅ Solución</summary>

```python
producto = "Auriculares"
cantidad = 2
precio_unitario = 29.99
tiene_fidelizacion = True  # ¿Cliente con tarjeta de fidelización?

# Calculamos el subtotal
subtotal = cantidad * precio_unitario

# Aplicamos descuento solo si tiene tarjeta de fidelización
descuento = subtotal * 0.05 if tiene_fidelizacion else 0
total = subtotal - descuento

# Mostramos la factura con alineación de columnas
print("=== FACTURA ===")
print(f"Producto:      {producto:>15}")
print(f"Cantidad:      {cantidad:>14}")
print(f"Precio unidad: {precio_unitario:>13.2f} €")
print(f"Subtotal:      {subtotal:>14.2f} €")
print(f"Descuento (5%): {descuento:>12.2f} €")
print(f"TOTAL:         {total:>14.2f} €")
```

</details>

---

### Ejercicio 19 — Año bisiesto

Un año es bisiesto si cumple alguna de estas condiciones:
- Es divisible por 4 **y no** es divisible por 100.
- **O** es divisible por 400.

Implementa la comprobación para un año dado usando únicamente operadores aritméticos (`%`), de comparación y lógicos (`and`, `or`, `not`). Prueba con: 2024, 1900 y 2000.

<details>
<summary>💡 Pista</summary>

Construye primero cada condición por separado con variables booleanas intermedias antes de combinarlas.

</details>

<details>
<summary>✅ Solución</summary>

```python
anio = 2024

# Condiciones individuales
divisible_por_4 = anio % 4 == 0
divisible_por_100 = anio % 100 == 0
divisible_por_400 = anio % 400 == 0

# Un año es bisiesto si:
# (es divisible por 4 Y NO por 100) O (es divisible por 400)
es_bisiesto = (divisible_por_4 and not divisible_por_100) or divisible_por_400

print(f"Año: {anio}")
print(f"¿Divisible por 4? {divisible_por_4}")
print(f"¿Divisible por 100? {divisible_por_100}")
print(f"¿Divisible por 400? {divisible_por_400}")
print(f"¿Es bisiesto? {es_bisiesto}")

# Prueba también con 1900 (no bisiesto) y 2000 (sí bisiesto)
```

</details>

---

### Ejercicio 20 — Elegibilidad para un préstamo

Un banco concede un préstamo si se cumplen TODAS estas condiciones:
- El cliente tiene más de 18 años.
- Sus ingresos anuales superan los 15.000 €.
- No tiene deudas pendientes.
- Su puntuación crediticia es mayor de 600 **o** lleva más de 5 años como cliente del banco.

Declara variables para cada dato y calcula si el préstamo es aprobado. Muestra el resultado de cada condición y la decisión final con un mensaje claro. Añade comentarios explicando la lógica del banco.

<details>
<summary>✅ Solución</summary>

```python
# Datos del solicitante
edad = 35
ingresos_anuales = 22000.0
tiene_deudas = False
puntuacion_crediticia = 580
anios_como_cliente = 7

# --- Evaluación de cada requisito ---

# Requisito 1: mayoría de edad
es_mayor = edad > 18

# Requisito 2: ingresos mínimos de 15.000 €
ingresos_suficientes = ingresos_anuales > 15000

# Requisito 3: sin deudas pendientes (negamos tiene_deudas)
sin_deudas = not tiene_deudas

# Requisito 4: buena puntuación crediticia O cliente de larga trayectoria
# Basta con que se cumpla una de las dos alternativas
buena_credibilidad = puntuacion_crediticia > 600 or anios_como_cliente > 5

# --- Decisión final ---
# El préstamo se aprueba SOLO si se cumplen los CUATRO requisitos
prestamo_aprobado = es_mayor and ingresos_suficientes and sin_deudas and buena_credibilidad

# Informe de la evaluación
print("=== EVALUACIÓN DE PRÉSTAMO ===")
print(f"Edad: {edad} años              → ¿Mayor de 18? {es_mayor}")
print(f"Ingresos: {ingresos_anuales:.0f} €        → ¿Suficientes? {ingresos_suficientes}")
print(f"¿Tiene deudas? {tiene_deudas}       → ¿Sin deudas? {sin_deudas}")
print(f"Puntuación: {puntuacion_crediticia} / Años cliente: {anios_como_cliente}")
print(f"                             → ¿Credibilidad OK? {buena_credibilidad}")
print()
print(f">>> PRÉSTAMO APROBADO: {prestamo_aprobado} <<<")
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
