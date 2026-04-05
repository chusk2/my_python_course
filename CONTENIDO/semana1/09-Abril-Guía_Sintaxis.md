# Jueves 09/04 — Sintaxis Básica, Entrada y Salida de Datos y Buenas Prácticas

---

## 1. La sintaxis de Python: las reglas del juego

Al igual que el español tiene reglas gramaticales (sujeto, verbo, predicado), Python tiene reglas de **sintaxis** que debemos respetar para que el intérprete entienda nuestras instrucciones.

### 1.1 Indentación (sangrado)

En Python, la indentación no es decorativa: **es obligatoria**. Define qué instrucciones pertenecen a un bloque de código. Se usa una tabulación o 4 espacios (lo estándar son 4 espacios).

```python
# Correcto: el bloque dentro del if está indentado
if 5 > 3:
    print("Cinco es mayor que tres")

# Incorrecto: Python dará un error
if 5 > 3:
print("Esto da error")  # Falta la indentación
```

> **Consejo**: Configura tu editor (VS Code) para que use 4 espacios al pulsar la tecla Tab. VS Code lo hace por defecto con la extensión de Python.

### 1.2 Comentarios

Los comentarios son notas que escribimos en el código para explicar qué hace. Python los ignora al ejecutar el programa, pero son fundamentales para que otras personas (o tú mismo en el futuro) entiendan el código.

```python
# Esto es un comentario de una línea

"""
Esto es un comentario
de varias líneas.
Se usa para explicaciones más largas.
"""

precio = 19.99  # También puedes comentar al final de una línea
```

### 1.3 Mayúsculas y minúsculas importan

Python distingue entre mayúsculas y minúsculas. `nombre`, `Nombre` y `NOMBRE` son tres cosas completamente diferentes.

```python
nombre = "Ana"
Nombre = "Luis"
print(nombre)   # Muestra: Ana
print(Nombre)   # Muestra: Luis
```

### 1.4 Punto y coma (no es necesario)

A diferencia de otros lenguajes como Java o JavaScript, en Python **no se usa punto y coma** al final de cada línea. Cada instrucción va en su propia línea.

```python
# Así se escribe en Python (una instrucción por línea)
saludo = "Hola"
print(saludo)
```

---

## 2. La función `print()` — Mostrar información en pantalla

`print()` es la forma que tiene Python de mostrar resultados al usuario. Es probablemente la función que más usarás al principio.

```python
# Mostrar texto (entre comillas)
print("Bienvenido al curso de Python")

# Mostrar números
print(42)
print(3.14)

# Mostrar el resultado de una operación
print(10 + 5)

# Mostrar varias cosas separadas por coma
print("El resultado es:", 10 + 5)
```

### Parámetro `sep` (separador)

Por defecto, `print()` separa los elementos con un espacio. Puedes cambiarlo:

```python
print("Día", "Mes", "Año", sep="/")
# Resultado: Día/Mes/Año

print("uno", "dos", "tres", sep=" - ")
# Resultado: uno - dos - tres
```

### Parámetro `end` (final de línea)

Por defecto, `print()` añade un salto de línea al final. Puedes cambiarlo:

```python
print("Hola", end=" ")
print("Mundo")
# Resultado: Hola Mundo (en una sola línea)
```

---

## 3. La función `input()` — Recibir información del usuario

`input()` permite que el programa se detenga y espere a que el usuario escriba algo por teclado.

```python
nombre = input("¿Cómo te llamas? ")
print("¡Hola,", nombre, "!")
```

**Importante**: `input()` **siempre devuelve texto** (una cadena de caracteres), aunque el usuario escriba un número. Esto es crucial y lo veremos con más detalle en la clase del viernes.

```python
edad = input("¿Cuántos años tienes? ")
# Si el usuario escribe 25, la variable edad contiene "25" (texto, no número)

# Para usarlo como número, hay que convertirlo:
edad_numero = int(edad)
print("El año que viene tendrás", edad_numero + 1, "años")
```

---

## 4. Secuencia de instrucciones: el flujo natural

Un programa en Python se ejecuta de **arriba a abajo**, línea a línea. Esto es lo que llamamos ejecución secuencial:

```python
# Línea 1: se ejecuta primero
print("Paso 1: Saludamos")

# Línea 2: se ejecuta después
nombre = input("Paso 2: ¿Tu nombre? ")

# Línea 3: se ejecuta por último
print("Paso 3: Encantado,", nombre)
```

El orden importa. Si intentas usar una variable antes de crearla, Python dará un error:

```python
# Esto da error: "ciudad" no existe todavía
print(ciudad)
ciudad = "Málaga"
```

---

## 5. Errores comunes y cómo interpretarlos

