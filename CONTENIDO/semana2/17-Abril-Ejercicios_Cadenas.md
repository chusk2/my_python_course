# Ejercicios — Viernes 17/04: Manipulación y Formateo de Cadenas de Texto

---

## Ejercicios Básicos (1–5)

---

### Ejercicio 1: Información de una cadena

Pide al usuario una frase y muestra: la frase en mayúsculas, en minúsculas, su longitud, su primera letra y su última letra.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 1: Información de una cadena
frase = input("Escribe una frase: ")

print(f"Mayúsculas:    {frase.upper()}")
print(f"Minúsculas:    {frase.lower()}")
print(f"Longitud:      {len(frase)} caracteres")
print(f"Primera letra: {frase[0]}")
print(f"Última letra:  {frase[-1]}")
```

</details>

---

### Ejercicio 2: Contador de vocales y consonantes

Pide una frase al usuario y cuenta cuántas vocales y cuántas consonantes tiene (ignora espacios, números y signos).

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 2: Contador de vocales y consonantes
frase = input("Escribe una frase: ").lower()

vocales = 0
consonantes = 0

for letra in frase:
    if letra in "aeiouáéíóü":
        vocales += 1
    elif letra.isalpha():  # Es letra pero no vocal → consonante
        consonantes += 1

print(f"Vocales: {vocales}")
print(f"Consonantes: {consonantes}")
```

</details>

---

### Ejercicio 3: Invertir una frase

Pide una frase al usuario y muéstrala al revés usando slicing.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 3: Invertir una frase
frase = input("Escribe una frase: ")

# Usamos slicing con paso -1 para invertir
frase_invertida = frase[::-1]

print(f"Original:  {frase}")
print(f"Invertida: {frase_invertida}")
```

</details>

---

### Ejercicio 4: Reemplazar palabras

Pide una frase, una palabra a buscar y una palabra de reemplazo. Muestra la frase resultante y cuántas sustituciones se hicieron.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 4: Reemplazar palabras
frase = input("Escribe una frase: ")
buscar = input("Palabra a buscar: ")
reemplazo = input("Reemplazar por: ")

# Contamos apariciones antes de reemplazar
apariciones = frase.lower().count(buscar.lower())

# Reemplazamos
nueva_frase = frase.replace(buscar, reemplazo)

print(f"Resultado: {nueva_frase}")
print(f"Se hicieron {apariciones} sustituciones.")
```

</details>

---

### Ejercicio 5: Extraer datos de un DNI

Pide al usuario su DNI (formato 12345678A). Extrae el número y la letra por separado usando slicing. Muestra cada parte.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 5: Extraer datos de un DNI
dni = input("Introduce tu DNI (ej: 12345678A): ").strip().upper()

# Extraemos número y letra con slicing
numero = dni[:-1]    # Todo menos el último carácter
letra = dni[-1]      # Último carácter

print(f"DNI completo: {dni}")
print(f"Número:       {numero}")
print(f"Letra:        {letra}")
```

</details>

---

## Ejercicios de Nivel Medio (6–8)

---

### Ejercicio 6: Generador de acrónimos

Pide al usuario una frase y genera su acrónimo (las iniciales de cada palabra en mayúsculas). Por ejemplo, "Organización de las Naciones Unidas" → "ONU" (ignorando palabras cortas como "de", "las", "y", "el", "la", "en", "los").

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 6: Generador de acrónimos
frase = input("Escribe una frase: ")

# Palabras que ignoramos (artículos, preposiciones comunes)
ignorar = ["de", "del", "las", "los", "la", "el", "en", "y", "a", "e", "o", "u"]

# Dividimos la frase en palabras
palabras = frase.split()

acronimo = ""
for palabra in palabras:
    # Si la palabra (en minúsculas) no está en la lista de ignoradas
    if palabra.lower() not in ignorar:
        acronimo += palabra[0].upper()  # Añadimos la inicial en mayúsculas

print(f"Frase: {frase}")
print(f"Acrónimo: {acronimo}")
```

