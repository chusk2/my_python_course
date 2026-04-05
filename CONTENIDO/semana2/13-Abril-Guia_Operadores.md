# Lunes 13/04 — Operadores Aritméticos, Lógicos y Construcción de Expresiones

---

## 1. ¿Qué es un operador?

Un **operador** es un símbolo que le dice a Python que realice una operación sobre uno o más valores. Ya conocemos el operador de asignación (`=`) y los operadores aritméticos básicos de la semana anterior. Ahora vamos a profundizar en todos los tipos de operadores y a aprender a combinarlos en **expresiones** más complejas.

---

## 2. Operadores aritméticos

Son los que usamos para hacer cálculos matemáticos:

| Operador | Nombre             | Ejemplo     | Resultado |
|----------|--------------------|-------------|-----------|
| `+`      | Suma               | `7 + 3`     | `10`      |
| `-`      | Resta              | `7 - 3`     | `4`       |
| `*`      | Multiplicación     | `7 * 3`     | `21`      |
| `/`      | División           | `7 / 3`     | `2.3333…` |
| `//`     | División entera    | `7 // 3`    | `2`       |
| `%`      | Módulo (resto)     | `7 % 3`     | `1`       |
| `**`     | Potencia           | `2 ** 4`    | `16`      |

### División `/` vs división entera `//`

```python
# La división normal siempre devuelve un float
print(10 / 3)    # 3.3333333333333335
print(10 / 2)    # 5.0 (¡float, no int!)

# La división entera descarta los decimales (no redondea)
print(10 // 3)   # 3
print(10 // 2)   # 5 (int)
```

### El operador módulo `%`

El módulo devuelve el **resto** de una división. Es increíblemente útil en programación:

```python
# ¿Es un número par o impar?
print(10 % 2)   # 0 → par (se divide exacto)
print(7 % 2)    # 1 → impar (sobra 1)

# ¿Es divisible entre 5?
print(15 % 5)   # 0 → sí
print(17 % 5)   # 2 → no

# Obtener la última cifra de un número
print(1234 % 10)  # 4
```

**Aplicación real**: Saber si un año es bisiesto, alternar colores en filas de una tabla, controlar turnos rotativos, etc.

---

## 3. Operadores de comparación

Comparan dos valores y devuelven un **booleano** (`True` o `False`):

| Operador | Significado         | Ejemplo     | Resultado |
|----------|---------------------|-------------|-----------|
| `==`     | Igual a             | `5 == 5`    | `True`    |
| `!=`     | Diferente de        | `5 != 3`    | `True`    |
| `>`      | Mayor que           | `5 > 3`     | `True`    |
| `<`      | Menor que           | `5 < 3`     | `False`   |
| `>=`     | Mayor o igual que   | `5 >= 5`    | `True`    |
| `<=`     | Menor o igual que   | `3 <= 5`    | `True`    |

```python
edad = 25

print(edad == 25)    # True
print(edad != 30)    # True
print(edad > 18)     # True
print(edad < 18)     # False
print(edad >= 25)    # True
```

> **Cuidado**: `=` es **asignación** (guardar un valor). `==` es **comparación** (¿son iguales?). Es uno de los errores más comunes al empezar.

### Comparar textos

Las comparaciones también funcionan con cadenas. Se comparan en **orden alfabético** (técnicamente, por su código Unicode):

```python
print("Ana" == "Ana")      # True
print("Ana" == "ana")      # False (mayúsculas ≠ minúsculas)
print("Ana" < "Carlos")    # True ("A" va antes que "C")
print("zapato" > "barco")  # True ("z" va después de "b")
```

---

## 4. Operadores lógicos

Permiten combinar varias condiciones booleanas:

| Operador | Significado | Ejemplo                     | Resultado |
|----------|-------------|-----------------------------|-----------|
| `and`    | Y (ambos)   | `True and False`            | `False`   |
| `or`     | O (alguno)  | `True or False`             | `True`    |
| `not`    | No (negar)  | `not True`                  | `False`   |

### Tablas de verdad

**`and`** — Solo es `True` si **ambas** condiciones son verdaderas:

| A       | B       | A and B |
|---------|---------|---------|
| `True`  | `True`  | `True`  |
| `True`  | `False` | `False` |
| `False` | `True`  | `False` |
| `False` | `False` | `False` |

**`or`** — Es `True` si **al menos una** condición es verdadera:

| A       | B       | A or B  |
|---------|---------|---------|
| `True`  | `True`  | `True`  |
| `True`  | `False` | `True`  |
| `False` | `True`  | `True`  |
| `False` | `False` | `False` |

**`not`** — Invierte el valor:

| A       | not A   |
|---------|---------|
| `True`  | `False` |
| `False` | `True`  |

### Ejemplos prácticos

```python
edad = 25
tiene_carnet = True
salario = 1800

# ¿Puede alquilar un coche? (mayor de 21 Y tiene carnet)
puede_alquilar = edad >= 21 and tiene_carnet
print(puede_alquilar)  # True

# ¿Accede a la promoción? (menor de 30 O salario menor de 1500)
accede_promo = edad < 30 or salario < 1500
print(accede_promo)    # True (cumple la primera)

# ¿No es menor de edad?
es_adulto = not (edad < 18)
print(es_adulto)       # True
```

---

## 5. Operadores de asignación compuesta

Son atajos para operar y asignar al mismo tiempo:

