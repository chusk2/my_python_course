# Ejercicios — Viernes 10/04: Variables, Tipos de Datos y Conversión entre Tipos

---

## Ejercicios Básicos (1–5)

---

### Ejercicio 1: Inspector de tipos

Crea variables con los siguientes valores y muestra en pantalla el valor y su tipo usando `type()`:

- Un número entero (tu edad)
- Un número decimal (tu altura en metros)
- Una cadena de texto (tu nombre)
- Un booleano (si tienes mascota o no)
- Un valor `None`

**Ejemplo de salida:**
```
Valor: 28 - Tipo: <class 'int'>
Valor: 1.75 - Tipo: <class 'float'>
Valor: Laura - Tipo: <class 'str'>
Valor: True - Tipo: <class 'bool'>
Valor: None - Tipo: <class 'NoneType'>
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 1: Inspector de tipos
# Creamos variables de distintos tipos
edad = 28
altura = 1.75
nombre = "Laura"
tiene_mascota = True
dato_pendiente = None

# Mostramos cada valor con su tipo
print("Valor:", edad, "- Tipo:", type(edad))
print("Valor:", altura, "- Tipo:", type(altura))
print("Valor:", nombre, "- Tipo:", type(nombre))
print("Valor:", tiene_mascota, "- Tipo:", type(tiene_mascota))
print("Valor:", dato_pendiente, "- Tipo:", type(dato_pendiente))
```

</details>

---

### Ejercicio 2: Conversor de kilómetros a millas

Pide al usuario una distancia en kilómetros y conviértela a millas (1 km = 0.621371 millas). Muestra el resultado con 2 decimales usando un f-string.

**Ejemplo de interacción:**
```
Distancia en kilómetros: 100
100.0 km equivalen a 62.14 millas
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 2: Conversor de kilómetros a millas
# Factor de conversión
FACTOR_KM_A_MILLAS = 0.621371

# Pedimos la distancia y la convertimos a número decimal
km = float(input("Distancia en kilómetros: "))

# Calculamos las millas
millas = km * FACTOR_KM_A_MILLAS

# Mostramos el resultado con 2 decimales
print(f"{km} km equivalen a {millas:.2f} millas")
```

</details>

---

### Ejercicio 3: Intercambio de variables

Crea dos variables `a` y `b` con valores que el usuario introduzca. Muestra sus valores, intercámbialos (que `a` tenga el valor de `b` y viceversa) y muestra el resultado.

**Pista**: Python permite hacer `a, b = b, a`.

**Ejemplo de interacción:**
```
Valor de a: Hola
Valor de b: Mundo
Antes del intercambio: a = Hola, b = Mundo
Después del intercambio: a = Mundo, b = Hola
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 3: Intercambio de variables
# Recogemos los valores
a = input("Valor de a: ")
b = input("Valor de b: ")

# Mostramos los valores originales
print(f"Antes del intercambio: a = {a}, b = {b}")

# Intercambiamos los valores (forma Pythónica)
a, b = b, a

# Mostramos los valores después del intercambio
print(f"Después del intercambio: a = {a}, b = {b}")
```

</details>

---

### Ejercicio 4: Verificador de tipos de `input()`

Escribe un programa que pida al usuario un número. Sin convertirlo, muestra su tipo (será `str`). Luego conviértelo a `int` y a `float`, y muestra el tipo de cada conversión. Este ejercicio demuestra que `input()` siempre devuelve texto.

**Ejemplo de interacción:**
```
Escribe un número: 42
Tal como lo recoge input(): '42' -> <class 'str'>
Convertido a entero: 42 -> <class 'int'>
Convertido a decimal: 42.0 -> <class 'float'>
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 4: Verificador de tipos de input()
# Recogemos un dato del usuario
dato = input("Escribe un número: ")

# Mostramos el tipo original (siempre str)
print(f"Tal como lo recoge input(): '{dato}' -> {type(dato)}")

# Convertimos a int y mostramos
dato_int = int(dato)
print(f"Convertido a entero: {dato_int} -> {type(dato_int)}")

# Convertimos a float y mostramos
dato_float = float(dato)
print(f"Convertido a decimal: {dato_float} -> {type(dato_float)}")
```

</details>

---

### Ejercicio 5: Cálculo de edad

Pide al usuario su año de nacimiento. Calcula su edad aproximada (restando al año actual, 2026) y muestra un mensaje indicando la edad y si es mayor de edad o no.

