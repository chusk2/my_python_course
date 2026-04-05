# Ejercicios — Martes 14/04: Estructuras Condicionales

---

## Ejercicios Básicos (1–5)

---

### Ejercicio 1: Mayor de edad

Pide la edad del usuario y muestra si es mayor o menor de edad.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 1: Mayor de edad
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
```

</details>

---

### Ejercicio 2: Número positivo, negativo o cero

Pide un número y muestra si es positivo, negativo o cero.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 2: Positivo, negativo o cero
numero = float(input("Introduce un número: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
```

</details>

---

### Ejercicio 3: Calificación por nota

Pide una nota del 0 al 10 y muestra la calificación: Suspenso (0-4.99), Aprobado (5-6.99), Notable (7-8.99), Sobresaliente (9-10).

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 3: Calificación por nota
nota = float(input("Introduce tu nota (0-10): "))

if nota < 0 or nota > 10:
    print("Error: la nota debe estar entre 0 y 10.")
elif nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

</details>

---

### Ejercicio 4: Calculadora simple

Pide dos números y una operación (+, -, *, /). Realiza la operación indicada y muestra el resultado. Si la operación es `/` y el segundo número es 0, muestra un error.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 4: Calculadora simple
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
operacion = input("Operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operacion == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operacion == "/":
    if num2 == 0:
        print("Error: no se puede dividir entre cero.")
    else:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado:.2f}")
else:
    print("Operación no reconocida.")
```

</details>

---

### Ejercicio 5: Día de la semana

Pide un número del 1 al 7 y muestra el día de la semana correspondiente (1=Lunes, 7=Domingo). Si el número no está en ese rango, muestra un error.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 5: Día de la semana
dia = int(input("Introduce un número del 1 al 7: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Error: el número debe estar entre 1 y 7.")
```

</details>

---

## Ejercicios de Nivel Medio (6–8)

---

### Ejercicio 6: Tarifa eléctrica por franjas horarias

Simula el cálculo del coste eléctrico según la franja horaria. Pide al usuario la hora (0-23) y los kWh consumidos. Las tarifas son:

- Valle (0-7): 0.08 €/kWh
- Llano (8-9, 14-17, 22-23): 0.14 €/kWh
- Punta (10-13, 18-21): 0.22 €/kWh

Muestra la franja, la tarifa aplicada y el coste total.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 6: Tarifa eléctrica por franjas horarias
hora = int(input("Hora del consumo (0-23): "))
kwh = float(input("kWh consumidos: "))

# Determinamos la franja horaria
if hora < 0 or hora > 23:
    print("Error: la hora debe estar entre 0 y 23.")
elif hora <= 7:
    franja = "Valle"
    tarifa = 0.08
elif hora <= 9:
    franja = "Llano"
    tarifa = 0.14
elif hora <= 13:
    franja = "Punta"
    tarifa = 0.22
elif hora <= 17:
    franja = "Llano"
    tarifa = 0.14
elif hora <= 21:
    franja = "Punta"
    tarifa = 0.22
else:
    franja = "Llano"
    tarifa = 0.14

# Mostramos el resultado (solo si la hora era válida)
if 0 <= hora <= 23:
    coste = kwh * tarifa
    print()
    print(f"Hora: {hora}:00")
    print(f"Franja: {franja}")
    print(f"Tarifa: {tarifa:.2f} €/kWh")
    print(f"Consumo: {kwh:.2f} kWh")
    print(f"Coste: {coste:.2f} €")
```

</details>

---

### Ejercicio 7: Clasificador de triángulos

Pide al usuario los tres lados de un triángulo. Primero, verifica que los lados formen un triángulo válido (la suma de dos lados cualesquiera debe ser mayor que el tercero). Si es válido, clasifícalo como equilátero (3 lados iguales), isósceles (2 lados iguales) o escaleno (3 lados diferentes).

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 7: Clasificador de triángulos
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

# Verificamos que los lados formen un triángulo válido
# La suma de dos lados cualesquiera debe ser mayor que el tercero
es_valido = (a + b > c) and (a + c > b) and (b + c > a)

# También verificamos que todos los lados sean positivos
lados_positivos = a > 0 and b > 0 and c > 0

if not lados_positivos:
    print("Error: todos los lados deben ser mayores que cero.")
elif not es_valido:
    print("Estos lados no forman un triángulo válido.")
else:
    # Clasificamos el triángulo
    if a == b == c:
        tipo = "equilátero"
    elif a == b or a == c or b == c:
        tipo = "isósceles"
    else:
        tipo = "escaleno"

    print(f"Es un triángulo {tipo}.")
```

