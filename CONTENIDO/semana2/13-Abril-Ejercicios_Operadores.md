# Ejercicios — Lunes 13/04: Operadores y Construcción de Expresiones

---

## Ejercicios Básicos (1–5)

---

### Ejercicio 1: Calculadora de operaciones básicas

Pide al usuario dos números y muestra el resultado de todas las operaciones aritméticas: suma, resta, multiplicación, división, división entera, módulo y potencia.

**Ejemplo de interacción:**
```
Primer número: 17
Segundo número: 5
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.40
17 // 5 = 3
17 % 5 = 2
17 ** 5 = 1419857
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 1: Calculadora de operaciones básicas
a = float(input("Primer número: "))
b = float(input("Segundo número: "))

# Mostramos cada operación
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
```

</details>

---

### Ejercicio 2: Detector de números pares e impares

Pide al usuario un número entero y, usando el operador módulo (`%`), muestra si es par o impar. Muestra también el resultado booleano directamente.

**Ejemplo de interacción:**
```
Introduce un número: 13
¿Es par? False
¿Es impar? True
El número 13 es impar.
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 2: Detector de pares e impares
numero = int(input("Introduce un número: "))

# El módulo 2 devuelve 0 si es par, 1 si es impar
es_par = numero % 2 == 0
es_impar = not es_par

print(f"¿Es par? {es_par}")
print(f"¿Es impar? {es_impar}")

# Mostramos el mensaje usando una expresión condicional simple
tipo = "par" if es_par else "impar"
print(f"El número {numero} es {tipo}.")
```

</details>

---

### Ejercicio 3: Comparador de edades

Pide la edad de dos personas y muestra quién es mayor, quién es menor, y si tienen la misma edad. Usa operadores de comparación.

**Ejemplo de interacción:**
```
Edad de la primera persona: 28
Edad de la segunda persona: 35
¿Persona 1 es mayor que Persona 2? False
¿Persona 1 es menor que Persona 2? True
¿Tienen la misma edad? False
Diferencia de edad: 7 años
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 3: Comparador de edades
edad1 = int(input("Edad de la primera persona: "))
edad2 = int(input("Edad de la segunda persona: "))

# Comparaciones
print(f"¿Persona 1 es mayor que Persona 2? {edad1 > edad2}")
print(f"¿Persona 1 es menor que Persona 2? {edad1 < edad2}")
print(f"¿Tienen la misma edad? {edad1 == edad2}")

# Calculamos la diferencia (valor absoluto para evitar negativos)
diferencia = abs(edad1 - edad2)
print(f"Diferencia de edad: {diferencia} años")
```

</details>

---

### Ejercicio 4: Validador de contraseña simple

Pide al usuario una contraseña y comprueba si cumple tres requisitos usando operadores lógicos: tiene al menos 8 caracteres, contiene al menos un número (usa `any(c.isdigit() for c in password)` como expresión) y no está vacía. Muestra cada comprobación y si la contraseña es válida en conjunto.

**Ejemplo de interacción:**
```
Introduce una contraseña: hola123
¿Tiene al menos 8 caracteres? False
¿Contiene algún número? True
¿No está vacía? True
¿Contraseña válida? False
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 4: Validador de contraseña simple
password = input("Introduce una contraseña: ")

# Comprobamos cada requisito
tiene_longitud = len(password) >= 8
tiene_numero = any(c.isdigit() for c in password)
no_vacia = len(password) > 0

# La contraseña es válida solo si cumple TODOS los requisitos (and)
es_valida = tiene_longitud and tiene_numero and no_vacia

# Mostramos los resultados
print(f"¿Tiene al menos 8 caracteres? {tiene_longitud}")
print(f"¿Contiene algún número? {tiene_numero}")
print(f"¿No está vacía? {no_vacia}")
print(f"¿Contraseña válida? {es_valida}")
```

</details>

---

### Ejercicio 5: Acumulador con asignación compuesta

Simula una caja registradora sencilla: pide el precio de 5 productos uno a uno y ve acumulando el total usando el operador `+=`. Al final muestra el total y el IVA.