Equivocarse es parte del proceso. Python te indica qué ha ido mal con mensajes de error. Aprender a leerlos es una habilidad fundamental.

### SyntaxError (error de sintaxis)

Se ha escrito algo que Python no entiende:

```python
# Falta cerrar el paréntesis
print("Hola"
# SyntaxError: unexpected EOF while parsing
```

### NameError (nombre no definido)

Se intenta usar una variable que no existe:

```python
print(salario)
# NameError: name 'salario' is not defined
```

### IndentationError (error de indentación)

La sangría no es correcta:

```python
if True:
print("Mal indentado")
# IndentationError: expected an indented block
```

### TypeError (error de tipo)

Se intenta hacer una operación con tipos incompatibles:

```python
edad = input("Edad: ")  # Esto es texto
print(edad + 5)
# TypeError: can only concatenate str (not "int") to str
```

> **Consejo**: Lee siempre la **última línea** del mensaje de error. Es la que te dice exactamente qué ha fallado.

---

## 6. Buenas prácticas desde el primer día

### 6.1 Nombres descriptivos

```python
# Mal: ¿qué es x?
x = 1500

# Bien: se entiende al leerlo
salario_mensual = 1500
```

### 6.2 Nombres en minúsculas con guiones bajos

Python usa la convención `snake_case` para nombres de variables y funciones:

```python
# Bien (snake_case)
nombre_completo = "María García"
precio_con_iva = 24.20

# No recomendado (otros estilos)
NombreCompleto = "María García"   # CamelCase (se usa en clases, no en variables)
PRECIOCONIVA = 24.20              # Difícil de leer
```

### 6.3 Comentarios útiles

```python
# Mal: el comentario repite lo que ya dice el código
x = 5  # Asigno 5 a x

# Bien: el comentario explica el "por qué"
descuento = 0.15  # 15% de descuento para clientes nuevos
```

### 6.4 Líneas en blanco para separar bloques

```python
# Bloque 1: recogida de datos
nombre = input("Nombre: ")
edad = input("Edad: ")

# Bloque 2: procesamiento
edad_numero = int(edad)
anio_nacimiento = 2026 - edad_numero

# Bloque 3: salida de resultados
print("Hola,", nombre)
print("Naciste aproximadamente en", anio_nacimiento)
```

### 6.5 Evitar líneas demasiado largas

Intenta que cada línea no supere los 79 caracteres (recomendación oficial de Python, PEP 8). Si una línea es muy larga, puedes partirla:

```python
# Línea larga partida con paréntesis
mensaje = (
    "Este es un mensaje muy largo que no cabe "
    "en una sola línea de código"
)
print(mensaje)
```

---

## 7. Combinando todo: mini-programas de ejemplo

### Ejemplo 1: Saludo personalizado

```python
# Programa que saluda al usuario y le dice la hora de clase
nombre = input("¡Hola! ¿Cómo te llamas? ")
print("Encantado,", nombre)
print("Recuerda: la clase es de 16:00 a 18:30")
```

### Ejemplo 2: Calculadora de propina

```python
# Calculadora simple de propina en un restaurante
cuenta = input("¿Cuánto ha sido la cuenta? (€) ")
cuenta = float(cuenta)  # Convertimos a número decimal

propina = cuenta * 0.10  # 10% de propina
total = cuenta + propina

print("Cuenta:", cuenta, "€")
print("Propina (10%):", propina, "€")
print("Total a pagar:", total, "€")
```

### Ejemplo 3: Datos de un empleado

```python
# Registro sencillo de datos de un empleado
print("=== REGISTRO DE EMPLEADO ===")
nombre = input("Nombre completo: ")
departamento = input("Departamento: ")
antiguedad = input("Años de antigüedad: ")

print()  # Línea en blanco para separar
print("--- Resumen ---")
print("Empleado:", nombre)
print("Departamento:", departamento)
print("Antigüedad:", antiguedad, "años")
```

---

## Resumen de la sesión

| Concepto            | Idea clave                                                   |
|---------------------|--------------------------------------------------------------|
| Indentación         | 4 espacios, obligatoria para definir bloques                 |
| Comentarios         | `#` para una línea, `""" """` para varias                    |
| `print()`           | Muestra información en pantalla                              |
| `input()`           | Recoge información del usuario (siempre como texto)          |
| Ejecución secuencial| El código se ejecuta de arriba a abajo                       |
| Errores             | Leer siempre la última línea del mensaje                     |
| Buenas prácticas    | Nombres descriptivos, snake_case, comentarios útiles         |

---

*Siguiente clase: Viernes 10/04 — Variables, tipos de datos y conversión entre tipos.*