</details>

---

### Ejercicio 8: Diagnóstico de red simplificado

Simula un sistema de diagnóstico de red. Pide al usuario tres datos booleanos (s/n): si hay conexión a Internet, si el servidor responde y si el certificado SSL es válido. Según la combinación, muestra un diagnóstico:

- Todo correcto → "Conexión segura establecida"
- Sin Internet → "Error: sin conexión a Internet"
- Internet OK pero servidor no responde → "Error: servidor no disponible"
- Internet y servidor OK pero SSL inválido → "Advertencia: conexión no segura"

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 8: Diagnóstico de red simplificado
print("=== DIAGNÓSTICO DE RED ===")
internet = input("¿Hay conexión a Internet? (s/n): ").lower() == "s"
servidor = input("¿El servidor responde? (s/n): ").lower() == "s"
ssl_valido = input("¿Certificado SSL válido? (s/n): ").lower() == "s"

print()
print("--- Resultado ---")

# Evaluamos las condiciones en orden lógico
if not internet:
    print("ERROR: Sin conexión a Internet.")
    print("  → Comprueba tu router y cable de red.")
elif not servidor:
    print("ERROR: Servidor no disponible.")
    print("  → El servidor puede estar en mantenimiento.")
elif not ssl_valido:
    print("ADVERTENCIA: Conexión no segura.")
    print("  → El certificado SSL ha expirado o no es válido.")
else:
    print("OK: Conexión segura establecida.")
    print("  → Todos los sistemas funcionan correctamente.")

# Resumen de estado
print()
print("--- Estado de componentes ---")
print(f"  Internet:  {'✓' if internet else '✗'}")
print(f"  Servidor:  {'✓' if servidor else '✗'}")
print(f"  SSL:       {'✓' if ssl_valido else '✗'}")
```

</details>

---

## Ejercicios de Nivel Superior (9–10)

---

### Ejercicio 9: Cajero automático

Simula un cajero automático. El usuario tiene un saldo inicial de 1000€. El programa muestra un menú con 4 opciones: consultar saldo, ingresar dinero, retirar dinero y salir. Para retirar dinero, debe verificar que hay saldo suficiente. El programa solo ejecuta UNA operación (no es un bucle todavía, eso lo veremos el jueves). Usa condicionales, operadores de comparación, asignación compuesta, conversión de tipos y f-strings.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 9: Cajero automático (una operación)
saldo = 1000.00

print("=" * 35)
print("    CAJERO AUTOMÁTICO")
print("=" * 35)
print(f"Bienvenido. Su saldo actual: {saldo:.2f} €")
print()
print("1. Consultar saldo")
print("2. Ingresar dinero")
print("3. Retirar dinero")
print("4. Salir")
print()

opcion = input("Seleccione una opción: ").strip()

if opcion == "1":
    # Consultar saldo
    print(f"\nSu saldo actual es: {saldo:.2f} €")

elif opcion == "2":
    # Ingresar dinero
    cantidad = float(input("Cantidad a ingresar (€): "))
    if cantidad <= 0:
        print("Error: la cantidad debe ser positiva.")
    else:
        saldo += cantidad
        print(f"Ingreso realizado. Nuevo saldo: {saldo:.2f} €")

elif opcion == "3":
    # Retirar dinero
    cantidad = float(input("Cantidad a retirar (€): "))
    if cantidad <= 0:
        print("Error: la cantidad debe ser positiva.")
    elif cantidad > saldo:
        print(f"Error: saldo insuficiente. Saldo actual: {saldo:.2f} €")
    else:
        saldo -= cantidad
        print(f"Retirada realizada. Nuevo saldo: {saldo:.2f} €")

elif opcion == "4":
    print("Gracias por usar el cajero. ¡Hasta pronto!")

else:
    print("Opción no válida.")
```

</details>

---

### Ejercicio 10: Calculadora de impuestos para autónomos