**Ejemplo de interacción:**
```
¿En qué año naciste? 1995
Tienes aproximadamente 31 años.
Eres mayor de edad: True
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 5: Cálculo de edad
# Año actual (lo definimos como constante)
ANIO_ACTUAL = 2026

# Pedimos el año de nacimiento y lo convertimos a entero
anio_nacimiento = int(input("¿En qué año naciste? "))

# Calculamos la edad aproximada
edad = ANIO_ACTUAL - anio_nacimiento

# Determinamos si es mayor de edad (resultado booleano)
es_mayor_de_edad = edad >= 18

# Mostramos los resultados
print(f"Tienes aproximadamente {edad} años.")
print(f"Eres mayor de edad: {es_mayor_de_edad}")
```

</details>

---

## Ejercicios de Nivel Medio (6–8)

---

### Ejercicio 6: Desglose de billetes y monedas

Pide al usuario una cantidad de dinero en euros (número entero) y calcula cuántos billetes de 50€, 20€, 10€ y 5€ y monedas de 2€ y 1€ se necesitan para formar esa cantidad, usando el menor número de billetes y monedas posible.

**Pista**: Usa la división entera (`//`) y el módulo (`%`).

**Ejemplo de interacción:**
```
Introduce una cantidad en euros: 187
Desglose de 187 €:
  Billetes de 50€: 3
  Billetes de 20€: 1
  Billetes de 10€: 1
  Billetes de 5€:  1
  Monedas de 2€:   1
  Monedas de 1€:   0
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 6: Desglose de billetes y monedas
# Recogemos la cantidad y la convertimos a entero
cantidad = int(input("Introduce una cantidad en euros: "))

# Guardamos la cantidad original para mostrarla al final
cantidad_original = cantidad

# Calculamos el desglose de mayor a menor
billetes_50 = cantidad // 50
cantidad = cantidad % 50       # Lo que sobra tras sacar billetes de 50

billetes_20 = cantidad // 20
cantidad = cantidad % 20

billetes_10 = cantidad // 10
cantidad = cantidad % 10

billetes_5 = cantidad // 5
cantidad = cantidad % 5

monedas_2 = cantidad // 2
cantidad = cantidad % 2

monedas_1 = cantidad           # Lo que queda son monedas de 1€

# Mostramos el resultado
print(f"Desglose de {cantidad_original} €:")
print(f"  Billetes de 50€: {billetes_50}")
print(f"  Billetes de 20€: {billetes_20}")
print(f"  Billetes de 10€: {billetes_10}")
print(f"  Billetes de 5€:  {billetes_5}")
print(f"  Monedas de 2€:   {monedas_2}")
print(f"  Monedas de 1€:   {monedas_1}")
```

</details>

---

### Ejercicio 7: Calculadora de consumo de combustible

Pide al usuario los kilómetros recorridos, los litros de combustible consumidos y el precio por litro. Calcula y muestra: consumo medio (litros/100 km), coste total del viaje y coste por kilómetro. Usa f-strings para formatear todos los resultados a 2 decimales.

**Ejemplo de interacción:**
```
Kilómetros recorridos: 450
Litros consumidos: 32.5
Precio por litro (€): 1.65

=== RESUMEN DEL VIAJE ===
Distancia:           450.00 km
Combustible:         32.50 litros
Consumo medio:       7.22 L/100km
Coste total:         53.63 €
Coste por kilómetro: 0.12 €/km
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 7: Calculadora de consumo de combustible
# Recogemos los datos del viaje
km = float(input("Kilómetros recorridos: "))
litros = float(input("Litros consumidos: "))
precio_litro = float(input("Precio por litro (€): "))

# Realizamos los cálculos
consumo_medio = (litros / km) * 100      # Litros por cada 100 km
coste_total = litros * precio_litro       # Coste total del combustible
coste_por_km = coste_total / km           # Coste por kilómetro

# Mostramos el resumen con f-strings y 2 decimales
print()
print("=== RESUMEN DEL VIAJE ===")
print(f"Distancia:           {km:.2f} km")
print(f"Combustible:         {litros:.2f} litros")
print(f"Consumo medio:       {consumo_medio:.2f} L/100km")
print(f"Coste total:         {coste_total:.2f} €")
print(f"Coste por kilómetro: {coste_por_km:.2f} €/km")
```

</details>

---

### Ejercicio 8: Conversor de unidades de almacenamiento digital

