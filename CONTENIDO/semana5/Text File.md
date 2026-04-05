# Guía de Gestión de Archivos en Python

Esta guía resume los conceptos fundamentales para la lectura, escritura y manipulación de archivos y directorios en Python, basados en el módulo estándar `pathlib`.

---

## 1. Archivos y el Sistema de Archivos

* [cite_start]**¿Qué es un archivo?** Un archivo es, en última instancia, una secuencia de bytes[cite: 28]. [cite_start]Cada byte en un archivo puede concebirse como un entero con un valor entre 0 y 255[cite: 29]. [cite_start]No hay nada intrínseco en el archivo que dicte cómo deben interpretarse sus contenidos; esto depende de cómo se decodifiquen[cite: 32].
* [cite_start]**El Sistema de Archivos:** Proporciona una representación abstracta de los archivos almacenados y se encarga de interactuar con los dispositivos para controlar el almacenamiento y recuperación de datos [cite: 44-46]. [cite_start]Diferentes sistemas operativos utilizan distintos sistemas de archivos[cite: 49].
* [cite_start]**Jerarquía:** Los sistemas de archivos organizan los archivos en una jerarquía de directorios (carpetas) que parten de un directorio principal llamado directorio raíz [cite: 54-55].
* [cite_start]**Rutas de Archivos:** La manera de ubicar un archivo enumerando los directorios desde la raíz hasta el nombre del archivo se denomina "ruta de archivo" [cite: 74-78]. [cite_start]En macOS y Linux, la raíz se representa con una barra inclinada (`/`)[cite: 87]. [cite_start]En Windows, cada dispositivo tiene un directorio raíz único representado por una letra de unidad y una barra invertida (`\`)[cite: 89].

---

## 2. Trabajando con Rutas (`pathlib`)

[cite_start]Para gestionar de forma segura y multiplataforma las rutas, Python ofrece el módulo estándar `pathlib`[cite: 95, 99].

### Creación de Objetos `Path`
* [cite_start]**A partir de una cadena:** `pathlib.Path("/ruta/al/archivo.txt")`[cite: 106, 114]. [cite_start]En Windows, para evitar errores por secuencias de escape, se pueden usar barras inclinadas (`/`) o prefijar la cadena con `r` (cadena cruda) [cite: 120-125].
* **Métodos de clase especiales:**
    * [cite_start]`Path.home()`: Devuelve un objeto que representa el directorio de usuario actual [cite: 127-128, 137].
    * [cite_start]`Path.cwd()`: Devuelve el directorio de trabajo actual (Current Working Directory) [cite: 127-128, 154].
* [cite_start]**Operador `/`:** Permite extender una ruta existente combinando objetos `Path` con cadenas u otros objetos `Path`[cite: 163, 168].

### Rutas Absolutas vs. Relativas
* [cite_start]Una ruta que comienza en el directorio raíz se denomina absoluta[cite: 172].
* [cite_start]Una ruta que no es absoluta se llama ruta relativa[cite: 173]. [cite_start]Estas cobran sentido al considerarse dentro del contexto de otro directorio[cite: 182].
* [cite_start]Puedes comprobar si una ruta es absoluta con el método `.is_absolute()`[cite: 180].

### Componentes de una Ruta
Una vez creado el objeto `Path`, puedes inspeccionar sus partes:
* [cite_start]`.parents`: Devuelve un iterable con la lista de directorios en la ruta, en orden inverso[cite: 196, 202].
* [cite_start]`.parent`: Devuelve el nombre del primer directorio padre en la ruta[cite: 210].
* [cite_start]`.anchor`: Devuelve el directorio raíz de la ruta (si es absoluta)[cite: 213].
* [cite_start]`.name`: Nombre del archivo o directorio al que apunta la ruta[cite: 222].
* [cite_start]`.stem`: El nombre del archivo sin la extensión (a la izquierda del punto)[cite: 230].
* [cite_start]`.suffix`: La extensión del archivo (a la derecha del punto)[cite: 230].

### Verificación de Existencia
* [cite_start]`.exists()`: Devuelve `True` o `False` dependiendo de si la ruta existe en la máquina[cite: 245].
* [cite_start]`.is_file()`: Comprueba si la ruta hace referencia a un archivo [cite: 252-253].
* [cite_start]`.is_dir()`: Comprueba si la ruta hace referencia a un directorio[cite: 257].

---

## 3. Operaciones Comunes del Sistema de Archivos

### Creación de Directorios y Archivos
* [cite_start]**Crear Directorio:** Usa `Path.mkdir()`[cite: 288]. [cite_start]Para crear múltiples niveles de directorios simultáneamente, usa el argumento `parents=True`[cite: 333]. [cite_start]Para evitar excepciones si el directorio ya existe, usa `exist_ok=True`[cite: 312].
    * [cite_start]*Patrón común:* `ruta.mkdir(parents=True, exist_ok=True)` [cite: 336-338].
* [cite_start]**Crear Archivo:** Usa `Path.touch()` para crear un archivo vacío[cite: 347, 361]. [cite_start]A diferencia de `.mkdir()`, `.touch()` no tiene un parámetro para crear carpetas padre; estas deben existir previamente [cite: 375-376]. [cite_start]No lanza un error si el archivo ya existe[cite: 357].

### Iteración y Búsqueda
* [cite_start]**Iterar contenidos directos:** `Path.iterdir()` devuelve un iterador de objetos `Path` con cada elemento del directorio (archivos y subcarpetas inmediatos)[cite: 384, 390].
* [cite_start]**Búsqueda con patrones (`glob`):** `Path.glob(patrón)` devuelve elementos que cumplan ciertos criterios utilizando caracteres comodín[cite: 421, 425].
    * [cite_start]`*`: Coincide con cualquier número de caracteres[cite: 444].
    * [cite_start]`?`: Coincide con un solo carácter[cite: 444, 490].
    * [cite_start]`[abc]`: Coincide con uno de los caracteres específicos entre los corchetes [cite: 444, 508-510].
* [cite_start]**Búsqueda recursiva:** Usando el prefijo `**/` con `.glob()` o utilizando el método simplificado `.rglob()`, puedes buscar recursivamente en el directorio actual y todos sus subdirectorios [cite: 520-522, 534].

### Mover, Renombrar y Eliminar
* **Mover/Renombrar:** `ruta_origen.replace(ruta_destino)`. Si el destino ya existe, será sobrescrito sin lanzar ninguna excepción, por lo que debe hacerse con precaución[cite: 543, 551, 554].
* [cite_start]**Eliminar archivo:** `Path.unlink()`[cite: 566]. [cite_start]Si la ruta no existe, lanza un `FileNotFoundError` a menos que se use `missing_ok=True`[cite: 579, 588].
* **Eliminar directorio:** `Path.rmdir()`. [cite_start]Sólo funciona si el directorio está vacío [cite: 595-596].
* **Eliminar árbol de directorios (no vacío):** Es necesario utilizar la función `rmtree()` del módulo estándar `shutil` (`shutil.rmtree()`) [cite: 616-617].

---

## 4. Lectura y Escritura de Archivos

Para poder interpretar la secuencia de bytes de un archivo de texto, Python necesita aplicar una codificación (encoding) durante el proceso de apertura [cite: 676, 693-694]. UTF-8 es una de las codificaciones de caracteres más utilizadas porque puede representar un rango mucho mayor de caracteres que ASCII [cite: 698, 703-704].

### Apertura de Archivos (La declaración `with`)
Se recomienda encarecidamente utilizar un bloque `with` para abrir archivos, ya que asegura que el sistema operativo libere los recursos automáticamente una vez terminada la ejecución de su bloque de código, incluso si ocurre una excepción [cite: 819, 828-832].

Se pueden abrir archivos con el método `Path.open()` o con la función integrada `open()` [cite: 755-757, 793].

```python
with ruta.open(mode="r", encoding="utf-8") as archivo:
    # Bloque de código procesando "archivo"

Modos de Apertura
Modo	Descripción
"r"	Crea un objeto de lectura y lanza un error si el archivo no existe.
"w"	Crea un objeto de escritura y sobrescribe todos los datos existentes en el archivo.
"a"	Crea un objeto para añadir datos al final del archivo.
"rb", "wb", "ab"	Equivalentes en modo binario (no realiza procesos de decodificación).
Lectura de Datos

    .read(): Lee todo el texto en el archivo y lo devuelve como un único objeto str (cadena de texto). Si tiene múltiples líneas, estarán separadas por un carácter de salto de línea (\n).

    .readlines(): Devuelve un iterable de las líneas del archivo, lo cual es útil si quieres procesar o buscar registros línea por línea mediante un bucle for .

Escritura de Datos

    .write(cadena): Pasa una cadena al archivo (abierto en modo "w" o "a") y devuelve el número de caracteres escritos . Al abrir en "w", cualquier dato previo en el archivo original se pierde .

    .writelines(lista_de_cadenas): Permite escribir múltiples líneas a la vez iterando sobre una lista . No inserta automáticamente caracteres de nueva línea, por lo que se deben incluir en cada cadena manualmente (\n) .