Crea un programa que calcule los impuestos trimestrales simplificados de un autónomo. Pide: ingresos del trimestre, gastos deducibles del trimestre y si es su primer año de actividad (tiene bonificación). Calcula:

1. Beneficio = Ingresos - Gastos
2. Si el beneficio es negativo, no hay impuestos pero se guarda la pérdida.
3. IVA a ingresar = Ingresos × 21% - Gastos × 21% (IVA repercutido - IVA soportado)
4. IRPF = Beneficio × 20% (si es primer año, solo 7% por la tarifa plana de autónomos nuevos)
5. Cuota de autónomos mensual: 80€ si es primer año, 300€ si no.
6. Total trimestral de cuota de autónomos = cuota mensual × 3.

Muestra un resumen completo con todos los conceptos. Integra condicionales, operadores de todo tipo, f-strings y conversión de tipos.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 10: Calculadora de impuestos para autónomos
print("=== CALCULADORA TRIMESTRAL DE AUTÓNOMOS ===")
ingresos = float(input("Ingresos del trimestre (€): "))
gastos = float(input("Gastos deducibles del trimestre (€): "))
primer_anio = input("¿Es tu primer año de actividad? (s/n): ").lower() == "s"

# Cálculos
beneficio = ingresos - gastos

# IVA: repercutido (cobrado) - soportado (pagado)
iva_repercutido = ingresos * 0.21
iva_soportado = gastos * 0.21
iva_a_ingresar = iva_repercutido - iva_soportado

# IRPF: depende de si es primer año
if primer_anio:
    pct_irpf = 7
    cuota_autonomo_mensual = 80.0
else:
    pct_irpf = 20
    cuota_autonomo_mensual = 300.0

# El IRPF solo se calcula si hay beneficio positivo
if beneficio > 0:
    irpf = beneficio * (pct_irpf / 100)
else:
    irpf = 0.0

# Cuota de autónomos trimestral
cuota_autonomo_trimestral = cuota_autonomo_mensual * 3

# Total a pagar este trimestre (impuestos + cuota autónomos)
total_impuestos = iva_a_ingresar + irpf + cuota_autonomo_trimestral

# Resultado neto del trimestre
neto_trimestral = beneficio - irpf - cuota_autonomo_trimestral

# Mostramos el resumen
print()
print("=" * 48)
print("      RESUMEN TRIMESTRAL")
print("=" * 48)
print(f"Ingresos:                    {ingresos:>10.2f} €")
print(f"Gastos deducibles:          -{gastos:>10.2f} €")
print(f"-" * 48)
print(f"Beneficio bruto:             {beneficio:>10.2f} €")

if beneficio < 0:
    print("  (Trimestre con pérdidas)")

print()
print("  --- IVA ---")
print(f"  IVA repercutido (21%):     {iva_repercutido:>10.2f} €")
print(f"  IVA soportado (21%):      -{iva_soportado:>10.2f} €")
print(f"  IVA a ingresar:            {iva_a_ingresar:>10.2f} €")

print()
print("  --- IRPF ---")
print(f"  Tipo aplicado:             {pct_irpf}%", end="")
if primer_anio:
    print(" (tarifa plana nuevo autónomo)")
else:
    print()
print(f"  Retención IRPF:            {irpf:>10.2f} €")

print()
print("  --- Cuota de autónomos ---")
print(f"  Cuota mensual:             {cuota_autonomo_mensual:>10.2f} €")
print(f"  Cuota trimestral (×3):     {cuota_autonomo_trimestral:>10.2f} €")

print()
print("=" * 48)
print(f"TOTAL IMPUESTOS TRIMESTRE:   {total_impuestos:>10.2f} €")
print(f"RESULTADO NETO TRIMESTRE:    {neto_trimestral:>10.2f} €")
print("=" * 48)

if neto_trimestral > 0:
    print("Resultado: BENEFICIO NETO POSITIVO")
else:
    print("Resultado: RESULTADO NEGATIVO — Revisa tus gastos")
```

</details>

---

*Estos ejercicios integran condicionales (`if`, `elif`, `else`), operadores (aritméticos, de comparación, lógicos), conversión de tipos, f-strings y buenas prácticas de la Semana 1.*