Pide al usuario una cantidad en **gigabytes (GB)** y convierte esa cantidad a megabytes (MB), kilobytes (KB), bytes y terabytes (TB). Muestra los resultados formateados. Recuerda: 1 GB = 1024 MB, 1 MB = 1024 KB, 1 KB = 1024 Bytes, 1 TB = 1024 GB.

**Ejemplo de interacción:**
```
Cantidad en GB: 4.5

=== CONVERSIÓN DE ALMACENAMIENTO ===
Terabytes (TB):   0.004395 TB
Gigabytes (GB):   4.500000 GB
Megabytes (MB):   4608.00 MB
Kilobytes (KB):   4718592.00 KB
Bytes (B):        4831838208.00 B
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 8: Conversor de unidades de almacenamiento digital
# Recogemos la cantidad en GB
gb = float(input("Cantidad en GB: "))

# Realizamos las conversiones
tb = gb / 1024                    # GB a Terabytes
mb = gb * 1024                    # GB a Megabytes
kb = mb * 1024                    # MB a Kilobytes
bytes_total = kb * 1024           # KB a Bytes

# Mostramos los resultados
print()
print("=== CONVERSIÓN DE ALMACENAMIENTO ===")
print(f"Terabytes (TB):   {tb:.6f} TB")
print(f"Gigabytes (GB):   {gb:.6f} GB")
print(f"Megabytes (MB):   {mb:.2f} MB")
print(f"Kilobytes (KB):   {kb:.2f} KB")
print(f"Bytes (B):        {bytes_total:.2f} B")
```

</details>

---

## Ejercicios de Nivel Superior (9–10)

---

### Ejercicio 9: Simulador de presupuesto personal

Crea un programa que funcione como un planificador de presupuesto mensual sencillo. Debe pedir al usuario:

- Su salario neto mensual
- Gasto fijo en alquiler/hipoteca
- Gasto fijo en suministros (luz, agua, gas, internet)
- Gasto estimado en alimentación
- Gasto estimado en transporte

El programa debe calcular y mostrar: el total de gastos, el dinero restante, el porcentaje del salario que va a cada concepto y si el usuario tiene superávit o déficit. Usa `type()` para verificar al menos una conversión y f-strings para todo el formato.

**Ejemplo de salida:**
```
=== PLANIFICADOR DE PRESUPUESTO MENSUAL ===
Salario neto mensual (€): 1800
Alquiler/Hipoteca (€): 650
Suministros (€): 120
Alimentación (€): 350
Transporte (€): 80

========================================
       RESUMEN DE PRESUPUESTO
========================================
Ingresos:                 1800.00 €
----------------------------------------
Alquiler/Hipoteca:   650.00 € (36.11%)
Suministros:         120.00 € ( 6.67%)
Alimentación:        350.00 € (19.44%)
Transporte:           80.00 € ( 4.44%)
----------------------------------------
Total gastos:        1200.00 € (66.67%)
Disponible:           600.00 € (33.33%)
========================================
Resultado: SUPERÁVIT
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 9: Simulador de presupuesto personal
# Recogemos los datos de ingresos y gastos
print("=== PLANIFICADOR DE PRESUPUESTO MENSUAL ===")
salario = float(input("Salario neto mensual (€): "))
alquiler = float(input("Alquiler/Hipoteca (€): "))
suministros = float(input("Suministros (€): "))
alimentacion = float(input("Alimentación (€): "))
transporte = float(input("Transporte (€): "))

# Calculamos totales
total_gastos = alquiler + suministros + alimentacion + transporte
disponible = salario - total_gastos

# Calculamos porcentajes (sobre el salario)
pct_alquiler = (alquiler / salario) * 100
pct_suministros = (suministros / salario) * 100
pct_alimentacion = (alimentacion / salario) * 100
pct_transporte = (transporte / salario) * 100
pct_gastos = (total_gastos / salario) * 100
pct_disponible = (disponible / salario) * 100

# Verificamos el tipo de una variable (como pide el ejercicio)
print(f"\n[Verificación] Tipo de 'salario': {type(salario)}")

# Determinamos si hay superávit o déficit
# (disponible >= 0 devuelve un booleano, lo usamos para elegir texto)
es_superavit = disponible >= 0
resultado = "SUPERÁVIT" if es_superavit else "DÉFICIT"

# Mostramos el resumen
print()
print("=" * 42)
print("       RESUMEN DE PRESUPUESTO")
print("=" * 42)
print(f"Ingresos:            {salario:>10.2f} €")
print("-" * 42)
print(f"Alquiler/Hipoteca:   {alquiler:>7.2f} € ({pct_alquiler:>5.2f}%)")
print(f"Suministros:         {suministros:>7.2f} € ({pct_suministros:>5.2f}%)")
print(f"Alimentación:        {alimentacion:>7.2f} € ({pct_alimentacion:>5.2f}%)")
print(f"Transporte:          {transporte:>7.2f} € ({pct_transporte:>5.2f}%)")
print("-" * 42)
print(f"Total gastos:        {total_gastos:>7.2f} € ({pct_gastos:>5.2f}%)")
print(f"Disponible:          {disponible:>7.2f} € ({pct_disponible:>5.2f}%)")
print("=" * 42)
print(f"Resultado: {resultado}")
```