**Ejemplo de interacción:**
```
Precio del producto 1: 3.50
Precio del producto 2: 12.00
Precio del producto 3: 1.20
Precio del producto 4: 8.75
Precio del producto 5: 4.30
---
Subtotal: 29.75 €
IVA (21%): 6.25 €
Total: 36.00 €
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 5: Acumulador con asignación compuesta
# Inicializamos el total a 0
total = 0.0

# Pedimos 5 precios y los acumulamos con +=
precio = float(input("Precio del producto 1: "))
total += precio

precio = float(input("Precio del producto 2: "))
total += precio

precio = float(input("Precio del producto 3: "))
total += precio

precio = float(input("Precio del producto 4: "))
total += precio

precio = float(input("Precio del producto 5: "))
total += precio

# Calculamos el IVA y el total final
iva = total * 0.21
total_con_iva = total + iva

# Mostramos el resultado
print("---")
print(f"Subtotal: {total:.2f} €")
print(f"IVA (21%): {iva:.2f} €")
print(f"Total: {total_con_iva:.2f} €")
```

</details>

---

## Ejercicios de Nivel Medio (6–8)

---

### Ejercicio 6: Calculadora de IMC con interpretación

Pide al usuario su peso (kg) y altura (metros). Calcula el Índice de Masa Corporal (IMC = peso / altura²) y muestra la interpretación usando expresiones booleanas. Muestra en qué categoría cae el usuario:

- Bajo peso: IMC < 18.5
- Peso normal: 18.5 ≤ IMC < 25
- Sobrepeso: 25 ≤ IMC < 30
- Obesidad: IMC ≥ 30

**Ejemplo de interacción:**
```
Peso (kg): 75
Altura (m): 1.78
Tu IMC es: 23.67
¿Bajo peso? False
¿Peso normal? True
¿Sobrepeso? False
¿Obesidad? False
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 6: Calculadora de IMC
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

# Calculamos el IMC usando la potencia (**)
imc = peso / (altura ** 2)

# Evaluamos cada rango con operadores de comparación y lógicos
bajo_peso = imc < 18.5
peso_normal = imc >= 18.5 and imc < 25
sobrepeso = imc >= 25 and imc < 30
obesidad = imc >= 30

# Mostramos resultados
print(f"Tu IMC es: {imc:.2f}")
print(f"¿Bajo peso? {bajo_peso}")
print(f"¿Peso normal? {peso_normal}")
print(f"¿Sobrepeso? {sobrepeso}")
print(f"¿Obesidad? {obesidad}")
```

</details>

---

### Ejercicio 7: Desglose de tiempo

Pide al usuario una cantidad de **segundos** (número entero grande) y conviértela a días, horas, minutos y segundos restantes usando los operadores `//` y `%`.

**Ejemplo de interacción:**
```
Introduce una cantidad de segundos: 90061
90061 segundos equivalen a:
  1 días
  1 horas
  1 minutos
  1 segundos
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 7: Desglose de tiempo
total_segundos = int(input("Introduce una cantidad de segundos: "))

# Constantes de conversión
SEGUNDOS_POR_DIA = 86400     # 24 * 60 * 60
SEGUNDOS_POR_HORA = 3600     # 60 * 60
SEGUNDOS_POR_MINUTO = 60

# Calculamos cada unidad usando // y %
dias = total_segundos // SEGUNDOS_POR_DIA
restante = total_segundos % SEGUNDOS_POR_DIA

horas = restante // SEGUNDOS_POR_HORA
restante = restante % SEGUNDOS_POR_HORA

minutos = restante // SEGUNDOS_POR_MINUTO
segundos = restante % SEGUNDOS_POR_MINUTO

# Mostramos el resultado
print(f"{total_segundos} segundos equivalen a:")
print(f"  {dias} días")
print(f"  {horas} horas")
print(f"  {minutos} minutos")
print(f"  {segundos} segundos")
```

</details>

---

### Ejercicio 8: Evaluador de riesgo crediticio

Un banco simplificado evalúa el riesgo de un solicitante de préstamo en base a tres criterios. Pide al usuario: salario anual, años de antigüedad laboral y si tiene deudas pendientes (s/n). Evalúa las siguientes condiciones y muestra si el préstamo se aprobaría:

- **Aprobado**: Salario ≥ 20000 AND antigüedad ≥ 2 AND no tiene deudas.
- **Revisión**: Cumple al menos 2 de los 3 criterios.
- **Denegado**: Cumple 1 o ninguno.

Usa operadores lógicos, de comparación y expresiones booleanas combinadas.

