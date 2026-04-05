# Ejercicios — Jueves 09/04: Sintaxis Básica, Entrada y Salida de Datos

---

## Ejercicios Básicos (1–5)

---

### Ejercicio 1: Presentación personal

Escribe un programa que muestre en pantalla (usando `print()`) tu nombre, tu ciudad y tu comida favorita, cada dato en una línea diferente.

**Ejemplo de salida:**
```
Me llamo Ana
Vivo en Málaga
Mi comida favorita es la paella
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 1: Presentación personal
# Usamos print() para mostrar cada dato en una línea independiente
print("Me llamo Ana")
print("Vivo en Málaga")
print("Mi comida favorita es la paella")
```

</details>

---

### Ejercicio 2: Datos de un producto

Escribe un programa que pida al usuario el nombre de un producto y su precio, y los muestre en pantalla con un formato claro.

**Ejemplo de interacción:**
```
Nombre del producto: Camiseta
Precio del producto: 25.99
---
Producto: Camiseta
Precio: 25.99 €
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 2: Datos de un producto
# Usamos input() para recoger datos y print() para mostrarlos
nombre_producto = input("Nombre del producto: ")
precio_producto = input("Precio del producto: ")

# Mostramos los datos formateados
print("---")
print("Producto:", nombre_producto)
print("Precio:", precio_producto, "€")
```

</details>

---

### Ejercicio 3: Saludo según el nombre

Escribe un programa que pregunte al usuario su nombre y le muestre un saludo personalizado usando `print()` con varios elementos separados por coma.

**Ejemplo de interacción:**
```
¿Cómo te llamas? María
¡Bienvenida al curso, María! Esperamos que aprendas mucho.
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 3: Saludo personalizado
# Recogemos el nombre del usuario
nombre = input("¿Cómo te llamas? ")

# Mostramos un saludo combinando texto y la variable
print("¡Bienvenida al curso,", nombre + "! Esperamos que aprendas mucho.")
```

</details>

---

### Ejercicio 4: Separador personalizado

Usa el parámetro `sep` de `print()` para mostrar una fecha en formato `DD/MM/AAAA`, pidiendo al usuario el día, el mes y el año por separado.

**Ejemplo de interacción:**
```
Día: 9
Mes: 4
Año: 2026
Fecha: 9/4/2026
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 4: Fecha con separador personalizado
# Recogemos cada parte de la fecha por separado
dia = input("Día: ")
mes = input("Mes: ")
anio = input("Año: ")

# Usamos sep="/" para que print() separe los valores con barras
print("Fecha:", dia, mes, anio, sep="/")
# Nota: "Fecha:" también se separa con "/", así que una alternativa mejor sería:
# print("Fecha: " + dia + "/" + mes + "/" + anio)
```

**Versión mejorada:**

```python
# Versión corregida para que "Fecha:" no se vea afectado por sep
dia = input("Día: ")
mes = input("Mes: ")
anio = input("Año: ")

# Concatenamos el texto de "Fecha: " por separado
print("Fecha: " + dia + "/" + mes + "/" + anio)
```

</details>

---

### Ejercicio 5: Tarjeta de visita

Escribe un programa que pida el nombre, el puesto de trabajo y el teléfono de una persona, y muestre una "tarjeta de visita" usando caracteres como `=`, `-` y `|`.

**Ejemplo de salida:**
```
================================
|  Nombre:   Ana García        |
|  Puesto:   Contable          |
|  Teléfono: 600 123 456       |
================================
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 5: Tarjeta de visita
# Recogemos los datos del usuario
nombre = input("Nombre: ")
puesto = input("Puesto de trabajo: ")
telefono = input("Teléfono: ")

# Mostramos la tarjeta con formato
print("=" * 35)
print("|  Nombre:  ", nombre)
print("|  Puesto:  ", puesto)
print("|  Teléfono:", telefono)
print("=" * 35)
```

</details>

---

## Ejercicios de Nivel Medio (6–8)

---

### Ejercicio 6: Calculadora de supermercado

Escribe un programa que pida al usuario el nombre y precio de 3 productos de la compra. El programa debe mostrar el listado de productos y el total a pagar. Recuerda que `input()` devuelve texto, así que deberás convertir los precios a número con `float()`.

