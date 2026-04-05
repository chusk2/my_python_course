# Viernes 17/04 — Manipulación y Formateo de Cadenas de Texto

---

## 1. Las cadenas son secuencias

En Python, una cadena de texto (`str`) es una **secuencia ordenada de caracteres**. Cada carácter tiene una posición (índice) que empieza en **0**:

```
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

```python
texto = "Python"
print(texto[0])    # P (primer carácter)
print(texto[5])    # n (último carácter)
print(texto[-1])   # n (último carácter, con índice negativo)
print(texto[-2])   # o (penúltimo)
```

> **Las cadenas son inmutables**: no puedes cambiar un carácter individual. `texto[0] = "J"` daría error. Si necesitas cambiar algo, creas una cadena nueva.

---

## 2. Slicing (rebanado)

El **slicing** permite extraer una porción de la cadena con la sintaxis `texto[inicio:fin:paso]`:

```python
texto = "Programación en Python"

print(texto[0:12])     # "Programación" (del 0 al 11)
print(texto[16:])      # "Python" (del 16 hasta el final)
print(texto[:12])      # "Programación" (del inicio al 11)
print(texto[::2])      # "Pormaió nPto" (cada 2 caracteres)
print(texto[::-1])     # "nohtyP ne nóicamargorP" (al revés)
```

**Regla**: `texto[inicio:fin]` incluye `inicio` pero **no** incluye `fin`.

### Ejemplos prácticos de slicing

```python
dni = "12345678A"
numero_dni = dni[:-1]    # "12345678" (todo menos la última letra)
letra_dni = dni[-1]      # "A" (solo la letra)

fecha = "15/04/2026"
dia = fecha[:2]          # "15"
mes = fecha[3:5]         # "04"
anio = fecha[6:]         # "2026"
```

---

## 3. Métodos principales de cadenas

Los métodos son funciones que se aplican sobre una cadena con la sintaxis `cadena.metodo()`. Como las cadenas son inmutables, los métodos **devuelven una cadena nueva** sin modificar la original.

### 3.1 Cambiar mayúsculas y minúsculas

```python
texto = "Hola Mundo"

print(texto.upper())       # "HOLA MUNDO"
print(texto.lower())       # "hola mundo"
print(texto.capitalize())  # "Hola mundo" (solo la primera letra mayúscula)
print(texto.title())       # "Hola Mundo" (primera de cada palabra)
print(texto.swapcase())    # "hOLA mUNDO" (invierte mayúsculas/minúsculas)
```

### 3.2 Eliminar espacios

```python
texto = "   datos con espacios   "

print(texto.strip())       # "datos con espacios" (quita espacios de ambos lados)
print(texto.lstrip())      # "datos con espacios   " (solo por la izquierda)
print(texto.rstrip())      # "   datos con espacios" (solo por la derecha)
```

**Aplicación real**: Limpiar datos introducidos por el usuario. Siempre es buena práctica hacer `input(...).strip()` para eliminar espacios accidentales.

### 3.3 Buscar y comprobar

```python
texto = "El informe trimestral de ventas Q3 2026"

# Buscar posición de un texto (devuelve -1 si no lo encuentra)
print(texto.find("ventas"))       # 28
print(texto.find("gastos"))       # -1

# Contar apariciones
print(texto.count("e"))           # 4

# Comprobar contenido
print(texto.startswith("El"))     # True
print(texto.endswith("2026"))     # True
print("ventas" in texto)          # True (operador in)
```

### 3.4 Reemplazar

```python
texto = "El precio es 100 euros. Total: 100 euros."

# replace(viejo, nuevo) — reemplaza TODAS las apariciones
nuevo = texto.replace("euros", "€")
print(nuevo)   # "El precio es 100 €. Total: 100 €."

# replace(viejo, nuevo, max_reemplazos)
nuevo = texto.replace("100", "200", 1)  # Solo reemplaza la primera
print(nuevo)   # "El precio es 200 euros. Total: 100 euros."
```

### 3.5 Dividir y unir

```python
# split() divide una cadena en una lista de trozos
frase = "Python es un lenguaje versátil"
palabras = frase.split()
print(palabras)   # ['Python', 'es', 'un', 'lenguaje', 'versátil']

# split() con un separador específico
datos = "Ana;28;Málaga;Contable"
campos = datos.split(";")
print(campos)     # ['Ana', '28', 'Málaga', 'Contable']

# join() une una lista en una cadena
lista = ["uno", "dos", "tres"]
resultado = ", ".join(lista)
print(resultado)  # "uno, dos, tres"

resultado = " - ".join(lista)
print(resultado)  # "uno - dos - tres"
```

### 3.6 Comprobar el contenido

```python
# Métodos que devuelven True o False
print("12345".isdigit())      # True (solo dígitos)
print("Hola".isalpha())       # True (solo letras)
print("Hola123".isalnum())    # True (letras y/o dígitos)
print("   ".isspace())        # True (solo espacios)
print("HOLA".isupper())       # True (todo mayúsculas)
print("hola".islower())       # True (todo minúsculas)
```

---

## 4. Formateo de cadenas: las tres formas

### 4.1 f-strings (recomendado, Python 3.6+)

Ya los conocemos de sesiones anteriores. Son la forma más moderna y legible:

```python
nombre = "Laura"
saldo = 1523.456

