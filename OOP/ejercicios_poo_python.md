# Ejercicios de Programación Orientada a Objetos en Python

> **Analogía general:** Trabajamos con una **cafetería** y todo lo que la rodea: bebidas, pedidos, recetas, empleados, máquinas...

---

## 1. Clases y objetos

### Ejercicio 1.1 — La bebida

Crea una clase `Bebida` con los atributos `nombre`, `tamaño` (pequeño, mediano, grande) y `precio`. Instancia al menos tres bebidas distintas e imprime sus datos con un método `describir()`.

```python
# Resultado esperado:
# Café con leche | Tamaño: mediano | Precio: 2.50€
```

### Ejercicio 1.2 — La receta

Crea una clase `Receta` con los atributos `nombre`, `ingredientes` (una lista) y `tiempo_preparacion` (en minutos). Añade un método `es_rapida()` que devuelva `True` si se prepara en menos de 5 minutos. Crea varias recetas y filtra las rápidas.

---

## 2. Atributos de instancia vs. atributos de clase

### Ejercicio 2.1 — El mostrador de pedidos

Crea una clase `Pedido` con un **atributo de clase** `total_pedidos` que se incremente cada vez que se crea un nuevo pedido. Cada pedido tiene como **atributos de instancia** el `cliente` y la `bebida`. Crea varios pedidos y muestra cuántos se han hecho en total.

### Ejercicio 2.2 — Programa de fidelidad

Crea una clase `TarjetaFidelidad` con un atributo de clase `puntos_por_euro` (por ejemplo, 10 puntos por euro). Cada tarjeta tiene un `titular` y unos `puntos` acumulados. Añade un método `registrar_compra(euros)` que sume los puntos correspondientes. Modifica el atributo de clase a mitad del programa y observa cómo afecta a las siguientes compras.

---

## 3. Métodos de instancia, de clase y estáticos

### Ejercicio 3.1 — La máquina de café

Crea una clase `MaquinaCafe` cuyo `__init__` reciba `marca`, `modelo` y `capacidad_ml` (capacidad del depósito en mililitros). Implementa:

- Un **método de instancia** `preparar(bebida, cantidad_ml)` que compruebe si hay suficiente capacidad en el depósito, descuente la cantidad usada e imprima qué bebida está preparando esa máquina.
- Un **método de clase** `crear_estandar()` que devuelva una instancia con valores por defecto (marca="Genérica", modelo="Básica", capacidad_ml=1000).
- Un **método estático** `convertir_oz_a_ml(oz)` que convierta onzas a mililitros (1 oz ≈ 29.57 ml). Útil cuando una receta viene en onzas y necesitas saber cuántos ml descontar del depósito.

```python
maquina = MaquinaCafe.crear_estandar()
oz_necesarias = 8
ml = MaquinaCafe.convertir_oz_a_ml(oz_necesarias)  # ≈ 236.56 ml
maquina.preparar("Americano", ml)
# Preparando Americano (236.56 ml) en Genérica Básica. Depósito restante: 763.44 ml
```

### Ejercicio 3.2 — El turno de trabajo

Crea una clase `Turno` con atributos `empleado`, `hora_inicio` y `hora_fin`. Implementa:

- Un método de instancia `duracion()` que devuelva las horas trabajadas.
- Un método de clase `turno_mañana(empleado)` que cree un turno de 7:00 a 15:00.
- Un método estático `es_horario_valido(hora)` que compruebe si una hora está entre 0 y 23.

---

## 4. Encapsulación: getters y setters con `@property`

### Ejercicio 4.1 — El precio de la bebida

Crea una clase `Bebida` donde el precio sea un atributo **privado** (`_precio`). Usa `@property` para crear un **getter** que devuelva el precio formateado con €, y un **setter** que no permita asignar precios negativos ni superiores a 20€.

```python
cafe = Bebida("Espresso", 1.50)
print(cafe.precio)       # 1.50€
cafe.precio = 2.00       # OK
cafe.precio = -3          # Error: El precio no puede ser negativo
cafe.precio = 25          # Error: El precio no puede superar los 20€
```

### Ejercicio 4.2 — La temperatura de la leche