**Ejemplo de interacción:**
```
Producto 1: Leche
Precio 1: 1.20
Producto 2: Pan
Precio 2: 0.85
Producto 3: Huevos
Precio 3: 2.10

--- TICKET DE COMPRA ---
Leche        1.20 €
Pan          0.85 €
Huevos       2.10 €
------------------------
TOTAL:       4.15 €
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 6: Calculadora de supermercado
# Recogemos nombre y precio de 3 productos
producto1 = input("Producto 1: ")
precio1 = float(input("Precio 1: "))

producto2 = input("Producto 2: ")
precio2 = float(input("Precio 2: "))

producto3 = input("Producto 3: ")
precio3 = float(input("Precio 3: "))

# Calculamos el total
total = precio1 + precio2 + precio3

# Mostramos el ticket
print()
print("--- TICKET DE COMPRA ---")
print(producto1, "       ", precio1, "€")
print(producto2, "       ", precio2, "€")
print(producto3, "       ", precio3, "€")
print("------------------------")
print("TOTAL:       ", total, "€")
```

</details>

---

### Ejercicio 7: Generador de email corporativo

Escribe un programa que pida al usuario su nombre, su primer apellido y el nombre de su empresa. El programa debe generar una dirección de email corporativa en formato `nombre.apellido@empresa.com`, todo en minúsculas.

**Pista**: Investiga el método `.lower()` que tienen las cadenas de texto.

**Ejemplo de interacción:**
```
Nombre: María
Primer apellido: García
Empresa: Acme
Tu email corporativo sería: maria.garcia@acme.com
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 7: Generador de email corporativo
# Recogemos los datos del usuario
nombre = input("Nombre: ")
apellido = input("Primer apellido: ")
empresa = input("Empresa: ")

# Construimos el email pasando todo a minúsculas con .lower()
email = nombre.lower() + "." + apellido.lower() + "@" + empresa.lower() + ".com"

# Mostramos el resultado
print("Tu email corporativo sería:", email)
```

</details>

---

### Ejercicio 8: Registro de incidencia técnica (Help Desk)

Escribe un programa que simule el registro de una incidencia en un sistema de soporte técnico. Debe pedir: nombre del usuario, número de empleado, descripción breve del problema y nivel de urgencia (1-Baja, 2-Media, 3-Alta). Muestra un resumen con un número de ticket ficticio (puedes inventarlo o usar un texto fijo como "INC-2026-0001").

**Ejemplo de interacción:**
```
=== REGISTRO DE INCIDENCIA ===
Nombre del usuario: Pedro Ruiz
Número de empleado: EMP-4521
Descripción del problema: El ordenador no enciende
Nivel de urgencia (1-Baja, 2-Media, 3-Alta): 3

=== TICKET GENERADO ===
Ticket:      INC-2026-0001
Empleado:    Pedro Ruiz (EMP-4521)
Problema:    El ordenador no enciende
Urgencia:    3 - Alta
Estado:      Abierto
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 8: Registro de incidencia técnica
# Número de ticket fijo (en un sistema real sería auto-generado)
numero_ticket = "INC-2026-0001"

# Recogemos los datos de la incidencia
print("=== REGISTRO DE INCIDENCIA ===")
nombre_usuario = input("Nombre del usuario: ")
numero_empleado = input("Número de empleado: ")
descripcion = input("Descripción del problema: ")
urgencia = input("Nivel de urgencia (1-Baja, 2-Media, 3-Alta): ")

# Determinamos el texto de la urgencia según el número introducido
# (De momento usamos una solución sencilla sin condicionales)
texto_urgencia = urgencia
if urgencia == "1":
    texto_urgencia = "1 - Baja"
elif urgencia == "2":
    texto_urgencia = "2 - Media"
elif urgencia == "3":
    texto_urgencia = "3 - Alta"

# Mostramos el resumen del ticket
print()
print("=== TICKET GENERADO ===")
print("Ticket:     ", numero_ticket)
print("Empleado:   ", nombre_usuario, "(" + numero_empleado + ")")
print("Problema:   ", descripcion)
print("Urgencia:   ", texto_urgencia)
print("Estado:      Abierto")
```

</details>

---

## Ejercicios de Nivel Superior (9–10)

---

### Ejercicio 9: Generador de recibos de alquiler