print(f"Hola, {nombre}. Tu saldo es {saldo:.2f} €")
# "Hola, Laura. Tu saldo es 1523.46 €"
```

### 4.2 Método `.format()`

Forma anterior a los f-strings, aún muy usada:

```python
print("Hola, {}. Tu saldo es {:.2f} €".format(nombre, saldo))

# Con índices
print("{0} tiene {1} años. {0} vive en Málaga.".format("Ana", 30))

# Con nombres
print("{nombre} tiene {edad} años".format(nombre="Ana", edad=30))
```

### 4.3 Operador `%` (estilo antiguo)

Lo verás en código antiguo. No se recomienda para código nuevo:

```python
print("Hola, %s. Tu saldo es %.2f €" % (nombre, saldo))
```

### Especificadores de formato comunes

| Código     | Significado                   | Ejemplo                        | Resultado       |
|------------|-------------------------------|--------------------------------|-----------------|
| `:.2f`     | 2 decimales                   | `f"{3.14159:.2f}"`             | `"3.14"`        |
| `:,.2f`    | Separador de miles + decimales| `f"{1234567.89:,.2f}"`         | `"1,234,567.89"`|
| `:.1%`     | Porcentaje con 1 decimal      | `f"{0.156:.1%}"`               | `"15.6%"`       |
| `:>10`     | Alinear a la derecha (10 car) | `f"{'Hola':>10}"`             | `"      Hola"`  |
| `:<10`     | Alinear a la izquierda        | `f"{'Hola':<10}"`             | `"Hola      "`  |
| `:^10`     | Centrar                       | `f"{'Hola':^10}"`             | `"   Hola   "`  |
| `:05d`     | Rellenar con ceros            | `f"{42:05d}"`                  | `"00042"`       |

---

## 5. Cadenas multilínea y caracteres especiales

### Cadenas multilínea

```python
mensaje = """Estimado cliente:

Le informamos de que su pedido
ha sido enviado correctamente.

Atentamente, El equipo."""

print(mensaje)
```

### Caracteres de escape

| Secuencia | Significado            |
|-----------|------------------------|
| `\n`      | Salto de línea         |
| `\t`      | Tabulación             |
| `\\`      | Barra invertida literal|
| `\"`      | Comilla doble literal  |
| `\'`      | Comilla simple literal |

```python
print("Primera línea\nSegunda línea")
print("Columna1\tColumna2\tColumna3")
print("Ruta: C:\\Users\\Documentos")
```

---

## 6. Aplicaciones prácticas

### Limpiar y normalizar datos de entrada

```python
# El usuario introduce datos con espacios y mayúsculas inconsistentes
email = input("Email: ").strip().lower()
nombre = input("Nombre: ").strip().title()

print(f"Email normalizado: {email}")
print(f"Nombre normalizado: {nombre}")
```

### Extraer información de un texto estructurado

```python
# Línea de un archivo CSV
linea = "García López, María;28;Málaga;1850.00"

campos = linea.split(";")
nombre_completo = campos[0]
edad = int(campos[1])
ciudad = campos[2]
salario = float(campos[3])

# Separar nombre y apellidos
partes_nombre = nombre_completo.split(", ")
apellidos = partes_nombre[0]
nombre = partes_nombre[1]

print(f"Nombre: {nombre} {apellidos}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad}")
print(f"Salario: {salario:.2f} €")
```

### Generar un informe con formato de tabla

```python
# Datos (simulados, aún sin listas formalmente)
print(f"{'PRODUCTO':<20} {'PRECIO':>10} {'STOCK':>8}")
print("-" * 40)
print(f"{'Camiseta algodón':<20} {'12.99':>10} {'150':>8}")
print(f"{'Pantalón vaquero':<20} {'29.99':>10} {'85':>8}")
print(f"{'Zapatillas running':<20} {'59.99':>10} {'42':>8}")
print("-" * 40)
```

---

## Resumen de la sesión

| Concepto            | Idea clave                                                    |
|---------------------|---------------------------------------------------------------|
| Índices             | Empiezan en 0. Negativos cuentan desde el final               |
| Slicing             | `texto[inicio:fin:paso]` para extraer porciones               |
| Inmutabilidad       | Las cadenas no se modifican, se crean nuevas                   |
| `.upper()/.lower()` | Cambiar mayúsculas/minúsculas                                 |
| `.strip()`          | Eliminar espacios laterales                                    |
| `.find()/.count()`  | Buscar y contar texto dentro de otro                           |
| `.replace()`        | Reemplazar apariciones de un texto por otro                    |
| `.split()/.join()`  | Dividir cadena en lista / Unir lista en cadena                 |
| f-strings           | `f"Texto {variable:.2f}"` — formato moderno y legible          |
| Especificadores     | `:.2f`, `:>10`, `:<10`, `:05d`, `:.1%`                        |

---

*Siguiente semana: Semana 3 — Listas, tuplas, diccionarios, conjuntos y funciones.*
