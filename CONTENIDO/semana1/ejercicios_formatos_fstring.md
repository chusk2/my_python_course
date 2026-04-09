# 🏋️ Ejercicios: Formatos en F-Strings

> Decimales (`.Nf`) · Zero-padding (`0N`) · Alineación a la derecha (`>N`)

---

## 🟢 Formato de Decimales

### Ejercicio 1 — Precios de café

Una cafetería tiene estos precios en euros. Tu tarea es mostrar cada precio **con exactamente 2 decimales**, aunque algunos números sean redondeados.

```
Café espresso: 2.5 €
Café con leche: 3.85 €
Capuchino: 4.0 €
Té: 1.999 €
```

Crea variables con estos precios y usa f-strings para mostrar cada uno con `.2f`.

**Ejemplo de salida esperada:**
```
Café espresso: 2.50 €
Café con leche: 3.85 €
Capuchino: 4.00 €
Té: 2.00 €
```

<details>
<summary>💡 Pista</summary>

Usa `{variable:.2f}` dentro de la f-string para asegurar 2 decimales. El formato `.Nf` redondea automáticamente.

</details>

<details>
<summary>✅ Solución</summary>

```python
# Precios en euros (algunos sin decimales, otros con muchos)
espresso = 2.5
con_leche = 3.85
capuchino = 4.0
te = 1.999

# Mostramos cada precio con exactamente 2 decimales
print(f"Café espresso: {espresso:.2f} €")
print(f"Café con leche: {con_leche:.2f} €")
print(f"Capuchino: {capuchino:.2f} €")
print(f"Té: {te:.2f} €")
```

</details>

---

### Ejercicio 2 — Cálculo de propinas

Un restaurante quiere calcular propinas. Dado el precio total de la comida, calcula el 10%, 15% y 20% de propina. Muestra cada propina con `.2f`.

**Datos:**
- Precio comida: 42.67 €

**Ejemplo de salida esperada:**
```
Total de la comida: 42.67 €
Propina 10%: 4.27 €
Propina 15%: 6.40 €
Propina 20%: 8.53 €
```

<details>
<summary>💡 Pista</summary>

Calcula cada propina multiplicando el precio por el porcentaje (0.10, 0.15, 0.20). Usa `.2f` para mostrar el resultado.

</details>

<details>
<summary>✅ Solución</summary>

```python
# Precio total de la comida
precio_comida = 42.67

# Calculamos las propinas
propina_10 = precio_comida * 0.10
propina_15 = precio_comida * 0.15
propina_20 = precio_comida * 0.20

# Mostramos con 2 decimales
print(f"Total de la comida: {precio_comida:.2f} €")
print(f"Propina 10%: {propina_10:.2f} €")
print(f"Propina 15%: {propina_15:.2f} €")
print(f"Propina 20%: {propina_20:.2f} €")
```

</details>

---

## 🟡 Zero-Padding

### Ejercicio 3 — Números de factura

Una empresa emite facturas con números secuenciales. Los números deben tener **siempre 6 dígitos**, con ceros a la izquierda si es necesario.

**Datos:**
- Números de factura: 1, 42, 305, 8, 999

**Ejemplo de salida esperada:**
```
Factura número: 000001
Factura número: 000042
Factura número: 000305
Factura número: 000008
Factura número: 000999
```

<details>
<summary>💡 Pista</summary>

Usa `{variable:06}` para rellenar con ceros hasta 6 dígitos. El `0` indica que rellena con ceros, y el `6` es el ancho total.

</details>

<details>
<summary>✅ Solución</summary>

```python
# Números de factura secuenciales
numeros = [1, 42, 305, 8, 999]

# Mostramos cada uno con 6 dígitos y relleno de ceros
for numero in numeros:
    print(f"Factura número: {numero:06}")
```

</details>

---

### Ejercicio 4 — Códigos de producto

Una tienda online necesita códigos de producto con formato: **"PROD-0000X"**, donde X es el número del producto (1, 5, 23, 100, 7).

**Ejemplo de salida esperada:**
```
PROD-00001
PROD-00005
PROD-00023
PROD-00100
PROD-00007
```

<details>
<summary>💡 Pista</summary>

Combina texto fijo con `{variable:05}`. El número debe tener exactamente 5 dígitos con relleno de ceros.

