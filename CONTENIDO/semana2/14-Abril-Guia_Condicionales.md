# Martes 14/04 — Estructuras Condicionales y Toma de Decisiones

---

## 1. ¿Por qué necesitamos condicionales?

Hasta ahora, nuestros programas siguen un camino lineal: se ejecutan de arriba a abajo, línea a línea. Pero en la vida real, constantemente tomamos decisiones:

- *Si* está lloviendo, *entonces* cojo el paraguas; *si no*, no lo cojo.
- *Si* el cliente tiene descuento, aplico el 10%; *si no*, cobro el precio completo.
- *Si* la temperatura es mayor de 30°, enciendo el aire acondicionado.

Las **estructuras condicionales** permiten que nuestro programa tome caminos diferentes según se cumplan o no ciertas condiciones.

---

## 2. La sentencia `if`

Es la forma más básica de tomar una decisión. Si la condición es `True`, se ejecuta el bloque indentado. Si es `False`, se lo salta.

```python
temperatura = float(input("¿Qué temperatura hace? "))

if temperatura > 30:
    print("Hace mucho calor, ¡enciende el aire acondicionado!")

print("Este mensaje siempre aparece")  # Fuera del if
```

### Anatomía del `if`

```python
if condición:          # La condición debe evaluar a True o False
    instrucción_1      # Este bloque se ejecuta SOLO si la condición es True
    instrucción_2      # Todas las líneas del bloque deben estar indentadas
```

**Reglas clave:**

- La condición va seguida de **dos puntos** (`:`).
- El bloque interior debe estar **indentado** (4 espacios).
- La condición es cualquier **expresión booleana** (lo que aprendimos ayer con operadores).

---

## 3. La sentencia `if-else`

Cuando queremos hacer algo si la condición se cumple **y otra cosa diferente** si no se cumple:

```python
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18:
    print("Eres mayor de edad.")
    print("Puedes acceder al contenido.")
else:
    print("Eres menor de edad.")
    print("Acceso restringido.")
```

Piensa en `if-else` como una bifurcación: el programa siempre va por **uno** de los dos caminos, nunca por ambos.

---

## 4. La sentencia `if-elif-else`

Cuando hay **más de dos opciones** posibles, usamos `elif` (abreviatura de *else if*):

```python
nota = float(input("Introduce tu nota (0-10): "))

if nota >= 9:
    calificacion = "Sobresaliente"
elif nota >= 7:
    calificacion = "Notable"
elif nota >= 5:
    calificacion = "Aprobado"
else:
    calificacion = "Suspenso"

print(f"Tu calificación es: {calificacion}")
```

**Reglas de `elif`:**

- Puedes poner **tantos `elif` como necesites**.
- Se evalúan **en orden**: en cuanto una condición es `True`, se ejecuta ese bloque y se **ignoran los demás**.
- El `else` final es **opcional** y cubre "todo lo demás".

### Error común: condiciones que se solapan

```python
# MAL: las condiciones se solapan
nota = 9.5
if nota >= 5:
    print("Aprobado")     # ¡Entra aquí primero! 9.5 >= 5 es True
elif nota >= 7:
    print("Notable")      # Nunca llega aquí
elif nota >= 9:
    print("Sobresaliente") # Nunca llega aquí

# BIEN: evaluar de mayor a menor
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")
```

---

## 5. Condicionales anidados

Puedes poner un `if` dentro de otro `if`. Cada nivel requiere su propia indentación:

```python
tiene_entrada = input("¿Tienes entrada? (s/n): ").lower() == "s"
edad = int(input("¿Cuántos años tienes? "))

if tiene_entrada:
    if edad >= 18:
        print("Puedes pasar a cualquier zona.")
    else:
        print("Puedes pasar, pero solo a la zona general.")
else:
    print("No puedes pasar sin entrada.")
```

> **Consejo**: Evita anidar más de 2-3 niveles. Si necesitas más, probablemente puedes simplificar con `and`/`or` o reorganizar la lógica.

### Alternativa con operadores lógicos (más limpia)

```python
tiene_entrada = input("¿Tienes entrada? (s/n): ").lower() == "s"
edad = int(input("¿Cuántos años tienes? "))

if tiene_entrada and edad >= 18:
    print("Puedes pasar a cualquier zona.")
elif tiene_entrada and edad < 18:
    print("Puedes pasar, pero solo a la zona general.")
else:
    print("No puedes pasar sin entrada.")
```

---

## 6. Expresiones condicionales (operador ternario)

Python permite escribir un `if-else` en una sola línea para **asignar un valor** según una condición:

```python
# Forma larga
edad = 20
if edad >= 18:
    estado = "adulto"
else:
    estado = "menor"

# Forma corta (operador ternario)
estado = "adulto" if edad >= 18 else "menor"
```

La sintaxis es: `valor_si_true if condición else valor_si_false`