</details>

---

### Ejercicio 7: Cifrado César

Implementa un cifrado César sencillo para mensajes en minúsculas. El cifrado César desplaza cada letra un número fijo de posiciones en el alfabeto. Pide al usuario un mensaje y un desplazamiento. Cifra el mensaje (solo letras minúsculas; espacios y otros caracteres se mantienen igual).

**Pista**: Usa `ord()` para obtener el código numérico de un carácter y `chr()` para convertirlo de vuelta.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 7: Cifrado César
mensaje = input("Mensaje a cifrar: ").lower()
desplazamiento = int(input("Desplazamiento (1-25): "))

mensaje_cifrado = ""

for caracter in mensaje:
    if caracter.isalpha():
        # Obtenemos la posición relativa (a=0, b=1, ..., z=25)
        posicion = ord(caracter) - ord('a')
        # Desplazamos y volvemos al rango 0-25 con módulo
        nueva_posicion = (posicion + desplazamiento) % 26
        # Convertimos de vuelta a carácter
        nuevo_caracter = chr(nueva_posicion + ord('a'))
        mensaje_cifrado += nuevo_caracter
    else:
        # Espacios, números y signos se mantienen
        mensaje_cifrado += caracter

print(f"Original: {mensaje}")
print(f"Cifrado:  {mensaje_cifrado}")
```

</details>

---

### Ejercicio 8: Analizador de logs de servidor web

Dado un registro de log de servidor web en formato texto (una cadena con varias líneas), extrae y muestra información relevante. El formato de cada línea es:

```
IP;FECHA;MÉTODO;RUTA;CÓDIGO
```

El programa recibe los datos como una cadena multilínea (simulada en el código), y para cada línea extrae los campos con `.split()`. Al final muestra cuántas peticiones hubo, cuántas fueron exitosas (código 200), cuántas errores (código 404 o 500) y qué IPs aparecen.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 8: Analizador de logs de servidor web
# Simulamos un log multilínea (en la realidad vendría de un archivo)
log = """192.168.1.10;2026-04-17;GET;/inicio;200
192.168.1.15;2026-04-17;POST;/login;200
10.0.0.5;2026-04-17;GET;/productos;200
192.168.1.10;2026-04-17;GET;/admin;404
10.0.0.5;2026-04-17;GET;/contacto;200
172.16.0.1;2026-04-17;POST;/api/datos;500
192.168.1.15;2026-04-17;GET;/perfil;200
172.16.0.1;2026-04-17;GET;/inicio;200
10.0.0.5;2026-04-17;GET;/nosotros;404
192.168.1.10;2026-04-17;GET;/inicio;200"""

# Dividimos el log en líneas
lineas = log.strip().split("\n")

# Contadores
total = 0
exitosas = 0
errores_404 = 0
errores_500 = 0
ips_vistas = ""  # Guardamos IPs únicas como texto (sin usar sets aún)

print("=== ANÁLISIS DE LOG DEL SERVIDOR ===\n")

for linea in lineas:
    # Extraemos los campos con split
    campos = linea.split(";")
    ip = campos[0]
    fecha = campos[1]
    metodo = campos[2]
    ruta = campos[3]
    codigo = campos[4]

    total += 1

    # Contamos por código de respuesta
    if codigo == "200":
        exitosas += 1
    elif codigo == "404":
        errores_404 += 1
    elif codigo == "500":
        errores_500 += 1

    # Guardamos IPs únicas (comprobamos si ya está en nuestra lista)
    if ip not in ips_vistas:
        if ips_vistas:
            ips_vistas += ", " + ip
        else:
            ips_vistas = ip

# Calculamos porcentaje de éxito
pct_exito = (exitosas / total) * 100 if total > 0 else 0

# Mostramos el informe
print("=" * 40)
print("    INFORME DE TRÁFICO WEB")
print("=" * 40)
print(f"Total peticiones:       {total}")
print(f"Exitosas (200):         {exitosas} ({pct_exito:.1f}%)")
print(f"No encontrado (404):    {errores_404}")
print(f"Error servidor (500):   {errores_500}")
print(f"IPs registradas:        {ips_vistas}")
print("=" * 40)
```

