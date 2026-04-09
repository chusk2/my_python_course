# Métodos en Python: Estáticos, de Clase y de Instancia

## Teoría

En Python, los métodos dentro de una clase se dividen en tres categorías según cómo acceden al estado del objeto o la clase.

---

### 🔵 Métodos de Instancia

Son los más comunes. Reciben como primer parámetro `self`, que representa al objeto que llama al método. Pueden acceder y modificar los atributos del objeto.

```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):          # método de instancia
        return f"{self.nombre} dice: ¡Guau!"
```

---

### 🟢 Métodos de Clase

Se definen con el decorador `@classmethod` y reciben `cls` como primer parámetro, que representa a la **clase** (no al objeto). Se usan para crear constructores alternativos o acceder a atributos de clase.

```python
class Perro:
    especie = "Canis lupus familiaris"

    @classmethod
    def descripcion_especie(cls):          # método de clase
        return f"Todos los perros son: {cls.especie}"
```

---

### 🟡 Métodos Estáticos

Se definen con `@staticmethod`. **No reciben** ni `self` ni `cls`. Son funciones auxiliares que tienen sentido lógico dentro de la clase, pero no necesitan acceder al objeto ni a la clase.

```python
class Matematica:
    @staticmethod
    def sumar(a, b):          # método estático
        return a + b
```

---

### Tabla comparativa

| Tipo          | Decorador       | Primer parámetro | Accede a instancia | Accede a clase |
|---------------|-----------------|------------------|--------------------|----------------|
| Instancia     | _(ninguno)_     | `self`           | ✅                 | ✅ (vía self)  |
| De clase      | `@classmethod`  | `cls`            | ❌                 | ✅             |
| Estático      | `@staticmethod` | _(ninguno)_      | ❌                 | ❌             |

---

## Ejercicios

---

### Ejercicio 1 — Temperatura 🌡️
**Tipo:** Estático y de instancia

Crea una clase `Temperatura` que:
- Guarde un valor en **Celsius** como atributo de instancia.
- Tenga un **método estático** `celsius_a_fahrenheit(c)` que convierta y retorne el valor.
- Tenga un **método de instancia** `mostrar()` que imprima el valor en Celsius y su equivalente en Fahrenheit (usando el método estático).

```python
# Uso esperado:
t = Temperatura(100)
t.mostrar()
# → 100°C equivale a 212.0°F
```

---

### Ejercicio 2 — Contador de objetos 🔢
**Tipo:** De clase e instancia

Crea una clase `Robot` que:
- Lleve la cuenta de cuántos robots se han creado usando un **atributo de clase** `total`.
- Incremente ese contador en `__init__`.
- Tenga un **método de clase** `cuantos_robots()` que retorne el total actual.
- Tenga un **método de instancia** `presentarse()` que imprima el nombre del robot.

```python
# Uso esperado:
r1 = Robot("R2D2")
r2 = Robot("C3PO")
Robot.cuantos_robots()   # → 2
r1.presentarse()         # → "Soy R2D2"
```

---

### Ejercicio 3 — Constructor alternativo 📅
**Tipo:** De clase

Crea una clase `Fecha` con atributos `dia`, `mes` y `anio`. Añade:
- Un **método de clase** `desde_string(cadena)` que reciba una cadena con formato `"DD-MM-AAAA"` y retorne una instancia de `Fecha`.
- Un **método de instancia** `mostrar()` que imprima la fecha con formato legible.

```python
# Uso esperado:
f = Fecha.desde_string("25-12-2024")
f.mostrar()   # → "25 de 12 de 2024"
```

---

### Ejercicio 4 — Validador de contraseñas 🔐
**Tipo:** Estático

Crea una clase `Cuenta` con atributos `usuario` y `contrasena`. Añade:
- Un **método estático** `es_contrasena_valida(contrasena)` que retorne `True` si la contraseña tiene al menos 8 caracteres, una mayúscula y un número. Si no cumple, retorna `False`.
- Un **método de instancia** `registrar()` que use el método estático para validar antes de confirmar el registro.

```python
# Uso esperado:
Cuenta.es_contrasena_valida("abc")        # → False
Cuenta.es_contrasena_valida("Segura123")  # → True
c = Cuenta("usuario1", "Segura123")
c.registrar()   # → "Registro exitoso"
```

---

### Ejercicio 5 — Descuento en tienda 🛍️
**Tipo:** De clase e instancia

Crea una clase `Producto` con atributos `nombre` y `precio`. Añade:
- Un **atributo de clase** `descuento` (porcentaje, ej: `0.10` para 10%).
- Un **método de clase** `cambiar_descuento(nuevo)` que actualice el descuento para todos los productos.
- Un **método de instancia** `precio_final()` que retorne el precio con el descuento aplicado.

