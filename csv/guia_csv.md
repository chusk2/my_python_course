# Guía Rápida: Módulo CSV en Python

## 1. Leer un CSV

### Lectura simple con `csv.reader()`
```python
import csv

with open('datos.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)  # Cada fila es una lista
```

### Lectura como diccionarios con `csv.DictReader()`
```python
with open('datos.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila)  # Cada fila es un diccionario
        print(fila['nombre'])  # Acceso por columna
```

## 2. Escribir un CSV

### Escritura simple con `csv.writer()`
```python
with open('salida.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['nombre', 'edad', 'ciudad'])
    escritor.writerow(['Ana', 25, 'Madrid'])
    escritor.writerow(['Bob', 30, 'Barcelona'])
```

### Escritura como diccionarios con `csv.DictWriter()`
```python
with open('salida.csv', 'w', newline='', encoding='utf-8') as archivo:
    campos = ['nombre', 'edad', 'ciudad']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    
    escritor.writeheader()  # Escribir encabezados
    escritor.writerow({'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'})
    escritor.writerow({'nombre': 'Bob', 'edad': 30, 'ciudad': 'Barcelona'})
```

## 3. Parámetros comunes

```python
# Delimitador personalizado
lector = csv.reader(archivo, delimiter=';')  # Para CSV con ;

# Entrecomillado
escritor = csv.writer(archivo, quoting=csv.QUOTE_ALL)  # Entrecomilla todo
escritor = csv.writer(archivo, quoting=csv.QUOTE_MINIMAL)  # Solo si necesario

# Salto de línea (importante en Windows)
with open('datos.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
```

## 4. Ejemplo práctico completo

```python
import csv

# Leer y procesar
datos = []
with open('entrada.csv', 'r', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        fila['edad'] = int(fila['edad'])
        datos.append(fila)

# Escribir resultado
with open('salida.csv', 'w', newline='', encoding='utf-8') as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'edad', 'ciudad'])
    escritor.writeheader()
    escritor.writerows(datos)
```

## 5. Consejos prácticos

- **Encoding:** Usa `encoding='utf-8'` para caracteres acentuados (español)
- **Newline:** Siempre usa `newline=''` al escribir para evitar líneas en blanco extras
- **pandas:** Para operaciones complejas, usa `pd.read_csv()` y `pd.to_csv()` (más poderoso)
- **DictReader vs reader:** DictReader es mejor cuando necesitas acceso por nombre de columna

---

**Tip:** `csv.reader()` es más rápido para archivos grandes, `csv.DictReader()` es más legible. Elige según tu necesidad. 📊
