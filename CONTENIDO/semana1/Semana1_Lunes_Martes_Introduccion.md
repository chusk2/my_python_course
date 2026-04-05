# Semana 1 — Lunes 06/04 y Martes 07/04

## Introducción a la Programación, Algoritmos y Entorno de Trabajo

---

## 1. ¿Qué es programar?

Programar es darle instrucciones a un ordenador para que resuelva un problema o realice una tarea. Piensa en una receta de cocina: tú escribes los pasos y el ordenador los ejecuta, uno a uno, sin saltarse ninguno.

La diferencia con una receta real es que el ordenador es **extremadamente literal**: hace exactamente lo que le dices, ni más ni menos. Si olvidas un paso o lo escribes mal, el resultado no será el esperado.

### ¿Por qué aprender a programar?

- **Automatización**: tareas repetitivas que haces cada día (renombrar archivos, enviar correos, organizar datos en Excel) pueden resolverse con unas pocas líneas de código.
- **Análisis de datos**: extraer conclusiones de grandes cantidades de información.
- **Empleabilidad**: la programación es una de las habilidades más demandadas en el mercado laboral actual, independientemente del sector.
- **Pensamiento lógico**: aprender a programar mejora tu capacidad para resolver problemas de forma estructurada.

---

## 2. ¿Qué es un algoritmo?

Un **algoritmo** es una secuencia finita de pasos ordenados para resolver un problema. Los usamos a diario sin darnos cuenta:

**Ejemplo cotidiano — Preparar un café:**

1. Coger una taza del armario.
2. Encender la cafetera.
3. Poner la cápsula o el café molido.
4. Pulsar el botón de preparar.
5. Esperar a que termine.
6. Retirar la taza.

**Características de un buen algoritmo:**

- **Preciso**: cada paso está claramente definido.
- **Finito**: tiene un inicio y un final.
- **Ordenado**: los pasos se ejecutan en una secuencia lógica.
- **Definido**: ante los mismos datos de entrada, siempre produce el mismo resultado.

### Ejercicio mental

Intenta escribir el algoritmo para "cruzar un paso de peatones con semáforo". Verás que necesitas contemplar decisiones (¿está en verde o en rojo?) y repeticiones (esperar hasta que cambie).

---

## 3. Lógica básica de programación

Todos los programas, desde una calculadora hasta una red social, se construyen combinando tres estructuras fundamentales:

| Estructura      | Qué hace                                        | Ejemplo cotidiano                      |
|-----------------|--------------------------------------------------|----------------------------------------|
| **Secuencia**   | Ejecutar instrucciones una tras otra             | Seguir los pasos de una receta         |
| **Decisión**    | Elegir un camino según una condición             | Si llueve, cojo el paraguas            |
| **Repetición**  | Repetir un bloque de instrucciones               | Remover la salsa cada 2 minutos        |

Estas tres estructuras son la base de **cualquier** lenguaje de programación.

---

## 4. ¿Qué es Python y por qué lo usamos?

**Python** es un lenguaje de programación creado en 1991 por Guido van Rossum. Sus características principales son:

- **Sintaxis sencilla y legible**: se parece mucho al lenguaje natural (en inglés).
- **Multiuso**: sirve para automatización, análisis de datos, inteligencia artificial, desarrollo web, scripting y mucho más.
- **Gran comunidad**: miles de bibliotecas gratuitas disponibles y una comunidad enorme que resuelve dudas.
- **Demanda laboral**: empresas como Google, Netflix, Spotify o Instagram usan Python en sus sistemas.

### Python vs. otros lenguajes

| Característica        | Python           | Java             | JavaScript       |
|-----------------------|------------------|------------------|------------------|
| Dificultad inicial    | Baja             | Media-Alta       | Media            |
| Legibilidad           | Muy alta         | Media            | Media            |
| Uso principal         | Datos, IA, auto. | Apps empresar.   | Web              |
| Tipado                | Dinámico         | Estático         | Dinámico         |

---

## 5. Arquitectura básica del ordenador

Para entender qué ocurre cuando ejecutamos un programa, es útil conocer los componentes principales de un ordenador:

- **CPU (Procesador)**: el "cerebro" que ejecuta las instrucciones. Cuando Python ejecuta `2 + 3`, es la CPU quien hace el cálculo.
- **RAM (Memoria)**: almacenamiento temporal y rápido. Cuando creamos una variable, se guarda aquí mientras el programa se ejecuta.
- **Disco duro / SSD**: almacenamiento permanente. Aquí están tus archivos `.py` guardados.
- **Entrada/Salida**: teclado, ratón, pantalla, impresora... todo lo que permite comunicarte con el ordenador.

### ¿Cómo se ejecuta un programa en Python?

```
Archivo .py (disco) → Intérprete de Python (CPU + RAM) → Resultado (pantalla)
```

Python es un lenguaje **interpretado**: un programa llamado "intérprete" lee tu código línea a línea y lo ejecuta. No necesitas un paso previo de compilación como en C o Java.

