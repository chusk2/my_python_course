# Jueves 16/04 — Bucles, Control de Flujo y Depuración Básica

---

## 1. ¿Qué es un bucle?

Un **bucle** (o ciclo) permite repetir un bloque de instrucciones múltiples veces. Sin bucles, si quisieras imprimir los números del 1 al 100, necesitarías 100 líneas de `print()`. Con un bucle, bastan 2 líneas.

Python tiene dos tipos de bucles:

- **`for`**: cuando sabes de antemano cuántas veces quieres repetir (o quieres recorrer una colección).
- **`while`**: cuando quieres repetir mientras se cumpla una condición.

---

## 2. El bucle `for`

### Recorrer un rango de números

La función `range()` genera una secuencia de números:

```python
# Imprime los números del 0 al 4 (5 no se incluye)
for i in range(5):
    print(i)
# Salida: 0, 1, 2, 3, 4
```

### Variantes de `range()`

```python
# range(inicio, fin) — desde inicio hasta fin-1
for i in range(1, 6):
    print(i)
# Salida: 1, 2, 3, 4, 5

# range(inicio, fin, paso) — saltando de X en X
for i in range(0, 20, 5):
    print(i)
# Salida: 0, 5, 10, 15

# Cuenta atrás (paso negativo)
for i in range(10, 0, -1):
    print(i)
# Salida: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

### Recorrer texto

Un `for` puede recorrer cada carácter de una cadena:

```python
palabra = "Python"
for letra in palabra:
    print(letra, end=" ")
# Salida: P y t h o n
```

### La variable del bucle

La variable `i` (o como la llames) toma un valor nuevo en cada vuelta (iteración):

```python
# Tabla de multiplicar del 7
for i in range(1, 11):
    resultado = 7 * i
    print(f"7 x {i} = {resultado}")
```

---

## 3. El bucle `while`

Repite un bloque **mientras** una condición sea `True`. Se usa cuando no sabemos de antemano cuántas repeticiones serán necesarias.

```python
# Pedir un número positivo (repetir hasta que lo introduzca)
numero = -1  # Inicializamos con un valor que no cumple la condición

while numero < 0:
    numero = int(input("Introduce un número positivo: "))
    if numero < 0:
        print("¡He dicho positivo! Inténtalo de nuevo.")

print(f"Gracias. Has introducido: {numero}")
```

### Anatomía del `while`

```python
while condición:       # Se evalúa ANTES de cada iteración
    instrucciones      # Se ejecutan si la condición es True
    # ...
    # En algún momento, algo debe hacer que la condición pase a False
    # Si no, ¡bucle infinito!
```

> **Peligro**: Si la condición nunca se hace `False`, el programa se ejecuta para siempre (bucle infinito). Puedes detenerlo con `Ctrl+C` en la terminal.

### Ejemplo: contador con `while`

```python
# Cuenta de 1 a 5
contador = 1

while contador <= 5:
    print(f"Vuelta número {contador}")
    contador += 1    # ¡No olvidar incrementar! Si no, bucle infinito

print("Bucle terminado.")
```

---

## 4. `break`, `continue` y `else` en bucles

### `break`: salir del bucle inmediatamente

```python
# Buscar un número específico
for i in range(1, 100):
    if i == 42:
        print(f"¡Encontrado! El número es {i}")
        break    # Sale del for inmediatamente
    print(f"Probando {i}...")

# El programa continúa aquí después del break
```

### `continue`: saltar a la siguiente iteración

```python
# Imprimir solo los números pares del 1 al 10
for i in range(1, 11):
    if i % 2 != 0:
        continue    # Si es impar, salta al siguiente i
    print(i)
# Salida: 2, 4, 6, 8, 10
```

### `else` en bucles

El bloque `else` de un bucle se ejecuta **solo si el bucle terminó sin `break`**:

```python
# Buscar si hay algún número negativo
numeros = [5, 3, 8, 2, 7]

for n in numeros:
    if n < 0:
        print("¡Hay un número negativo!")
        break
else:
    print("Todos los números son positivos.")
# Como no hay negativos, se ejecuta el else
```

---

## 5. Bucles anidados

Puedes poner un bucle dentro de otro. El bucle interior se ejecuta completamente por cada iteración del exterior:

```python
# Tablas de multiplicar del 1 al 5
for tabla in range(1, 6):
    print(f"\n--- Tabla del {tabla} ---")
    for i in range(1, 11):
        print(f"{tabla} x {i} = {tabla * i}")
```

**Cuidado**: Cada nivel de anidamiento multiplica el número de iteraciones. Un `for` de 100 dentro de otro `for` de 100 ejecuta 10.000 iteraciones.

---

## 6. Patrones comunes con bucles

### Acumulador (sumar valores)

```python
# Sumar los números del 1 al 100
total = 0
for i in range(1, 101):
    total += i