Escribe un programa que genere un recibo de alquiler. Debe pedir: nombre del inquilino, dirección del inmueble, importe mensual del alquiler y mes/año del recibo. El programa debe calcular el IVA (si aplica, al 21%) y mostrar un recibo formateado. Usa conversión de tipos para trabajar con los importes y el parámetro `end` de `print()` donde lo consideres útil.

**Ejemplo de salida:**
```
==============================
     RECIBO DE ALQUILER
==============================
Inquilino: Laura Sánchez
Dirección: C/ Larios 15, 2ºB
Periodo:   Abril 2026

Alquiler base:    750.00 €
IVA (21%):        157.50 €
------------------------------
TOTAL:            907.50 €
==============================
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 9: Generador de recibos de alquiler
# Recogemos los datos
print("=== DATOS DEL RECIBO ===")
inquilino = input("Nombre del inquilino: ")
direccion = input("Dirección del inmueble: ")
mes = input("Mes del recibo: ")
anio = input("Año del recibo: ")
alquiler_texto = input("Importe mensual del alquiler (€): ")

# Convertimos el importe a número decimal
alquiler = float(alquiler_texto)

# Calculamos el IVA y el total
iva = alquiler * 0.21
total = alquiler + iva

# Construimos el periodo juntando mes y año
periodo = mes + " " + anio

# Mostramos el recibo formateado
print()
print("=" * 35)
print("     RECIBO DE ALQUILER")
print("=" * 35)
print("Inquilino:", inquilino)
print("Dirección:", direccion)
print("Periodo:  ", periodo)
print()
# Usamos end="" para controlar el formato en la misma línea
print("Alquiler base: ", end="")
print(str(alquiler) + " €")
print("IVA (21%):     ", end="")
print(str(round(iva, 2)) + " €")
print("-" * 35)
print("TOTAL:         ", end="")
print(str(round(total, 2)) + " €")
print("=" * 35)
```

</details>

---

### Ejercicio 10: Simulador de terminal de comandos

Crea un programa que simule un mini-terminal. El programa debe pedir al usuario su nombre de usuario y mostrar un prompt (como en una terminal real). Luego, debe pedir 3 "comandos" (simplemente texto que el usuario escriba) y mostrar una respuesta ficticia para cada uno. Al final, debe mostrar un resumen de la sesión con el número de comandos ejecutados y la longitud total de caracteres escritos.

**Pista**: Usa `len()` para contar los caracteres de un texto.

**Ejemplo de interacción:**
```
=== SIMULADOR DE TERMINAL ===
Usuario: admin

admin@python:~$ whoami
> Respuesta: Usuario actual: admin

admin@python:~$ date
> Respuesta: Fecha del sistema: 09/04/2026

admin@python:~$ help
> Respuesta: Comandos disponibles: whoami, date, help, exit

=== RESUMEN DE SESIÓN ===
Usuario: admin
Comandos ejecutados: 3
Total caracteres escritos: 15
Sesión finalizada.
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 10: Simulador de terminal de comandos
# Recogemos el nombre de usuario
print("=== SIMULADOR DE TERMINAL ===")
usuario = input("Usuario: ")
print()

# Construimos el prompt personalizado
prompt = usuario + "@python:~$ "

# Pedimos 3 comandos al usuario
comando1 = input(prompt)
print("> Respuesta: Comando '" + comando1 + "' ejecutado correctamente.")
print()

comando2 = input(prompt)
print("> Respuesta: Comando '" + comando2 + "' ejecutado correctamente.")
print()

comando3 = input(prompt)
print("> Respuesta: Comando '" + comando3 + "' ejecutado correctamente.")
print()

# Calculamos estadísticas de la sesión
total_comandos = 3
# Sumamos la longitud de cada comando para saber el total de caracteres escritos
total_caracteres = len(comando1) + len(comando2) + len(comando3)

# Mostramos el resumen
print("=== RESUMEN DE SESIÓN ===")
print("Usuario:", usuario)
print("Comandos ejecutados:", total_comandos)
print("Total caracteres escritos:", total_caracteres)
print("Sesión finalizada.")
```

</details>

---

*Estos ejercicios cubren los conceptos de `print()`, `input()`, comentarios, indentación, secuencia de instrucciones y buenas prácticas. Los ejercicios 9 y 10 introducen además conversión de tipos (`float()`) y la función `len()`, anticipando los contenidos de la clase del viernes.*
