# Guía Rápida: Módulo `zipfile` en Python

## 1. Descomprimir un ZIP

### Extraer todo
```python
import zipfile

with zipfile.ZipFile('archivo.zip', 'r') as zip_ref:
    zip_ref.extractall('carpeta_destino/')
```

### Extraer archivo específico
```python
with zipfile.ZipFile('archivo.zip', 'r') as zip_ref:
    zip_ref.extract('archivo.csv', 'carpeta_destino/')
```

## 2. Comprimir archivos

### Comprimir un archivo
```python
import zipfile

with zipfile.ZipFile('salida.zip', 'w') as zip_ref:
    zip_ref.write('archivo.csv')
```

### Comprimir carpeta completa
```python
import zipfile
import os

def comprimir_carpeta(carpeta, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as zip_ref:
        for archivo in os.listdir(carpeta):
            ruta = os.path.join(carpeta, archivo)
            if os.path.isfile(ruta):
                zip_ref.write(ruta, arcname=archivo)

comprimir_carpeta('datos/', 'datos.zip')
```

## 3. Listar contenido de un ZIP

```python
with zipfile.ZipFile('archivo.zip', 'r') as zip_ref:
    # Ver lista de archivos
    print(zip_ref.namelist())
    
    # Ver información detallada
    for info in zip_ref.infolist():
        print(f"{info.filename} - {info.file_size} bytes")
```

## 4. Leer archivo dentro del ZIP sin extraer

```python
with zipfile.ZipFile('archivo.zip', 'r') as zip_ref:
    contenido = zip_ref.read('archivo.txt').decode('utf-8')
    print(contenido)
```

## 5. Parámetros comunes

```python
# Modos
'r'  # Leer
'w'  # Escribir (crea nuevo)
'a'  # Añadir

# Compresión
zipfile.ZIP_DEFLATED  # Con compresión (por defecto)
zipfile.ZIP_STORED    # Sin compresión
```

## Ejemplo práctico: Flujo estudiantes

```python
import zipfile
import os

# Descomprimir materiales
with zipfile.ZipFile('curso_python.zip', 'r') as zip_ref:
    zip_ref.extractall('materiales/')

# Acceder a los archivos
if os.path.exists('materiales/datos/transacciones.csv'):
    print("✅ Archivos listos para usar")
```

---

**Nota:** Para carpetas complejas con subcarpetas, `extractall()` preserva la estructura automáticamente. 📦