</details>

---

## Ejercicios de Nivel Superior (9–10)

---

### Ejercicio 9: Validador y formateador de datos personales

Crea un programa que pida los siguientes datos, los valide y los formatee correctamente:

- Nombre completo (al menos 2 palabras, solo letras y espacios)
- Email (debe contener @ y al menos un punto después de la @)
- Teléfono (debe tener 9 dígitos, puede empezar con +34)
- IBAN (debe empezar por "ES" y tener 24 caracteres)

Si un dato no es válido, informa del error y pide que lo introduzca de nuevo (bucle `while`). Al final, muestra todos los datos limpios y formateados. Integra bucles, condicionales, y todos los métodos de cadenas.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 9: Validador y formateador de datos personales
print("=== FORMULARIO DE DATOS PERSONALES ===\n")

# --- Nombre ---
while True:
    nombre = input("Nombre completo: ").strip()
    # Comprobamos que tenga al menos 2 palabras
    palabras = nombre.split()
    # Comprobamos que solo contenga letras y espacios
    solo_letras = nombre.replace(" ", "").isalpha()

    if len(palabras) >= 2 and solo_letras:
        nombre = nombre.title()  # Formateamos: primera letra de cada palabra en mayúscula
        break
    else:
        print("  Error: introduce nombre y al menos un apellido (solo letras).\n")

# --- Email ---
while True:
    email = input("Email: ").strip().lower()
    arroba_pos = email.find("@")
    # La @ debe existir y no estar al principio ni al final
    # Debe haber un punto después de la @
    if arroba_pos > 0 and "." in email[arroba_pos:] and not email.endswith("."):
        break
    else:
        print("  Error: el email debe contener @ y un punto en el dominio.\n")

# --- Teléfono ---
while True:
    telefono = input("Teléfono: ").strip()
    # Limpiamos: quitamos espacios, guiones y el prefijo +34
    telefono_limpio = telefono.replace(" ", "").replace("-", "")
    if telefono_limpio.startswith("+34"):
        telefono_limpio = telefono_limpio[3:]

    if len(telefono_limpio) == 9 and telefono_limpio.isdigit():
        # Formateamos como XXX XXX XXX
        telefono_formato = (
            telefono_limpio[:3] + " " +
            telefono_limpio[3:6] + " " +
            telefono_limpio[6:]
        )
        break
    else:
        print("  Error: el teléfono debe tener 9 dígitos.\n")

# --- IBAN ---
while True:
    iban = input("IBAN: ").strip().replace(" ", "").upper()

    if iban.startswith("ES") and len(iban) == 24 and iban[2:].isdigit():
        # Formateamos en grupos de 4
        iban_formato = ""
        for i in range(0, len(iban), 4):
            iban_formato += iban[i:i+4] + " "
        iban_formato = iban_formato.strip()
        break
    else:
        print("  Error: el IBAN debe empezar por ES y tener 24 caracteres.\n")

# --- Resumen ---
print()
print("=" * 45)
print("    DATOS REGISTRADOS CORRECTAMENTE")
print("=" * 45)
print(f"Nombre:    {nombre}")
print(f"Email:     {email}")
print(f"Teléfono:  {telefono_formato}")
print(f"IBAN:      {iban_formato}")
print("=" * 45)
```

</details>

---

### Ejercicio 10: Analizador de texto completo

Crea un programa que pida al usuario un texto largo (puede ser un párrafo o varias oraciones) y genere un informe completo de análisis:

1. Número total de caracteres (con y sin espacios)
2. Número de palabras
3. Número de oraciones (contando puntos, signos de interrogación y exclamación)
4. Longitud media de las palabras
5. La palabra más larga y la más corta
6. Las 5 palabras más frecuentes
7. El texto formateado a un ancho de 50 caracteres por línea

Integra todos los métodos de cadenas, bucles, condicionales, contadores, acumuladores y f-strings.

<details>
<summary>Ver solución</summary>

```python
# Ejercicio 10: Analizador de texto completo
print("=== ANALIZADOR DE TEXTO ===")
print("Introduce un texto (puede ser largo):")
texto = input()

