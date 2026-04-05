# Ejercicios — Jueves 16/04: Bucles, Control de Flujo y Depuración

---

## Ejercicios Básicos (1–5)

---

### Ejercicio 1: Tabla de multiplicar

Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10 usando un bucle `for`.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 1: Tabla de multiplicar
numero = int(input("¿De qué número quieres la tabla? "))

print(f"\n--- Tabla del {numero} ---")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
```

</details>

---

### Ejercicio 2: Suma de números

Pide al usuario cuántos números quiere introducir. Luego, pide esos números uno a uno con un bucle `for` y muestra la suma total y la media.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 2: Suma de números
cantidad = int(input("¿Cuántos números quieres introducir? "))

total = 0
for i in range(1, cantidad + 1):
    numero = float(input(f"Número {i}: "))
    total += numero

media = total / cantidad if cantidad > 0 else 0

print(f"\nSuma total: {total:.2f}")
print(f"Media: {media:.2f}")
```

</details>

---

### Ejercicio 3: Cuenta atrás

Pide un número al usuario y muestra una cuenta atrás desde ese número hasta 0, usando un bucle `while`. Al llegar a 0, muestra "¡Despegue!".

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 3: Cuenta atrás
numero = int(input("Introduce un número para la cuenta atrás: "))

while numero > 0:
    print(numero)
    numero -= 1

print("¡Despegue!")
```

</details>

---

### Ejercicio 4: Validación de entrada

Pide al usuario un número entre 1 y 100. Si introduce algo fuera de rango, muestra un error y vuelve a pedirlo. Usa un bucle `while` para repetir hasta que la entrada sea válida.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 4: Validación de entrada con while
numero = 0  # Valor inicial fuera del rango válido

while numero < 1 or numero > 100:
    numero = int(input("Introduce un número entre 1 y 100: "))
    if numero < 1 or numero > 100:
        print("Error: el número debe estar entre 1 y 100.")

print(f"Número válido: {numero}")
```

</details>

---

### Ejercicio 5: Números pares con `continue`

Usa un bucle `for` del 1 al 20. Con `continue`, salta los números impares y muestra solo los pares.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 5: Solo pares con continue
print("Números pares del 1 al 20:")
for i in range(1, 21):
    if i % 2 != 0:
        continue  # Si es impar, saltamos a la siguiente vuelta
    print(i, end=" ")

print()  # Salto de línea final
```

</details>

---

## Ejercicios de Nivel Medio (6–8)

---

### Ejercicio 6: Cajero automático con menú

Mejora el cajero automático del ejercicio del martes: ahora el menú se repite en bucle hasta que el usuario elija "Salir". El saldo se mantiene entre operaciones. Usa `while True` con `break`.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 6: Cajero automático con menú en bucle
saldo = 1000.00

print("=" * 35)
print("    CAJERO AUTOMÁTICO")
print("=" * 35)

while True:
    print(f"\nSaldo actual: {saldo:.2f} €")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("\nSeleccione una opción: ").strip()

    if opcion == "1":
        print(f"Su saldo es: {saldo:.2f} €")

    elif opcion == "2":
        cantidad = float(input("Cantidad a ingresar (€): "))
        if cantidad <= 0:
            print("Error: la cantidad debe ser positiva.")
        else:
            saldo += cantidad
            print(f"Ingreso realizado. Nuevo saldo: {saldo:.2f} €")

    elif opcion == "3":
        cantidad = float(input("Cantidad a retirar (€): "))
        if cantidad <= 0:
            print("Error: la cantidad debe ser positiva.")
        elif cantidad > saldo:
            print(f"Error: saldo insuficiente.")
        else:
            saldo -= cantidad
            print(f"Retirada realizada. Nuevo saldo: {saldo:.2f} €")

    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida.")
```

</details>

---

### Ejercicio 7: Detector de números primos

Pide un número al usuario y determina si es primo. Un número primo solo es divisible entre 1 y sí mismo. Usa un bucle `for` para comprobar divisores y `break` si encuentras alguno.

**Pista**: Solo necesitas comprobar divisores desde 2 hasta la raíz cuadrada del número. Puedes usar `int(numero ** 0.5) + 1` como límite.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 7: Detector de números primos
numero = int(input("Introduce un número: "))

if numero < 2:
    print(f"{numero} no es primo.")
else:
    es_primo = True
    # Solo comprobamos divisores hasta la raíz cuadrada
    limite = int(numero ** 0.5) + 1

    for divisor in range(2, limite):
        if numero % divisor == 0:
            es_primo = False
            print(f"{numero} no es primo (es divisible entre {divisor}).")
            break

    if es_primo:
        print(f"{numero} es primo.")