</details>

<details>
<summary>✅ Solución</summary>

```python
# IDs de productos
ids = [1, 5, 23, 100, 7]

# Creamos el código con formato y relleno de ceros
for id_producto in ids:
    codigo = f"PROD-{id_producto:05}"
    print(codigo)
```

</details>

---

## 🔴 Alineación a la Derecha

### Ejercicio 5 — Tabla de inventario

Una tienda necesita mostrar un inventario en forma de tabla. Los nombres de productos deben estar alineados a la izquierda y las cantidades a la derecha (para fácil lectura).

**Datos:**
- Manzanas: 45
- Plátanos: 8
- Naranjas: 127
- Uvas: 3

**Ejemplo de salida esperada:**
```
Manzanas         45
Plátanos          8
Naranjas        127
Uvas              3
```

<details>
<summary>💡 Pista</summary>

Usa `{variable:>N}` donde N es el ancho. Para alinear a la izquierda productos y a la derecha cantidades, necesitas dos formatos diferentes en la misma línea.

</details>

<details>
<summary>✅ Solución</summary>

```python
# Inventario: producto y cantidad
inventario = [
    ("Manzanas", 45),
    ("Plátanos", 8),
    ("Naranjas", 127),
    ("Uvas", 3)
]

# Mostramos con alineación a la derecha para las cantidades
for producto, cantidad in inventario:
    print(f"{producto:<15} {cantidad:>3}")
```

</details>

---

### Ejercicio 6 — Factura profesional

Crea una factura simple pero profesional con precios alineados a la derecha y con 2 decimales. Los artículos tienen nombre, cantidad y precio unitario.

**Datos:**
- Artículo 1: "Laptop", cantidad: 2, precio unitario: 999.99 €
- Artículo 2: "Mouse", cantidad: 5, precio unitario: 25.50 €
- Artículo 3: "Teclado", cantidad: 3, precio unitario: 120.00 €

**Ejemplo de salida esperada:**
```
=== FACTURA ===
Laptop           2      999.99 €    1999.98 €
Mouse            5       25.50 €     127.50 €
Teclado          3      120.00 €     360.00 €
---
TOTAL:                            2487.48 €
```

<details>
<summary>💡 Pista</summary>

Usa:
- `{nombre:<15}` para alinear el producto a la izquierda
- `{cantidad:>2}` para la cantidad centrada
- `{precio:>10.2f}` para el precio unitario alineado a la derecha
- Calcula el subtotal multiplicando cantidad por precio unitario

</details>

<details>
<summary>✅ Solución</summary>

```python
# Datos de la factura
articulos = [
    ("Laptop", 2, 999.99),
    ("Mouse", 5, 25.50),
    ("Teclado", 3, 120.00)
]

# Encabezado
print("=== FACTURA ===")

# Variable para acumular total
total = 0

# Mostramos cada artículo
for nombre, cantidad, precio_unitario in articulos:
    subtotal = cantidad * precio_unitario
    total += subtotal
    print(f"{nombre:<15} {cantidad:>2} {precio_unitario:>10.2f} € {subtotal:>10.2f} €")

# Línea de separación y total
print("-" * 60)
print(f"{'TOTAL:':>35} {total:>10.2f} €")
```

</details>

---

## 📊 Resumen de ejercicios

| Nº  | Nivel   | Concepto principal              | Dificultad |
|-----|---------|----------------------------------|-----------|
| 1   | 🟢      | Decimales (`.2f`)               | Fácil     |
| 2   | 🟢      | Decimales con cálculos          | Media     |
| 3   | 🟡      | Zero-padding (`0N`)             | Fácil     |
| 4   | 🟡      | Zero-padding en códigos         | Media     |
| 5   | 🔴      | Alineación (`>N`)               | Media     |
| 6   | 🔴      | Combinación de formatos         | Avanzada  |

---

## 💡 Consejos finales

- **Dinero:** siempre `.2f`
- **Códigos:** `0N` para relleno de ceros
- **Tablas:** `>N` o `>N.2f` para números alineados
- **Profesionalidad:** la alineación hace que los datos se lean más fácilmente

---

*¡Completa los ejercicios en orden y consulta las pistas antes de ver la solución!*