print(f"La suma de 1 a 100 es: {total}")  # 5050
```

### Contador

```python
# Contar cuántas vocales tiene una frase
frase = input("Escribe una frase: ")
vocales = 0

for letra in frase.lower():
    if letra in "aeiouáéíóú":
        vocales += 1

print(f"La frase tiene {vocales} vocales.")
```

### Buscar el máximo o mínimo

```python
# Pedir 5 números y encontrar el mayor
mayor = None

for i in range(1, 6):
    numero = float(input(f"Número {i}: "))
    if mayor is None or numero > mayor:
        mayor = numero

print(f"El mayor es: {mayor}")
```

### Menú interactivo con `while`

```python
# Menú que se repite hasta que el usuario elija salir
while True:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Despedir")
    print("3. Salir")

    opcion = input("Elige: ")

    if opcion == "1":
        print("¡Hola!")
    elif opcion == "2":
        print("¡Adiós!")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")
```

---

## 7. Depuración básica

**Depurar** (debugging) es el proceso de encontrar y corregir errores en tu código. Algunos trucos fundamentales:

### 7.1 Print de depuración

El método más sencillo: añade `print()` temporales para ver qué valor tienen tus variables en cada paso:

```python
total = 0
for i in range(1, 6):
    total += i
    print(f"[DEBUG] i={i}, total={total}")  # Temporal, borrar después

# [DEBUG] i=1, total=1
# [DEBUG] i=2, total=3
# [DEBUG] i=3, total=6
# ...
```

### 7.2 Leer los mensajes de error

Recuerda de la Semana 1: lee siempre la **última línea** del error. Además, Python te indica el **número de línea** donde ocurrió el problema.

### 7.3 Errores comunes en bucles

```python
# Error 1: Bucle infinito (olvidar incrementar)
i = 0
while i < 5:
    print(i)
    # Falta: i += 1  → bucle infinito

# Error 2: Off-by-one (pasarse o quedarse corto)
# Si quieres del 1 al 10 inclusive:
for i in range(1, 10):    # ¡Solo llega al 9!
    print(i)
for i in range(1, 11):    # Correcto: llega al 10
    print(i)

# Error 3: Modificar la variable del for (no tiene efecto)
for i in range(5):
    i = i * 2     # Esto NO cambia el rango, en la siguiente vuelta i se reasigna
    print(i)
# Imprime: 0, 2, 4, 6, 8 (parece funcionar, pero es engañoso)
```

### 7.4 El depurador de VS Code

VS Code tiene un depurador integrado que permite:

- **Puntos de parada (breakpoints)**: haz clic en el margen izquierdo de una línea para que el programa se detenga ahí.
- **Ejecución paso a paso**: avanza línea a línea y observa cómo cambian las variables.
- **Panel de variables**: muestra en tiempo real el valor de cada variable.

Para usarlo: abre tu archivo `.py`, pon un breakpoint, y pulsa `F5` o ve a *Ejecutar > Iniciar depuración*.

---

## 8. Ejemplo integrador: juego de adivinanzas

```python
import random

# Generamos un número aleatorio entre 1 y 50
numero_secreto = random.randint(1, 50)
intentos = 0
max_intentos = 7

print("=== ADIVINA EL NÚMERO ===")
print(f"He pensado un número entre 1 y 50. Tienes {max_intentos} intentos.")

while intentos < max_intentos:
    respuesta = int(input(f"\nIntento {intentos + 1}/{max_intentos}: "))
    intentos += 1

    if respuesta == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos.")
        break
    elif respuesta < numero_secreto:
        print("Demasiado bajo...")
    else:
        print("Demasiado alto...")
else:
    # Se ejecuta si el while termina sin break (no adivinó)
    print(f"\nSe acabaron los intentos. El número era {numero_secreto}.")
```

---

## Resumen de la sesión

| Concepto         | Idea clave                                                        |
|------------------|-------------------------------------------------------------------|
| `for`            | Repite un número conocido de veces o recorre una secuencia        |
| `range()`        | Genera secuencias de números: `range(inicio, fin, paso)`          |
| `while`          | Repite mientras la condición sea `True`                           |
| `break`          | Sale del bucle inmediatamente                                     |
| `continue`       | Salta a la siguiente iteración                                    |
| `else` en bucles | Se ejecuta solo si el bucle terminó sin `break`                   |
| Bucles anidados  | Un bucle dentro de otro (cuidado con el rendimiento)              |
| Acumulador       | `total += valor` dentro de un bucle                               |
| Depuración       | `print()` temporal, leer errores, usar breakpoints en VS Code     |

---

*Siguiente clase: Viernes 17/04 — Manipulación y formateo de cadenas de texto.*
