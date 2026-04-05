# Guía de Gestión de Archivos en Python

Esta guía resume los conceptos fundamentales para la lectura, escritura y manipulación de archivos y directorios en Python, basados en el módulo estándar `pathlib`.

---

## 1. Archivos y el Sistema de Archivos

* **¿Qué es un archivo?** Un archivo es, en última instancia, una secuencia de bytes. Cada byte en un archivo puede concebirse como un entero con un valor entre 0 y 255. No hay nada intrínseco en el archivo que dicte cómo deben interpretarse sus contenidos; esto depende de cómo se decodifiquen.
* **El Sistema de Archivos:** Proporciona una representación abstracta de los archivos almacenados y se encarga de interactuar con los dispositivos para controlar el almacenamiento y recuperación de datos. Diferentes sistemas operativos utilizan distintos sistemas de archivos.
* **Jerarquía:** Los sistemas de archivos organizan los archivos en una jerarquía de directorios (carpetas) que parten de un directorio principal llamado directorio raíz.
* **Rutas de Archivos:** La manera de ubicar un archivo enumerando los directorios desde la raíz hasta el nombre del archivo se denomina "ruta de archivo". En macOS y Linux, la raíz se representa con una barra inclinada (`/`). En Windows, cada dispositivo tiene un directorio raíz único representado por una letra de unidad y una barra invertida (`\`).

---

## 2. Trabajando con Rutas (`pathlib`)

Para gestionar de forma segura y multiplataforma las rutas, Python ofrece el módulo estándar `pathlib`.

### Creación de Objetos `Path`
* **A partir de una cadena:** `pathlib.Path("/ruta/al/archivo.txt")`. En Windows, para evitar errores por secuencias de escape, se pueden usar barras inclinadas (`/`) o prefijar la cadena con `r` (cadena cruda) .
* **Métodos de clase especiales:**
    * `Path.home()`: Devuelve un objeto que representa el directorio de usuario actual].
    * `Path.cwd()`: Devuelve el directorio de trabajo actual (Current Working Directory).
* **Operador `/`:** Permite extender una ruta existente combinando objetos `Path` con cadenas u otros objetos `Path`.

### Rutas Absolutas vs. Relativas
* Una ruta que comienza en el directorio raíz se denomina absoluta.
* Una ruta que no es absoluta se llama ruta relativa. Estas cobran sentido al considerarse dentro del contexto de otro directorio.
* Puedes comprobar si una ruta es absoluta con el método `.is_absolute().

### Componentes de una Ruta
Una vez creado el objeto `Path`, puedes inspeccionar sus partes:
* `.parents`: Devuelve un iterable con la lista de directorios en la ruta, en orden inverso.
* `.parent`: Devuelve el nombre del primer directorio padre en la ruta.
* `.anchor`: Devuelve el directorio raíz de la ruta (si es absoluta).
* `.name`: Nombre del archivo o directorio al que apunta la ruta.
* `.stem`: El nombre del archivo sin la extensión (a la izquierda del punto).
* `.suffix`: La extensión del archivo (a la derecha del punto).

### Verificación de Existencia
* `.exists()`: Devuelve `True` o `False` dependiendo de si la ruta existe en la máquina.
* `.is_file()`: Comprueba si la ruta hace referencia a un archivo.
* `.is_dir()`: Comprueba si la ruta hace referencia a un directorio.

---

## 3. Operaciones Comunes del Sistema de Archivos

### Creación de Directorios y Archivos
* **Crear Directorio:** Usa `Path.mkdir()`. Para crear múltiples niveles de directorios simultáneamente, usa el argumento `parents=True`. Para evitar excepciones si el directorio ya existe, usa `exist_ok=True`.
    * *Patrón común:* `ruta.mkdir(parents=True, exist_ok=True)`.
* **Crear Archivo:** Usa `Path.touch()` para crear un archivo vacío. A diferencia de `.mkdir()`, `.touch()` no tiene un parámetro para crear carpetas padre; estas deben existir previamente. No lanza un error si el archivo ya existe.

### Iteración y Búsqueda
* **Iterar contenidos directos:** `Path.iterdir()` devuelve un iterador de objetos `Path` con cada elemento del directorio (archivos y subcarpetas inmediatos).
* **Búsqueda con patrones (`glob`):** `Path.glob(patrón)` devuelve elementos que cumplan ciertos criterios utilizando caracteres comodín.
    * `*`: Coincide con cualquier número de caracteres.
    * `?`: Coincide con un solo carácter.
    * `[abc]`: Coincide con uno de los caracteres específicos entre los corchetes.
* **Búsqueda recursiva:** Usando el prefijo `**/` con `.glob()` o utilizando el método simplificado `.rglob()`, puedes buscar recursivamente en el directorio actual y todos sus subdirectorios.

### Mover, Renombrar y Eliminar
* **Mover/Renombrar:** `ruta_origen.replace(ruta_destino)`. Si el destino ya existe, será sobrescrito sin lanzar ninguna excepción, por lo que debe hacerse con precaución.
* **Eliminar archivo:** `Path.unlink()`. Si la ruta no existe, lanza un `FileNotFoundError` a menos que se use `missing_ok=True`.
* **Eliminar directorio:** `Path.rmdir()`. Sólo funciona si el directorio está vacío.
* **Eliminar árbol de directorios (no vacío):** Es necesario utilizar la función `rmtree()` del módulo estándar `shutil` (`shutil.rmtree()`).

---

## 4. Lectura y Escritura de Archivos

Para poder interpretar la secuencia de bytes de un archivo de texto, Python necesita aplicar una codificación (encoding) durante el proceso de apertura. UTF-8 es una de las codificaciones de caracteres más utilizadas porque puede representar un rango mucho mayor de caracteres que ASCII.

### Apertura de Archivos (La declaración `with`)
Se recomienda encarecidamente utilizar un bloque `with` para abrir archivos, ya que asegura que el sistema operativo libere los recursos automáticamente una vez terminada la ejecución de su bloque de código, incluso si ocurre una excepción.

Se pueden abrir archivos con el método `Path.open()` o con la función integrada `open()`.

```python
with ruta.open(mode="r", encoding="utf-8") as archivo:
    # Bloque de código procesando "archivo"
```

#### Modos de Apertura
Modo	Descripción
"r"	Crea un objeto de lectura y lanza un error si el archivo no existe.
"w"	Crea un objeto de escritura y sobrescribe todos los datos existentes en el archivo.
"a"	Crea un objeto para añadir datos al final del archivo.
"rb", "wb", "ab"	Equivalentes en modo binario (no realiza procesos de decodificación).

### Lectura de Datos

    .read(): Lee todo el texto en el archivo y lo devuelve como un único objeto str (cadena de texto). Si tiene múltiples líneas, estarán separadas por un carácter de salto de línea (\n).

    .readlines(): Devuelve un iterable de las líneas del archivo, lo cual es útil si quieres procesar o buscar registros línea por línea mediante un bucle for .

### Escritura de Datos

    .write(cadena): Pasa una cadena al archivo (abierto en modo "w" o "a") y devuelve el número de caracteres escritos . Al abrir en "w", cualquier dato previo en el archivo original se pierde .

    .writelines(lista_de_cadenas): Permite escribir múltiples líneas a la vez iterando sobre una lista . No inserta automáticamente caracteres de nueva línea, por lo que se deben incluir en cada cadena manualmente (\n) .