**Ejemplo de interacción:**
```
Salario anual (€): 25000
Años de antigüedad: 3
¿Tiene deudas pendientes? (s/n): n

--- EVALUACIÓN ---
Salario suficiente (≥20000€): True
Antigüedad suficiente (≥2 años): True
Sin deudas pendientes: True
Criterios cumplidos: 3 de 3
Resultado: APROBADO
```

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 8: Evaluador de riesgo crediticio
salario = float(input("Salario anual (€): "))
antiguedad = int(input("Años de antigüedad: "))
respuesta_deudas = input("¿Tiene deudas pendientes? (s/n): ").lower()

# Evaluamos cada criterio (resultado booleano)
salario_ok = salario >= 20000
antiguedad_ok = antiguedad >= 2
sin_deudas = respuesta_deudas == "n"

# Contamos cuántos criterios se cumplen
# True se comporta como 1 y False como 0 al sumar
criterios_cumplidos = int(salario_ok) + int(antiguedad_ok) + int(sin_deudas)

# Determinamos el resultado con operadores lógicos
aprobado = salario_ok and antiguedad_ok and sin_deudas
en_revision = not aprobado and criterios_cumplidos >= 2

# Elegimos el texto del resultado
if aprobado:
    resultado = "APROBADO"
elif en_revision:
    resultado = "EN REVISIÓN"
else:
    resultado = "DENEGADO"

# Mostramos la evaluación
print()
print("--- EVALUACIÓN ---")
print(f"Salario suficiente (≥20000€): {salario_ok}")
print(f"Antigüedad suficiente (≥2 años): {antiguedad_ok}")
print(f"Sin deudas pendientes: {sin_deudas}")
print(f"Criterios cumplidos: {criterios_cumplidos} de 3")
print(f"Resultado: {resultado}")
```

</details>

---

## Ejercicios de Nivel Superior (9–10)

---

### Ejercicio 9: Simulador de facturación con descuentos escalonados

Crea un programa para una tienda que aplica descuentos según el importe de la compra:

- Menos de 50€: sin descuento
- De 50€ a 99.99€: 5% de descuento
- De 100€ a 199.99€: 10% de descuento
- 200€ o más: 15% de descuento

Además, si el cliente tiene tarjeta de fidelización, se aplica un 3% de descuento adicional **sobre el precio ya descontado**. Pide el importe y si tiene tarjeta, y muestra una factura detallada. Usa variables, conversión de tipos, operadores aritméticos, de comparación y lógicos, y f-strings.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 9: Simulador de facturación con descuentos escalonados
print("=== SISTEMA DE FACTURACIÓN ===")
importe = float(input("Importe de la compra (€): "))
tiene_tarjeta = input("¿Tiene tarjeta de fidelización? (s/n): ").lower() == "s"

# Determinamos el porcentaje de descuento según el importe
# Usamos comparaciones encadenadas
if importe >= 200:
    pct_descuento = 15
elif importe >= 100:
    pct_descuento = 10
elif importe >= 50:
    pct_descuento = 5
else:
    pct_descuento = 0

# Calculamos el descuento por importe
descuento_importe = importe * (pct_descuento / 100)
subtotal = importe - descuento_importe

# Si tiene tarjeta, aplicamos el 3% adicional sobre el subtotal
descuento_tarjeta = subtotal * 0.03 if tiene_tarjeta else 0.0
precio_sin_iva = subtotal - descuento_tarjeta

# Calculamos el IVA
iva = precio_sin_iva * 0.21
total_final = precio_sin_iva + iva

# Mostramos la factura
print()
print("=" * 40)
print("           FACTURA")
print("=" * 40)
print(f"Importe original:     {importe:>10.2f} €")
print(f"Descuento ({pct_descuento}%):       -{descuento_importe:>10.2f} €")

if tiene_tarjeta:
    print(f"Dto. fidelización (3%):  -{descuento_tarjeta:>7.2f} €")

print(f"-" * 40)
print(f"Base imponible:       {precio_sin_iva:>10.2f} €")
print(f"IVA (21%):            {iva:>10.2f} €")
print(f"=" * 40)
print(f"TOTAL A PAGAR:        {total_final:>10.2f} €")
print(f"Tarjeta fidelización: {'Sí' if tiene_tarjeta else 'No'}")
```

</details>

---

### Ejercicio 10: Calculadora de nómina con tramos IRPF