Crea una clase `Vaporizador` con un atributo privado `_temperatura`. El **getter** devuelve la temperatura en °C. El **setter** solo permite valores entre 50 y 90 grados (rango seguro para vaporizar leche). Añade un **deleter** que reinicie la temperatura a 65 (valor por defecto).

```python
v = Vaporizador()
v.temperatura = 75        # OK
v.temperatura = 120       # Error: Temperatura fuera de rango seguro (50-90°C)
del v.temperatura          # Se reinicia a 65°C
print(v.temperatura)       # 65
```

### Nota teórica — "Privado" en Python: un cartel, no un candado

En lenguajes como Java, `private` es una restricción real: el compilador impide el acceso desde fuera de la clase. En Python, la privacidad es una **convención social**, no una imposición técnica. La comunidad lo resume con la frase *"We're all consenting adults here"*.

Existen tres niveles de acceso, pero todos son técnicamente accesibles:

| Sintaxis | Significado | Analogía |
|---|---|---|
| `precio` | Público, acceso libre | Puerta abierta |
| `_precio` | "Privado" por convención | Cartel de "Solo personal autorizado" |
| `__precio` | Name mangling | Misma puerta, pero le han cambiado el nombre a la sala |

**¿Qué es el name mangling?**

Cuando usas doble guion bajo, Python no oculta el atributo: lo **renombra** internamente a `_NombreClase__atributo`. No puedes acceder con `objeto.__precio`, pero sí con `objeto._Bebida__precio`. Es una protección contra colisiones de nombres en herencia, no un mecanismo de seguridad.

```python
class Bebida:
    def __init__(self, precio):
        self.__precio = precio

cafe = Bebida(2.50)
# cafe.__precio          → AttributeError (no lo encuentra)
# cafe._Bebida__precio   → 2.50 (ahí estaba)
```

**Descubriendo lo "oculto" con `dir()` y `vars()`**

`dir(objeto)` muestra **todo**: métodos, atributos, dunders internos... sin importar el nivel de privacidad. Para filtrar el ruido:

```python
print([attr for attr in dir(cafe) if not attr.startswith('__')])
# ['_Bebida__precio']
```

`vars(objeto)` es aún más directo: muestra solo los atributos de instancia como diccionario.

```python
print(vars(cafe))
# {'_Bebida__precio': 2.50}
```

**Conclusión para el aula:** Haz dos versiones del mismo ejercicio (una con `_` y otra con `__`), y pide a los alumnos que usen `dir()` y `vars()` para inspeccionar los objetos. Verán con sus propios ojos que ambos atributos están ahí, accesibles si sabes dónde mirar. La privacidad en Python es un contrato de confianza entre programadores, no una barrera técnica.

---

## 5. Herencia

### Ejercicio 5.1 — Tipos de bebida

Crea una clase base `Bebida` con `nombre`, `tamaño` (pequeño, mediano, grande) y `precio`. Luego crea dos clases hijas:

- `BebidaCaliente` que añada el atributo `temperatura`.
- `BebidaFria` que añada el atributo `hielo` (booleano).

Ambas deben sobrescribir el método `describir()` para incluir su información extra.

### Ejercicio 5.2 — Empleados de la cafetería

Crea una clase base `Empleado` con `nombre` y `salario_base`. Crea dos subclases:

- `Barista` con un atributo extra `especialidad` y un método `preparar(tipo_cafe)` que imprima qué café está preparando y quién lo hace.
- `Encargado` con un atributo extra `turno` y un atributo `pedido_actual` (el tipo de café que debe prepararse). Añade un método `pedir_cafe(barista)` que le encargue al barista que prepare el `pedido_actual`.

Usa `super().__init__()` correctamente en ambas subclases.

---

## 6. Polimorfismo

### Ejercicio 6.1 — Procesando pedidos

Crea las clases `PedidoLocal`, `PedidoParaLlevar` y `PedidoDelivery`, todas con un método `calcular_total()`. Cada una calcula el total de forma distinta:

- `PedidoLocal`: precio base.
- `PedidoParaLlevar`: precio base + 0.20€ (envase).
- `PedidoDelivery`: precio base + 2.50€ (envío).

Crea una lista con pedidos variados y recórrela llamando a `calcular_total()` sin importar el tipo.