```python
# Ejemplos prácticos
descuento = 0.10 if es_socio else 0.0
mensaje = "Aprobado" if nota >= 5 else "Suspenso"
saludo = "Buenos días" if hora < 14 else "Buenas tardes"
```

> **Úsalo solo para asignaciones sencillas**. Si la lógica es compleja, usa un `if-else` normal: la legibilidad es más importante que escribir menos líneas.

---

## 7. Valores "truthy" y "falsy"

En Python, **cualquier valor** puede evaluarse como `True` o `False` dentro de un `if`, no solo los booleanos:

| Evaluado como `False` (falsy) | Evaluado como `True` (truthy) |
|-------------------------------|-------------------------------|
| `False`                       | `True`                        |
| `0`, `0.0`                    | Cualquier número distinto de 0 |
| `""` (texto vacío)            | Cualquier texto con contenido |
| `None`                        | Cualquier objeto que no sea None |
| `[]` (lista vacía)            | Lista con elementos           |

```python
nombre = input("Tu nombre: ")

# En lugar de: if nombre != "":
if nombre:
    print(f"Hola, {nombre}")
else:
    print("No has introducido ningún nombre")

# En lugar de: if len(lista) > 0:
resultados = []
if resultados:
    print("Hay resultados")
else:
    print("No hay resultados")
```

---

## 8. Patrones comunes y buenas prácticas

### Validar entrada del usuario

```python
respuesta = input("¿Continuar? (s/n): ").lower().strip()

if respuesta == "s" or respuesta == "si" or respuesta == "sí":
    print("Continuamos...")
elif respuesta == "n" or respuesta == "no":
    print("Saliendo...")
else:
    print("Opción no reconocida.")
```

### Evitar comparaciones redundantes con booleanos

```python
es_socio = True

# MAL: redundante
if es_socio == True:
    print("Descuento aplicado")

# BIEN: directo
if es_socio:
    print("Descuento aplicado")

# MAL: redundante
if es_socio == False:
    print("Sin descuento")

# BIEN: con not
if not es_socio:
    print("Sin descuento")
```

### Guardar el resultado en una variable

```python
# En lugar de repetir código en cada rama, asigna un valor y úsalo después
precio = 100
es_vip = True

if es_vip:
    descuento = 0.20
else:
    descuento = 0.05

precio_final = precio * (1 - descuento)
print(f"Precio final: {precio_final:.2f} €")
```

---

## 9. Ejemplo integrador: sistema de tarifas de parking

```python
# Sistema de tarifas de un parking
print("=== PARKING CENTRO CIUDAD ===")
horas = float(input("Horas de estacionamiento: "))
es_residente = input("¿Es residente? (s/n): ").lower() == "s"
es_fin_de_semana = input("¿Es fin de semana? (s/n): ").lower() == "s"

# Tarifa base por hora
if horas <= 1:
    tarifa_hora = 2.50
elif horas <= 4:
    tarifa_hora = 2.00
elif horas <= 8:
    tarifa_hora = 1.50
else:
    tarifa_hora = 1.00  # Tarifa plana para estancias largas

# Calculamos importe base
importe = horas * tarifa_hora

# Descuentos y recargos
descuento_residente = importe * 0.30 if es_residente else 0.0
recargo_finde = importe * 0.15 if es_fin_de_semana else 0.0

# Total final
total = importe - descuento_residente + recargo_finde

# Mostramos el ticket
print()
print("=" * 35)
print("        TICKET DE PARKING")
print("=" * 35)
print(f"Horas:               {horas:.1f}")
print(f"Tarifa/hora:         {tarifa_hora:.2f} €")
print(f"Importe base:        {importe:.2f} €")
if es_residente:
    print(f"Dto. residente (30%):  -{descuento_residente:.2f} €")
if es_fin_de_semana:
    print(f"Recargo finde (15%):  +{recargo_finde:.2f} €")
print("-" * 35)
print(f"TOTAL:               {total:.2f} €")
print("=" * 35)
```

---

## Resumen de la sesión

| Concepto                  | Idea clave                                                          |
|---------------------------|---------------------------------------------------------------------|
| `if`                      | Ejecuta un bloque solo si la condición es `True`                    |
| `if-else`                 | Dos caminos: uno si es `True`, otro si es `False`                   |
| `if-elif-else`            | Múltiples caminos, se evalúan en orden                              |
| Condicionales anidados    | `if` dentro de otro `if` (evitar más de 2-3 niveles)                |
| Operador ternario         | `valor_a if condición else valor_b` (para asignaciones simples)     |
| Truthy / Falsy            | `0`, `""`, `None`, `[]` son falsos; casi todo lo demás es verdadero |
| Buena práctica            | Evaluar de mayor a menor, no comparar con `True`/`False`            |

---

*Siguiente clase: Jueves 16/04 — Bucles, control de flujo y depuración básica.*