| Operador | Equivale a        | Ejemplo            |
|----------|--------------------|--------------------|
| `+=`     | `x = x + valor`   | `x += 5`           |
| `-=`     | `x = x - valor`   | `x -= 3`           |
| `*=`     | `x = x * valor`   | `x *= 2`           |
| `/=`     | `x = x / valor`   | `x /= 4`           |
| `//=`    | `x = x // valor`  | `x //= 3`          |
| `%=`     | `x = x % valor`   | `x %= 2`           |
| `**=`    | `x = x ** valor`  | `x **= 2`          |

```python
contador = 0
contador += 1   # Ahora vale 1
contador += 1   # Ahora vale 2

precio = 100
precio *= 1.21  # Aplicar IVA: ahora vale 121.0
```

---

## 6. Operadores de pertenencia e identidad

### Pertenencia: `in` y `not in`

Comprueban si un valor está contenido dentro de otro (texto, lista, etc.):

```python
# En texto
print("a" in "Hola")       # False (no hay "a" minúscula en "Hola")
print("ol" in "Hola")      # True

# En listas (las veremos en la semana 3, pero adelantamos)
frutas = ["manzana", "pera", "naranja"]
print("pera" in frutas)       # True
print("kiwi" not in frutas)   # True
```

### Identidad: `is` y `is not`

Comprueban si dos variables apuntan al **mismo objeto en memoria** (no solo si tienen el mismo valor):

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)     # True (mismo valor)
print(a is b)     # False (son objetos distintos en memoria)
print(a is c)     # True (c apunta al mismo objeto que a)
```

> **Regla práctica**: Usa `==` para comparar valores. Usa `is` solo para comparar con `None`: `if resultado is None:`.

---

## 7. Precedencia de operadores (orden de evaluación)

Cuando una expresión tiene varios operadores, Python los evalúa en un orden específico, similar a las matemáticas:

| Prioridad | Operadores                     | Ejemplo                |
|-----------|--------------------------------|------------------------|
| 1 (alta)  | `**`                           | Potencia               |
| 2         | `+x`, `-x`, `not`             | Signos y negación      |
| 3         | `*`, `/`, `//`, `%`           | Multiplicación, etc.   |
| 4         | `+`, `-`                       | Suma y resta           |
| 5         | `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `not in`, `is` | Comparaciones |
| 6         | `not`                          | Negación lógica        |
| 7         | `and`                          | Y lógico               |
| 8 (baja)  | `or`                           | O lógico               |

### Usa paréntesis para ser explícito

Aunque Python tiene reglas de precedencia, es **buena práctica** usar paréntesis para dejar claro el orden:

```python
# Sin paréntesis: ¿qué se evalúa primero?
resultado = 5 + 3 * 2    # = 11 (no 16, porque * va antes que +)

# Con paréntesis: intención clara
resultado = 5 + (3 * 2)  # = 11 (explícito)
resultado = (5 + 3) * 2  # = 16 (cambia el resultado)
```

```python
# Ejemplo con operadores lógicos
edad = 20
tiene_invitacion = True

# Sin paréntesis puede ser confuso
puede_entrar = edad >= 18 and tiene_invitacion or edad >= 16
# ¿Cómo se lee? Puede ser ambiguo

# Con paréntesis, queda claro:
puede_entrar = (edad >= 18 and tiene_invitacion) or (edad >= 16)
```

---

## 8. Construir expresiones: combinar todo

Una **expresión** es cualquier combinación de valores, variables y operadores que Python puede evaluar para obtener un resultado.

### Ejemplo: Calcular el precio final de un producto

```python
precio_base = 50.00
descuento_pct = 15       # 15%
iva_pct = 21             # 21%

# Expresión que combina varios operadores
precio_con_descuento = precio_base * (1 - descuento_pct / 100)
precio_final = precio_con_descuento * (1 + iva_pct / 100)

print(f"Precio base:      {precio_base:.2f} €")
print(f"Descuento ({descuento_pct}%):  -{precio_base - precio_con_descuento:.2f} €")
print(f"Precio + IVA:     {precio_final:.2f} €")
```

### Ejemplo: Validar un formulario

```python
email = input("Email: ")
password = input("Contraseña: ")

# Expresión lógica compleja: combinamos varias condiciones
es_valido = (
    len(email) > 5
    and "@" in email
    and "." in email
    and len(password) >= 8
)

print(f"Formulario válido: {es_valido}")
```

### Ejemplo: Calcular coste de envío

```python
peso_kg = float(input("Peso del paquete (kg): "))
distancia_km = float(input("Distancia (km): "))
es_urgente = input("¿Envío urgente? (s/n): ").lower() == "s"

# Tarifa base + tarifa por peso + recargo urgente
coste = 3.50 + (peso_kg * 0.80) + (distancia_km * 0.02)
if es_urgente:
    coste *= 1.50  # Recargo del 50%

print(f"Coste de envío: {coste:.2f} €")
```

---

## Resumen de la sesión

| Concepto                  | Idea clave                                                       |
|---------------------------|------------------------------------------------------------------|
| Operadores aritméticos    | `+`, `-`, `*`, `/`, `//`, `%`, `**`                              |
| Operadores de comparación | `==`, `!=`, `>`, `<`, `>=`, `<=` → devuelven `bool`              |
| Operadores lógicos        | `and`, `or`, `not` → combinan condiciones                        |
| Asignación compuesta      | `+=`, `-=`, `*=`… → operan y asignan en un paso                 |
| Pertenencia               | `in`, `not in` → buscar dentro de textos, listas…                |
| Precedencia               | Potencia > Multiplicación > Suma > Comparación > Lógicos         |
| Expresiones               | Combinación de valores, variables y operadores                    |
| Buena práctica            | Usar paréntesis para hacer explícito el orden de evaluación       |

---

*Siguiente clase: Martes 14/04 — Estructuras condicionales y toma de decisiones en código.*
