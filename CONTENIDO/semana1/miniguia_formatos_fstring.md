# 📋 Miniguía: Formatos en F-Strings

> Decimales · Zero-padding · Alineación a la derecha

---

## 🎯 ¿Por qué formatear números?

Los números en programas reales necesitan presentarse de forma clara y profesional:
- **Dinero:** `25.50 €` (siempre 2 decimales)
- **Códigos:** `000042` (con ceros a la izquierda)
- **Tablas:** números alineados a la derecha para fácil lectura

---

## 1️⃣ Formato de Decimales (`.Nf`)

### ¿Qué es?
Controla **cuántos decimales** muestra un número flotante.

### Sintaxis:
```python
{variable:.Nf}
```
Donde `N` = número de decimales deseados

### Ejemplos:

```python
precio = 19.9999

print(f"{precio:.2f}")  # 19.99  (2 decimales)
print(f"{precio:.1f}")  # 20.0   (1 decimal)
print(f"{precio:.0f}")  # 20     (sin decimales)
print(f"{precio:.3f}")  # 20.000 (3 decimales)
```

### Caso de uso real:
```python
# En una tienda
articulo = "Café"
precio = 2.567

print(f"{articulo}: {precio:.2f} €")
# Salida: Café: 2.57 €
```

---

## 2️⃣ Zero-Padding (`0N`)

### ¿Qué es?
Rellena un número con **ceros a la izquierda** hasta alcanzar un ancho mínimo.

### Sintaxis:
```python
{variable:0N}
```
Donde `N` = ancho total incluyendo ceros

### Ejemplos:

```python
numero = 42

print(f"{numero:04}")   # 0042  (4 dígitos)
print(f"{numero:05}")   # 00042 (5 dígitos)
print(f"{numero:03}")   # 042   (3 dígitos)
print(f"{numero:02}")   # 42    (no se añaden ceros, ya tiene 2)
```

### Caso de uso real:
```python
# Códigos de factura
numero_factura = 7

print(f"Factura: {numero_factura:06}")
# Salida: Factura: 000007
```

---

## 3️⃣ Alineación a la Derecha (`>N`)

### ¿Qué es?
Alinea un número **a la derecha** dentro de un espacio de ancho mínimo, rellenando con espacios a la izquierda.

### Sintaxis:
```python
{variable:>N}
```
Donde `N` = ancho total incluyendo espacios

### Ejemplos:

```python
numero = 25

print(f"|{numero:>5}|")   # |   25|  (5 caracteres total)
print(f"|{numero:>8}|")   # |      25|  (8 caracteres total)
print(f"|{numero:>3}|")   # | 25|   (3 caracteres total)
```

### Caso de uso real:
```python
# Lista de precios alineados
print(f"Manzana:      {1.50:>8.2f} €")
print(f"Plátano:      {0.75:>8.2f} €")
print(f"Sandía:      {12.99:>8.2f} €")

# Salida:
# Manzana:           1.50 €
# Plátano:           0.75 €
# Sandía:           12.99 €
```

---

## 🔗 Combinando formatos

Puedes **combinar** estos formatos en una sola expresión:

```python
{variable:0N.Mf}
```

- `0` = rellena con ceros
- `N` = ancho total
- `.M` = decimales

### Ejemplo:

```python
temperatura = 5.3

print(f"{temperatura:08.2f}")  # 00005.30
#        ^^^^^^
#        8 caracteres total, relleno con ceros
#               ^^
#               2 decimales
```

### Otro ejemplo - Tabla de precios:

```python
items = [("Café", 2.5), ("Té", 1.75), ("Agua", 0.5)]

for nombre, precio in items:
    codigo = len(nombre)  # Simulamos un código
    print(f"[{codigo:03}] {nombre:>10} → {precio:>7.2f} €")

# Salida:
# [004] Café → 2.50 €
# [003] Té → 1.75 €
# [005] Agua → 0.50 €
```

---

## 📊 Tabla resumen

| Formato | Qué hace | Ejemplo | Salida |
|---------|----------|---------|--------|
| `{x:.2f}` | 2 decimales | `{3.7:.2f}` | `3.70` |
| `{x:.0f}` | Sin decimales | `{3.7:.0f}` | `4` |
| `{x:05}` | Rellena con 5 ceros | `{42:05}` | `00042` |
| `{x:08}` | Rellena con 8 ceros | `{7:08}` | `00000007` |
| `{x:>8}` | Alinea derecha, 8 ancho | `{25:>8}` | `      25` |
| `{x:>10.2f}` | Derecha + 2 decimales | `{5.1:>10.2f}` | `      5.10` |
| `{x:010.2f}` | Ceros + 2 decimales | `{5.1:010.2f}` | `0000005.10` |

---

## ✅ Checklist práctico

- [ ] ¿Necesitas mostrar dinero? → Usa `.2f`
- [ ] ¿Necesitas códigos de factura? → Usa `0N`
- [ ] ¿Necesitas tablas legibles? → Usa `>N`
- [ ] ¿Dinero en tabla? → Usa `>N.2f`
- [ ] ¿Códigos formales (DNI)? → Usa `0N.Mf` si necesitas decimales

---

*¡Ahora practica con los ejercicios!*