```python
# Uso esperado:
p1 = Producto("Camiseta", 50)
p2 = Producto("Pantalón", 80)
Producto.cambiar_descuento(0.20)
p1.precio_final()   # → 40.0
p2.precio_final()   # → 64.0
```

---

### Ejercicio 6 — Calculadora de IMC 🏃
**Tipo:** Estático e instancia

Crea una clase `Persona` con atributos `nombre`, `peso` (kg) y `altura` (m). Añade:
- Un **método estático** `calcular_imc(peso, altura)` que retorne el IMC.
- Un **método estático** `clasificar_imc(imc)` que retorne la categoría: `"Bajo peso"`, `"Normal"`, `"Sobrepeso"` u `"Obesidad"`.
- Un **método de instancia** `reporte_imc()` que imprima el nombre, el IMC y la clasificación.

```python
# Uso esperado:
p = Persona("Ana", 65, 1.65)
p.reporte_imc()
# → Ana | IMC: 23.88 | Normal
```

---

### Ejercicio 7 — Jerarquía de empleados 🏢
**Tipo:** De clase e instancia

Crea una clase `Empleado` con atributos `nombre` y `salario`. Añade:
- Un **atributo de clase** `empresa` con el nombre de la empresa.
- Un **método de clase** `cambiar_empresa(nombre)` para actualizar la empresa.
- Un **método de instancia** `info()` que imprima el nombre, salario y empresa del empleado.

Luego crea una subclase `Gerente` que herede de `Empleado` y añada un atributo `departamento`. Sobreescribe `info()` para incluir el departamento.

```python
# Uso esperado:
Empleado.cambiar_empresa("TechCorp")
e = Empleado("Luis", 3000)
g = Gerente("María", 6000, "Tecnología")
e.info()   # → Luis | $3000 | TechCorp
g.info()   # → María | $6000 | TechCorp | Dpto: Tecnología
```

---

### Ejercicio 8 — Conversor de unidades 📐
**Tipo:** Estático

Crea una clase `Conversor` que **no tenga atributos de instancia** y contenga únicamente **métodos estáticos**:
- `km_a_millas(km)`
- `kg_a_libras(kg)`
- `litros_a_galones(litros)`

Cada método debe realizar la conversión y retornar el resultado redondeado a 2 decimales.

```python
# Uso esperado:
Conversor.km_a_millas(100)     # → 62.14
Conversor.kg_a_libras(70)      # → 154.32
Conversor.litros_a_galones(10) # → 2.64
```

---

### Ejercicio 9 — Registro de instancias 📋
**Tipo:** De clase e instancia

Crea una clase `Estudiante` que:
- Mantenga una **lista de clase** `todos` con todas las instancias creadas.
- Registre cada estudiante en `todos` al crearse (en `__init__`).
- Tenga un **método de clase** `listar_todos()` que imprima los nombres de todos los estudiantes.
- Tenga un **método de clase** `buscar(nombre)` que retorne la instancia con ese nombre, o `None` si no existe.
- Tenga un **método de instancia** `saludar()` que imprima un saludo personalizado.

```python
# Uso esperado:
Estudiante("Carlos")
Estudiante("Lucía")
Estudiante.listar_todos()     # → Carlos, Lucía
Estudiante.buscar("Lucía").saludar()   # → "¡Hola! Soy Lucía"
```

---

### Ejercicio 10 — Juego de dados 🎲
**Tipo:** Estático, de clase e instancia

Crea una clase `Dado` que:
- Tenga un **atributo de clase** `historial` (lista) con todos los resultados de tiradas.
- Tenga un **método estático** `tirar()` que retorne un número aleatorio entre 1 y 6.
- Tenga un **método de instancia** `lanzar()` que use `tirar()`, guarde el resultado en `historial` y lo retorne.
- Tenga un **método de clase** `promedio_historial()` que calcule y retorne el promedio de todas las tiradas registradas.

```python
# Uso esperado:
d1 = Dado()
d2 = Dado()
d1.lanzar()   # → (algún número entre 1 y 6)
d2.lanzar()
d1.lanzar()
Dado.promedio_historial()   # → promedio de las 3 tiradas
```

---

## 💡 Tips finales

- Cuando un método **no necesita acceder a `self` ni a `cls`**, probablemente deba ser `@staticmethod`.
- Cuando un método opera sobre **datos de la clase** (no del objeto), usa `@classmethod`.
- Cuando un método opera sobre **datos del objeto**, usa un método de instancia.
- Los métodos de clase son ideales para **constructores alternativos** (patrón factory).