# 1. Caracteres
total_caracteres = len(texto)
sin_espacios = len(texto.replace(" ", ""))

# 2. Palabras
# Limpiamos signos de puntuación para contar palabras correctamente
texto_limpio = texto
for signo in ".,;:!?¿¡()\"'-":
    texto_limpio = texto_limpio.replace(signo, "")
palabras = texto_limpio.split()
num_palabras = len(palabras)

# 3. Oraciones (contamos ., !, ?)
num_oraciones = 0
for caracter in texto:
    if caracter in ".!?":
        num_oraciones += 1
# Si no hay signos de puntuación, al menos hay 1 oración
if num_oraciones == 0 and num_palabras > 0:
    num_oraciones = 1

# 4. Longitud media de las palabras
total_longitud = 0
for palabra in palabras:
    total_longitud += len(palabra)
media_longitud = total_longitud / num_palabras if num_palabras > 0 else 0

# 5. Palabra más larga y más corta
mas_larga = ""
mas_corta = None

for palabra in palabras:
    if len(palabra) > len(mas_larga):
        mas_larga = palabra
    if mas_corta is None or len(palabra) < len(mas_corta):
        mas_corta = palabra

# 6. Palabras más frecuentes
# Usamos un enfoque sin diccionarios: para cada palabra contamos y guardamos
# (Esto se simplificará mucho en la semana 3 con diccionarios)
palabras_lower = []
for p in palabras:
    palabras_lower.append(p.lower())

# Encontramos las más frecuentes buscando la que más se repite, luego la siguiente...
top_5 = ""
palabras_contadas = ""  # Para no contar la misma dos veces

for ronda in range(5):
    max_conteo = 0
    max_palabra = ""

    for p in palabras_lower:
        if p in palabras_contadas:
            continue
        conteo = 0
        for p2 in palabras_lower:
            if p2 == p:
                conteo += 1
        if conteo > max_conteo:
            max_conteo = conteo
            max_palabra = p

    if max_palabra:
        if top_5:
            top_5 += f", {max_palabra} ({max_conteo})"
        else:
            top_5 = f"{max_palabra} ({max_conteo})"
        palabras_contadas += max_palabra + " "

# 7. Formateo a 50 caracteres por línea
ancho = 50
texto_formateado = ""
linea_actual = ""

for palabra in texto.split():
    if len(linea_actual) + len(palabra) + 1 <= ancho:
        if linea_actual:
            linea_actual += " " + palabra
        else:
            linea_actual = palabra
    else:
        texto_formateado += linea_actual + "\n"
        linea_actual = palabra
if linea_actual:
    texto_formateado += linea_actual

# Mostramos el informe
print()
print("=" * 50)
print("         INFORME DE ANÁLISIS DE TEXTO")
print("=" * 50)
print(f"Caracteres totales:       {total_caracteres}")
print(f"Caracteres sin espacios:  {sin_espacios}")
print(f"Palabras:                 {num_palabras}")
print(f"Oraciones:                {num_oraciones}")
print(f"Longitud media palabra:   {media_longitud:.1f} caracteres")
print(f"Palabra más larga:        '{mas_larga}' ({len(mas_larga)} car.)")
if mas_corta:
    print(f"Palabra más corta:        '{mas_corta}' ({len(mas_corta)} car.)")
print(f"Top 5 palabras frecuentes: {top_5}")
print()
print("--- Texto formateado (50 car/línea) ---")
print(texto_formateado)
print("=" * 50)
```

</details>

---

*Estos ejercicios integran todos los métodos de cadenas, slicing, f-strings, bucles `for` y `while`, condicionales, `break`/`continue`, contadores, acumuladores y conversión de tipos. Los ejercicios 9 y 10 combinan todos los conceptos de las dos primeras semanas.*