```

</details>

---

### Ejercicio 8: Control de asistencia con estadísticas

Simula un sistema de control de asistencia. Pide el número de alumnos del curso. Para cada alumno, pide su nombre y si ha asistido (s/n). Al final, muestra un resumen con: total de asistentes, total de ausentes, porcentaje de asistencia y la lista de ausentes.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 8: Control de asistencia
num_alumnos = int(input("Número de alumnos del curso: "))

asistentes = 0
ausentes = 0
lista_ausentes = ""  # Guardamos los nombres (aún no sabemos listas)

print()
for i in range(1, num_alumnos + 1):
    nombre = input(f"Nombre del alumno {i}: ")
    asistio = input(f"  ¿Ha asistido {nombre}? (s/n): ").lower()

    if asistio == "s":
        asistentes += 1
    else:
        ausentes += 1
        # Acumulamos nombres de ausentes separados por coma
        if lista_ausentes:
            lista_ausentes += ", " + nombre
        else:
            lista_ausentes = nombre

# Calculamos porcentaje
pct_asistencia = (asistentes / num_alumnos) * 100 if num_alumnos > 0 else 0

# Mostramos el resumen
print()
print("=" * 35)
print("   RESUMEN DE ASISTENCIA")
print("=" * 35)
print(f"Total alumnos:    {num_alumnos}")
print(f"Asistentes:       {asistentes}")
print(f"Ausentes:         {ausentes}")
print(f"% Asistencia:     {pct_asistencia:.1f}%")
if lista_ausentes:
    print(f"Alumnos ausentes: {lista_ausentes}")
else:
    print("¡Asistencia completa!")
```

</details>

---

## Ejercicios de Nivel Superior (9–10)

---

### Ejercicio 9: Generador de patrones y figuras

Crea un programa con un menú que permita al usuario generar diferentes patrones usando bucles anidados:

1. Triángulo rectángulo de asteriscos (N filas)
2. Triángulo invertido
3. Cuadrado hueco
4. Pirámide centrada

El usuario elige el patrón y su tamaño. El menú se repite hasta que decida salir. Este ejercicio practica bucles anidados, `range()` con diferentes parámetros, y control de flujo.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 9: Generador de patrones
while True:
    print("\n=== GENERADOR DE PATRONES ===")
    print("1. Triángulo rectángulo")
    print("2. Triángulo invertido")
    print("3. Cuadrado hueco")
    print("4. Pirámide centrada")
    print("5. Salir")

    opcion = input("\nElige un patrón: ").strip()

    if opcion == "5":
        print("¡Hasta pronto!")
        break

    if opcion not in ("1", "2", "3", "4"):
        print("Opción no válida.")
        continue

    n = int(input("Tamaño (número de filas): "))

    print()

    if opcion == "1":
        # Triángulo rectángulo
        for i in range(1, n + 1):
            print("*" * i)

    elif opcion == "2":
        # Triángulo invertido
        for i in range(n, 0, -1):
            print("*" * i)

    elif opcion == "3":
        # Cuadrado hueco
        for i in range(n):
            if i == 0 or i == n - 1:
                # Primera y última fila: todo asteriscos
                print("*" * n)
            else:
                # Filas intermedias: asterisco, espacios, asterisco
                print("*" + " " * (n - 2) + "*")

    elif opcion == "4":
        # Pirámide centrada
        for i in range(1, n + 1):
            espacios = " " * (n - i)
            asteriscos = "*" * (2 * i - 1)
            print(espacios + asteriscos)
```

</details>

---

### Ejercicio 10: Análisis de ventas semanales

Simula el registro de ventas de una tienda durante una semana. Para cada día (lunes a domingo), pide el importe de ventas. El programa debe ir mostrando estadísticas actualizadas tras cada día: total acumulado, media diaria hasta el momento, mejor día y peor día. Al final, muestra un informe completo con todos los datos. Integra bucles, condicionales, operadores de comparación, acumuladores y f-strings.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 10: Análisis de ventas semanales
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

total = 0.0
mejor_venta = 0.0
peor_venta = None
mejor_dia = ""
peor_dia = ""

# Guardamos las ventas de cada día como texto (aún no usamos listas formalmente)
resumen = ""

print("=== REGISTRO DE VENTAS SEMANALES ===\n")

for i in range(7):
    dia_actual = dias[i]
    venta = float(input(f"Ventas del {dia_actual} (€): "))

    # Acumulamos
    total += venta
    dias_transcurridos = i + 1
    media = total / dias_transcurridos

    # Actualizamos mejor día
    if venta > mejor_venta:
        mejor_venta = venta
        mejor_dia = dia_actual

    # Actualizamos peor día
    if peor_venta is None or venta < peor_venta:
        peor_venta = venta
        peor_dia = dia_actual

    # Guardamos para el resumen
    resumen += f"  {dia_actual:12s} {venta:>10.2f} €\n"

    # Mostramos estadísticas parciales
    print(f"  → Acumulado: {total:.2f} € | Media: {media:.2f} € | "
          f"Mejor: {mejor_dia} ({mejor_venta:.2f} €)")
    print()

# Informe final
media_final = total / 7
objetivo_semanal = 5000  # Objetivo ficticio
cumple_objetivo = total >= objetivo_semanal

print("=" * 45)
print("      INFORME SEMANAL DE VENTAS")
print("=" * 45)
print(resumen)
print("-" * 45)
print(f"Total semanal:       {total:>10.2f} €")
print(f"Media diaria:        {media_final:>10.2f} €")
print(f"Mejor día:           {mejor_dia} ({mejor_venta:.2f} €)")
print(f"Peor día:            {peor_dia} ({peor_venta:.2f} €)")
print(f"Diferencia max-min:  {mejor_venta - peor_venta:>10.2f} €")
print(f"Objetivo semanal:    {objetivo_semanal:.2f} €")
print(f"¿Objetivo cumplido?: {'SÍ' if cumple_objetivo else 'NO'}")
print("=" * 45)
```

</details>

---

*Estos ejercicios integran `for`, `while`, `break`, `continue`, `range()`, bucles anidados, acumuladores, contadores, condicionales y todos los operadores de las sesiones anteriores.*