Crea un programa que calcule la nómina mensual de un empleado aplicando tramos simplificados de IRPF sobre el salario bruto **anual**. Los tramos son acumulativos (como en la realidad):

| Tramo                  | Tipo aplicable |
|------------------------|----------------|
| Hasta 12.450 €         | 19%            |
| De 12.450 a 20.200 €   | 24%            |
| De 20.200 a 35.200 €   | 30%            |
| De 35.200 a 60.000 €   | 37%            |
| Más de 60.000 €        | 45%            |

Pide el salario bruto anual. Calcula la retención total de IRPF por tramos, la cuota de Seguridad Social (6.35% del bruto), el salario neto anual y el salario neto mensual (12 pagas). Muestra todo con formato.

**Nota**: Los tramos se aplican de forma progresiva. Los primeros 12.450€ siempre tributan al 19%, los siguientes hasta 20.200€ al 24%, etc.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 10: Calculadora de nómina con tramos IRPF
print("=== CALCULADORA DE NÓMINA ===")
bruto_anual = float(input("Salario bruto anual (€): "))

# Definimos los límites de cada tramo y sus porcentajes
# Calculamos el IRPF de forma progresiva (por tramos)
irpf_total = 0.0
restante = bruto_anual

# Tramo 1: hasta 12.450€ al 19%
tramo1 = min(restante, 12450)
irpf_tramo1 = tramo1 * 0.19
irpf_total += irpf_tramo1
restante -= tramo1

# Tramo 2: de 12.450 a 20.200€ al 24% (franja de 7.750€)
tramo2 = min(restante, 20200 - 12450)
tramo2 = max(tramo2, 0)  # No puede ser negativo
irpf_tramo2 = tramo2 * 0.24
irpf_total += irpf_tramo2
restante -= tramo2

# Tramo 3: de 20.200 a 35.200€ al 30% (franja de 15.000€)
tramo3 = min(restante, 35200 - 20200)
tramo3 = max(tramo3, 0)
irpf_tramo3 = tramo3 * 0.30
irpf_total += irpf_tramo3
restante -= tramo3

# Tramo 4: de 35.200 a 60.000€ al 37% (franja de 24.800€)
tramo4 = min(restante, 60000 - 35200)
tramo4 = max(tramo4, 0)
irpf_tramo4 = tramo4 * 0.37
irpf_total += irpf_tramo4
restante -= tramo4

# Tramo 5: más de 60.000€ al 45%
tramo5 = max(restante, 0)
irpf_tramo5 = tramo5 * 0.45
irpf_total += irpf_tramo5

# Seguridad Social: 6.35% del bruto
ss = bruto_anual * 0.0635

# Tipo efectivo de IRPF
tipo_efectivo = (irpf_total / bruto_anual) * 100 if bruto_anual > 0 else 0

# Neto anual y mensual
neto_anual = bruto_anual - irpf_total - ss
neto_mensual = neto_anual / 12

# Mostramos el resultado
print()
print("=" * 45)
print("          DESGLOSE DE NÓMINA")
print("=" * 45)
print(f"Salario bruto anual:      {bruto_anual:>10.2f} €")
print()
print("  --- Retención IRPF por tramos ---")
print(f"  Tramo 1 (19%): {tramo1:>8.2f} € → {irpf_tramo1:>8.2f} €")
print(f"  Tramo 2 (24%): {tramo2:>8.2f} € → {irpf_tramo2:>8.2f} €")
print(f"  Tramo 3 (30%): {tramo3:>8.2f} € → {irpf_tramo3:>8.2f} €")
print(f"  Tramo 4 (37%): {tramo4:>8.2f} € → {irpf_tramo4:>8.2f} €")
print(f"  Tramo 5 (45%): {tramo5:>8.2f} € → {irpf_tramo5:>8.2f} €")
print(f"  Total IRPF:              -{irpf_total:>10.2f} €")
print(f"  Tipo efectivo IRPF:       {tipo_efectivo:>9.2f} %")
print()
print(f"Seg. Social (6.35%):      -{ss:>10.2f} €")
print("-" * 45)
print(f"Salario neto anual:       {neto_anual:>10.2f} €")
print(f"Salario neto mensual:     {neto_mensual:>10.2f} €")
print("=" * 45)
```

</details>

---

*Estos ejercicios integran todos los operadores (aritméticos, de comparación, lógicos, de asignación compuesta), la conversión de tipos y el formateo con f-strings de la Semana 1.*