</details>

---

### Ejercicio 10: Calculadora de hipoteca simplificada

Crea un programa que calcule la cuota mensual de una hipoteca. Debe pedir al usuario:

- Precio de la vivienda
- Porcentaje de entrada (ahorro inicial que aporta el comprador)
- Tipo de interés anual (en porcentaje)
- Plazo en años

El programa debe calcular: el importe de la entrada, el capital a financiar, la cuota mensual (usando la fórmula de amortización francesa) y el total que se pagará al banco incluyendo intereses.

**Fórmula de la cuota mensual:**
```
cuota = capital * (r * (1 + r)^n) / ((1 + r)^n - 1)
```
Donde `r` = tipo de interés mensual (anual / 12 / 100) y `n` = número total de cuotas (años * 12).

**Pista**: Para la potencia usa `**` (por ejemplo, `(1 + r) ** n`).

**Ejemplo de interacción:**
```
=== CALCULADORA DE HIPOTECA ===
Precio de la vivienda (€): 180000
Porcentaje de entrada (%): 20
Tipo de interés anual (%): 3.5
Plazo en años: 25

====================================
     RESUMEN DE LA HIPOTECA
====================================
Precio vivienda:     180000.00 €
Entrada (20.0%):      36000.00 €
Capital a financiar: 144000.00 €
Tipo interés anual:       3.50 %
Plazo:                25 años (300 cuotas)
------------------------------------
Cuota mensual:          720.03 €
Total a pagar:       216009.00 €
Total intereses:      72009.00 €
====================================
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 10: Calculadora de hipoteca simplificada
# Recogemos los datos del usuario
print("=== CALCULADORA DE HIPOTECA ===")
precio_vivienda = float(input("Precio de la vivienda (€): "))
pct_entrada = float(input("Porcentaje de entrada (%): "))
interes_anual = float(input("Tipo de interés anual (%): "))
plazo_anios = int(input("Plazo en años: "))

# Calculamos los valores intermedios
entrada = precio_vivienda * (pct_entrada / 100)
capital = precio_vivienda - entrada

# Convertimos el interés anual a mensual (en tanto por uno)
r = interes_anual / 12 / 100

# Número total de cuotas mensuales
n = plazo_anios * 12

# Fórmula de amortización francesa para la cuota mensual
# cuota = capital * (r * (1+r)^n) / ((1+r)^n - 1)
cuota_mensual = capital * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

# Total pagado al banco y total de intereses
total_pagado = cuota_mensual * n
total_intereses = total_pagado - capital

# Mostramos el resumen completo
print()
print("=" * 38)
print("     RESUMEN DE LA HIPOTECA")
print("=" * 38)
print(f"Precio vivienda:     {precio_vivienda:>10.2f} €")
print(f"Entrada ({pct_entrada}%):   {entrada:>10.2f} €")
print(f"Capital a financiar: {capital:>10.2f} €")
print(f"Tipo interés anual:  {interes_anual:>9.2f} %")
print(f"Plazo:               {plazo_anios:>2} años ({n} cuotas)")
print("-" * 38)
print(f"Cuota mensual:       {cuota_mensual:>10.2f} €")
print(f"Total a pagar:       {total_pagado:>10.2f} €")
print(f"Total intereses:     {total_intereses:>10.2f} €")
print("=" * 38)
```

</details>

---

*Estos ejercicios cubren: variables, tipos de datos (`int`, `float`, `str`, `bool`, `None`), `type()`, conversión de tipos (`int()`, `float()`, `str()`), f-strings, operaciones aritméticas y formateo de salida. Los ejercicios 9 y 10 integran todos los conceptos de la semana, incluyendo `input()`, `print()`, buenas prácticas de nombres y comentarios.*