### Ejercicio 6.2 — Métodos de pago

Crea una clase base `MetodoPago` con un método `procesar(cantidad)`. Crea subclases `Efectivo`, `Tarjeta` y `AppMovil`. Cada una imprime un mensaje distinto al procesar. Crea una función `cobrar(metodo, cantidad)` que funcione con cualquiera de ellos.

---

## 7. Abstracción (clases abstractas)

### Ejercicio 7.1 — Electrodoméstico de cocina

Usa el módulo `abc` para crear una clase abstracta `Electrodomestico` con los métodos abstractos `encender()` y `apagar()`. Crea las subclases `Cafetera` y `Molinillo`, cada una con su propia implementación. Intenta instanciar `Electrodomestico` directamente y observa el error.

```python
from abc import ABC, abstractmethod
```

### Ejercicio 7.2 — Promoción

Crea una clase abstracta `Promocion` con un método abstracto `aplicar_descuento(precio)`. Crea las subclases:

- `Descuento2x1`: devuelve la mitad del precio.
- `DescuentoPorcentaje`: recibe un porcentaje en el constructor y lo aplica.
- `DescuentoFijo`: resta una cantidad fija.

Aplica las tres promociones al mismo precio y compara resultados.

---

## 8. Métodos mágicos / dunder methods

### Ejercicio 8.1 — Sumando pedidos

Crea una clase `Pedido` con un atributo `total`. Implementa:

- `__str__` para que `print(pedido)` muestre algo legible.
- `__add__` para que sumar dos pedidos devuelva un nuevo pedido con el total combinado.
- `__len__` para que devuelva el número de artículos.

```python
p1 = Pedido(["café", "tostada"], 4.50)
p2 = Pedido(["zumo"], 3.00)
p3 = p1 + p2
print(p3)        # Pedido: 3 artículos | Total: 7.50€
print(len(p3))   # 3
```

### Ejercicio 8.2 — Comparando recetas

Crea una clase `Receta` con `nombre` y `dificultad` (1-10). Implementa `__lt__`, `__eq__` y `__repr__` para poder ordenar una lista de recetas por dificultad con `sorted()`.

---

## 9. Composición

### Ejercicio 9.1 — La cafetería completa

Crea las clases `Bebida`, `Barista` y `Cafeteria`. La clase `Cafeteria` debe **contener** una lista de baristas y un menú (lista de bebidas). Añade métodos para contratar baristas, añadir bebidas al menú y mostrar el estado completo de la cafetería.

### Ejercicio 9.2 — El pedido con extras

Crea las clases `Extra` (con `nombre` y `precio`: sirope, nata, leche de avena...) y `Pedido` (con una `bebida` y una lista de `extras`). El método `total()` del pedido suma el precio de la bebida más todos los extras. Demuestra que modificar un extra se refleja en el pedido.

---

## 10. Herencia múltiple y MRO

### Ejercicio 10.1 — Empleado multitarea

Crea las clases `Cajero` (con método `cobrar()`), `Limpiador` (con método `limpiar()`) y `EmpleadoCompleto` que herede de ambas. Crea una instancia y llama a todos los métodos. Imprime el MRO con `EmpleadoCompleto.__mro__`.

### Ejercicio 10.2 — Bebida especial (problema del diamante)

Crea esta jerarquía:

```
       Producto
      /        \
BebidaBase   Postre
      \        /
    FrappePostre
```

Cada clase tiene un `__init__` que imprime su nombre. Usa `super()` en todas y observa el orden de inicialización. ¿Se llama dos veces a `Producto.__init__`? ¿Por qué?

---

## Resumen de conceptos

| Concepto | Idea clave |
|---|---|
| Clases y objetos | Molde → objeto concreto |
| Atributos clase/instancia | Compartido vs. propio |
| Tipos de métodos | instancia · clase · estático |
| Encapsulación (getter/setter) | Controlar el acceso a los datos |
| Herencia | Reutilizar y especializar |
| Polimorfismo | Mismo método, distinto comportamiento |
| Abstracción | Definir contratos, no implementaciones |
| Métodos mágicos | Personalizar operadores y funciones |
| Composición | "Tiene un" en vez de "es un" |
| Herencia múltiple | Combinar capacidades, entender el MRO |