---

## 6. Instalación del entorno de trabajo

Vamos a preparar tres herramientas para trabajar durante el curso. Puedes elegir trabajar en local (Python + VS Code) o en la nube (Google Colab). Recomendamos tener ambas opciones configuradas.

### 6.1 Instalar Python en Windows

1. Ve a [python.org/downloads](https://www.python.org/downloads/).
2. Descarga la última versión estable de Python 3.
3. **MUY IMPORTANTE**: Marca la casilla **"Add python.exe to PATH"** antes de hacer clic en "Install Now".
4. Una vez instalado, abre una terminal (PowerShell o CMD) y escribe:

```
python --version
```

Si aparece algo como `Python 3.x.x`, la instalación ha sido correcta.

### 6.2 Instalar Visual Studio Code

1. Ve a [code.visualstudio.com](https://code.visualstudio.com/).
2. Descarga e instala la versión para tu sistema operativo.
3. Abre VS Code e instala la extensión **Python** (de Microsoft) desde el panel de extensiones (icono de cuadrados en la barra lateral o `Ctrl+Shift+X`).
4. Opcional pero recomendado: instala la extensión **Spanish Language Pack** para tener la interfaz en español.

### 6.3 Google Colab (sin instalar nada)

Google Colab es un entorno en la nube que permite escribir y ejecutar código Python directamente desde el navegador. Solo necesitas una cuenta de Google.

1. Ve a [colab.research.google.com](https://colab.research.google.com/).
2. Haz clic en **"Nuevo cuaderno"**.
3. Escribe código en las celdas y pulsa `Shift + Enter` para ejecutar.

**Ventajas de Colab**: no requiere instalación, funciona en cualquier sistema operativo, permite compartir cuadernos fácilmente y guarda todo en Google Drive.

---

## 7. Vídeos recomendados (en español)

### Instalación de Python en Windows

- **Cómo Instalar Python en Windows — Paso a paso**
  [https://www.youtube.com/watch?v=uxmMEqYEMlY](https://www.youtube.com/watch?v=uxmMEqYEMlY)

- **Instalación de Python desde cero (Python.org + verificación)**
  [https://www.youtube.com/watch?v=ePM8wAGMKMw](https://www.youtube.com/watch?v=ePM8wAGMKMw)

### Instalación de Visual Studio Code + extensión Python

- **Instalar Visual Studio Code y configurar Python — Tutorial completo**
  [https://www.youtube.com/watch?v=K5pTIB1gZOo](https://www.youtube.com/watch?v=K5pTIB1gZOo)

- **Visual Studio Code para Python — Configuración inicial**
  [https://www.youtube.com/watch?v=CSerCiVekPs](https://www.youtube.com/watch?v=CSerCiVekPs)

### Google Colab (funciona en cualquier sistema operativo)

- **Google Colab desde cero — Tutorial para principiantes**
  [https://www.youtube.com/watch?v=8VFYs3Ot_aA](https://www.youtube.com/watch?v=8VFYs3Ot_aA)

- **Primeros pasos en Google Colab con Python**
  [https://www.youtube.com/watch?v=ZG6seRKEPig](https://www.youtube.com/watch?v=ZG6seRKEPig)

> **Nota**: Los vídeos pueden hacer referencia a versiones ligeramente anteriores de Python o VS Code, pero los pasos son esencialmente los mismos. Lo importante es asegurarse de marcar "Add to PATH" al instalar Python y de instalar la extensión de Python en VS Code.

---

## 8. Tu primer programa en Python

Una vez tengas el entorno preparado (ya sea VS Code o Google Colab), escribe y ejecuta lo siguiente:

```python
print("¡Hola, mundo! Este es mi primer programa en Python")
```

Si ves el mensaje en pantalla, **¡felicidades!** Tu entorno de trabajo está correctamente configurado y estás listo para empezar a programar.

### Probemos algo más:

```python
# Esto es un comentario: Python lo ignora
print("Me llamo Python y sé hacer cálculos:")
print(2 + 3)
print(10 * 5)
print("¡Nos vemos en la siguiente clase!")
```

---

## Resumen de la sesión

| Concepto                  | Idea clave                                                |
|---------------------------|-----------------------------------------------------------|
| Programar                 | Dar instrucciones precisas a un ordenador                 |
| Algoritmo                 | Secuencia finita y ordenada de pasos                      |
| Estructuras básicas       | Secuencia, decisión y repetición                          |
| Python                    | Lenguaje interpretado, legible y multiuso                 |
| Intérprete                | Programa que lee y ejecuta código Python línea a línea    |
| VS Code                   | Editor de código profesional con extensiones              |
| Google Colab              | Entorno Python en la nube, sin instalación                |

---

*Siguiente clase: Jueves 09/04 — Sintaxis básica, entrada y salida de datos y buenas prácticas iniciales.*
