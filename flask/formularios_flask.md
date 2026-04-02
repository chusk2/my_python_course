# Formularios en Flask: Guía Completa (Sin JavaScript)

## Tabla de Contenidos
1. [Conceptos Básicos](#conceptos-básicos)
2. [Métodos GET y POST](#métodos-get-y-post)
3. [Estructura de Proyecto](#estructura-de-proyecto)
4. [CSS Separado y url_for](#css-separado-y-urlfor)
5. [Código de Ejemplo Completo](#código-de-ejemplo-completo)
6. [Flujo sin JavaScript](#flujo-sin-javascript)
7. [Explicación Línea por Línea](#explicación-línea-por-línea)

---

## Conceptos Básicos

Un formulario HTML es un conjunto de elementos que permite a los usuarios enviar información a un servidor. Los principales elementos son:

- **`<input>`**: Campo de texto, número, contraseña, etc.
- **`<select>`**: Lista desplegable de opciones
- **`<checkbox>`**: Casilla de verificación (múltiples opciones)
- **`<button type="submit">`**: Botón para enviar el formulario

---

## Métodos GET y POST

### GET
- **Uso**: Solicitar datos del servidor
- **Datos**: Se envían en la URL (visible en la barra de direcciones)
- **Límite**: Máximo ~2000 caracteres
- **Seguridad**: Baja (los datos son visibles)
- **Ejemplo URL**: `http://ejemplo.com/buscar?tema=quimica&tipo=examen`

```html
<form method="GET" action="/buscar">
    <input type="text" name="tema">
    <button type="submit">Buscar</button>
</form>
```

**Ventajas:**
- Fácil de depurar (ves los datos en la URL)
- Puedes guardar URLs con búsquedas
- No requiere confirmación al recargar

**Desventajas:**
- No es seguro para datos sensibles
- Los datos están limitados en tamaño

### POST
- **Uso**: Enviar datos para crear/modificar en el servidor
- **Datos**: Se envían en el cuerpo de la solicitud (ocultos)
- **Límite**: Mucho más alto (varios MB)
- **Seguridad**: Mayor (los datos no aparecen en la URL)
- **Ejemplo**: Al enviar un formulario de login

```html
<form method="POST" action="/login">
    <input type="text" name="usuario">
    <input type="password" name="contraseña">
    <button type="submit">Enviar</button>
</form>
```

**Ventajas:**
- Seguro para datos sensibles
- Sin límite de tamaño (prácticamente)
- Los datos no aparecen en la URL

**Desventajas:**
- No puedes compartir fácilmente la URL
- Más complejo de depurar
- Requiere confirmación al recargar en algunos navegadores

### Comparativa Rápida

| Característica | GET | POST |
|---|---|---|
| Visibilidad de datos | En la URL | En el cuerpo (oculto) |
| Tamaño máximo | ~2KB | MB |
| Caché | Sí | No |
| Historial del navegador | Sí | No |
| Uso recomendado | Búsquedas, filtros | Crear, editar, eliminar datos |

---

## Estructura de Proyecto

```
proyecto_flask/
│
├── app.py                    # Archivo principal de Flask
│
├── templates/                # Carpeta para HTML
│   ├── index.html           # Formulario principal
│   └── resultado.html       # Página de resultados
│
├── static/                   # Carpeta para archivos estáticos
│   └── css/
│       ├── style.css        # Estilos principales
│       └── resultado.css    # Estilos de página de resultados
│
└── requirements.txt          # Dependencias
```

### Carpetas importantes

**`templates/`** - Donde Flask busca los archivos HTML
- Flask automáticamente busca aquí cuando usas `render_template()`
- Nombre de carpeta debe ser exactamente `templates`

**`static/`** - Donde se guardan archivos que no cambian
- CSS, JavaScript, imágenes, fuentes
- Flask automáticamente sirve estos archivos en `/static/`
- Nombre de carpeta debe ser exactamente `static`

---

## CSS Separado y url_for

### ¿Por qué separar el CSS?

Mantener CSS separado del HTML tiene ventajas:

1. **Reutilizable**: El mismo CSS se puede usar en múltiples páginas
2. **Mantenible**: Cambiar estilos es más fácil
3. **Cacheable**: El navegador guarda el archivo CSS en caché
4. **Organizado**: Código HTML más limpio

### ¿Qué es `url_for()`?

`url_for()` es una **función de Jinja2** (motor de templates de Flask) que genera URLs **dinámicamente**. 

**Problema sin url_for:**
```html
<!-- ❌ INCORRECTO - URL hardcodeada -->
<link rel="stylesheet" href="/static/css/style.css">
```

Si mañana cambias la estructura, tendrías que actualizar todas las referencias manualmente.

**Solución con url_for:**
```html
<!-- ✅ CORRECTO - URL generada dinámicamente -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

### Sintaxis de `url_for()`

```html
<!-- Para archivos CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

<!-- Para archivos JavaScript -->
<script src="{{ url_for('static', filename='js/script.js') }}"></script>

<!-- Para imágenes -->
<img src="{{ url_for('static', filename='img/logo.png') }}">
```

**Desglose:**
- `url_for()`: Función de Flask
- `'static'`: Indica que es un archivo estático
- `filename='css/style.css'`: Ruta del archivo dentro de `static/`
- `{{ ... }}`: Sintaxis de Jinja2 para insertar variables

### ¿Qué genera url_for()?

```python
# En Flask
url_for('static', filename='css/style.css')

# Genera esta URL
/static/css/style.css
```

**Ventaja:** Si en el futuro cambias la configuración de Flask, la URL se ajusta automáticamente sin cambiar el HTML.

---

## Código de Ejemplo Completo

### 1. `app.py` - Lógica del servidor

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datos de ejemplo: categorías y sus opciones
datos_dinámicos = {
    'química': ['Ácido-Base', 'Redox', 'Termoquímica', 'Cinética'],
    'física': ['Mecánica', 'Termodinámica', 'Ondas', 'Óptica'],
    'biología': ['Genética', 'Ecología', 'Fisiología', 'Evolución']
}

@app.route('/')
def index():
    """
    Ruta GET: Muestra el formulario inicial
    - Renderiza el template index.html
    - Envía las categorías al template
    """
    return render_template('index.html', categorias=datos_dinámicos.keys())


@app.route('/procesar-formulario', methods=['GET', 'POST'])
def procesar_formulario():
    """
    Ruta GET y POST: Procesa el envío del formulario
    
    - Si es GET: muestra el formulario con posibles datos anteriores
    - Si es POST: valida y procesa los datos
    """
    
    # Validación de datos desde el formulario
    nombre = request.form.get('nombre', '')                # input tipo text
    categoria = request.form.get('categoria', '')          # select principal
    subcategoria = request.form.get('subcategoria', '')    # select dependiente
    intereses = request.form.getlist('interes')            # checkboxes (lista)
    
    errores = []
    
    # Solo validar si es POST (formulario enviado)
    if request.method == 'POST':
        
        # Validaciones
        if not nombre or len(nombre.strip()) == 0:
            errores.append('El nombre es obligatorio')
        
        if not categoria:
            errores.append('Debes seleccionar una categoría')
        
        if not subcategoria:
            errores.append('Debes seleccionar una subcategoría')
        
        if not intereses:
            errores.append('Debes seleccionar al menos un interés')
        
        # Si hay errores, mostrar el formulario nuevamente
        if errores:
            return render_template(
                'index.html',
                categorias=datos_dinámicos.keys(),
                errores=errores,
                datos_anteriores={
                    'nombre': nombre,
                    'categoria': categoria,
                    'subcategoria': subcategoria,
                    'intereses': intereses
                },
                subcategorias_actuales=datos_dinámicos.get(categoria, [])
            )
        
        # Si todo es válido, redirigir a página de resultados
        # con los datos en la sesión (o en argumentos GET)
        return redirect(url_for('resultado', 
                               nombre=nombre,
                               categoria=categoria,
                               subcategoria=subcategoria,
                               intereses=','.join(intereses)))
    
    # GET: mostrar formulario vacío
    return render_template('index.html', 
                          categorias=datos_dinámicos.keys(),
                          errores=[],
                          datos_anteriores={},
                          subcategorias_actuales=[])


@app.route('/resultado')
def resultado():
    """
    Ruta GET: Muestra la página de resultados
    
    - Recibe los datos como parámetros GET en la URL
    - Los datos vienen de la redirección en procesar_formulario
    """
    
    nombre = request.args.get('nombre', 'N/A')
    categoria = request.args.get('categoria', 'N/A')
    subcategoria = request.args.get('subcategoria', 'N/A')
    intereses_str = request.args.get('intereses', '')
    
    # Convertir string de intereses a lista
    intereses = intereses_str.split(',') if intereses_str else []
    
    return render_template('resultado.html',
                          nombre=nombre,
                          categoria=categoria,
                          subcategoria=subcategoria,
                          intereses=intereses)


if __name__ == '__main__':
    app.run(debug=True)
```

### 2. `templates/index.html` - Formulario

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario con Select Dinámico</title>
    
    <!-- Cargando CSS con url_for -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <h1>📋 Mi Formulario</h1>

        <!-- MOSTRAR ERRORES SI EXISTEN -->
        {% if errores %}
        <div class="error-box">
            <strong>⚠️ Por favor corrige los siguientes errores:</strong>
            <ul>
                {% for error in errores %}
                <li>{{ error }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}

        <!-- FORMULARIO -->
        <form method="POST" action="{{ url_for('procesar_formulario') }}">

            <!-- CAMPO DE ENTRADA TEXT -->
            <div class="form-group">
                <label for="nombre">Nombre:</label>
                <input 
                    type="text" 
                    id="nombre" 
                    name="nombre"
                    placeholder="Ej: Juan García"
                    value="{{ datos_anteriores.nombre if datos_anteriores else '' }}"
                    required
                >
            </div>

            <!-- SELECT PRINCIPAL -->
            <div class="form-group">
                <label for="categoria">Categoría:</label>
                <select 
                    id="categoria" 
                    name="categoria"
                    required
                    onchange="this.form.submit()"
                >
                    <option value="">-- Selecciona una categoría --</option>
                    {% for cat in categorias %}
                    <option 
                        value="{{ cat }}"
                        {% if datos_anteriores and datos_anteriores.categoria == cat %}selected{% endif %}
                    >
                        {{ cat | capitalize }}
                    </option>
                    {% endfor %}
                </select>
            </div>

            <!-- SELECT DINÁMICO (SE LLENA CON SERVIDOR) -->
            <div class="form-group">
                <label for="subcategoria">Subcategoría:</label>
                <select 
                    id="subcategoria" 
                    name="subcategoria"
                    required
                >
                    <option value="">-- Selecciona una subcategoría --</option>
                    {% for subcat in subcategorias_actuales %}
                    <option 
                        value="{{ subcat }}"
                        {% if datos_anteriores and datos_anteriores.subcategoria == subcat %}selected{% endif %}
                    >
                        {{ subcat }}
                    </option>
                    {% endfor %}
                </select>
            </div>

            <!-- CHECKBOXES (MÚLTIPLES OPCIONES) -->
            <div class="form-group">
                <label>Intereses (selecciona al menos uno):</label>
                <div class="checkbox-group">
                    <div class="checkbox-item">
                        <input 
                            type="checkbox" 
                            id="interes1" 
                            name="interes" 
                            value="Ejercicios"
                            {% if datos_anteriores and 'Ejercicios' in datos_anteriores.intereses %}checked{% endif %}
                        >
                        <label for="interes1">📝 Ejercicios</label>
                    </div>
                    <div class="checkbox-item">
                        <input 
                            type="checkbox" 
                            id="interes2" 
                            name="interes" 
                            value="Teoría"
                            {% if datos_anteriores and 'Teoría' in datos_anteriores.intereses %}checked{% endif %}
                        >
                        <label for="interes2">📚 Teoría</label>
                    </div>
                    <div class="checkbox-item">
                        <input 
                            type="checkbox" 
                            id="interes3" 
                            name="interes" 
                            value="Exámenes"
                            {% if datos_anteriores and 'Exámenes' in datos_anteriores.intereses %}checked{% endif %}
                        >
                        <label for="interes3">🧪 Exámenes</label>
                    </div>
                    <div class="checkbox-item">
                        <input 
                            type="checkbox" 
                            id="interes4" 
                            name="interes" 
                            value="Prácticas"
                            {% if datos_anteriores and 'Prácticas' in datos_anteriores.intereses %}checked{% endif %}
                        >
                        <label for="interes4">🔬 Prácticas</label>
                    </div>
                </div>
            </div>

            <!-- BOTÓN SUBMIT -->
            <button type="submit">✅ Enviar Formulario</button>
        </form>
    </div>
</body>
</html>
```

### 3. `templates/resultado.html` - Página de Resultados

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultados del Formulario</title>
    
    <!-- Cargando CSS con url_for -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/resultado.css') }}">
</head>
<body>
    <div class="container">
        <h1>✅ ¡Formulario Enviado!</h1>

        <!-- MOSTRAR DATOS ENVIADOS -->
        <div class="resultado-item">
            <div class="resultado-label">👤 Nombre</div>
            <div class="resultado-valor">{{ nombre }}</div>
        </div>

        <div class="resultado-item">
            <div class="resultado-label">📂 Categoría</div>
            <div class="resultado-valor">{{ categoria | capitalize }}</div>
        </div>

        <div class="resultado-item">
            <div class="resultado-label">📋 Subcategoría</div>
            <div class="resultado-valor">{{ subcategoria }}</div>
        </div>

        <div class="resultado-item">
            <div class="resultado-label">⭐ Intereses</div>
            <div class="resultado-valor">
                <ul class="intereses-list">
                    {% for interes in intereses %}
                    <li>{{ interes }}</li>
                    {% endfor %}
                </ul>
            </div>
        </div>

        <div class="button-group">
            <button class="btn-volver" onclick="history.back()">⬅️ Volver</button>
            <button class="btn-nuevo" onclick="window.location.href='{{ url_for('index') }}'">🔄 Nuevo Formulario</button>
        </div>
    </div>
</body>
</html>
```

### 4. `static/css/style.css` - Estilos del Formulario

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.container {
    background: white;
    border-radius: 10px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
    padding: 40px;
    width: 100%;
    max-width: 500px;
}

h1 {
    color: #333;
    margin-bottom: 30px;
    text-align: center;
    font-size: 28px;
}

.form-group {
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 8px;
    color: #555;
    font-weight: 600;
    font-size: 14px;
}

input[type="text"],
select {
    width: 100%;
    padding: 12px;
    border: 2px solid #ddd;
    border-radius: 5px;
    font-size: 14px;
    transition: border-color 0.3s;
    font-family: inherit;
}

input[type="text"]:focus,
select:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
}

.checkbox-group {
    background: #f8f9fa;
    padding: 15px;
    border-radius: 5px;
}

.checkbox-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}

.checkbox-item:last-child {
    margin-bottom: 0;
}

input[type="checkbox"] {
    width: 18px;
    height: 18px;
    margin-right: 10px;
    cursor: pointer;
    accent-color: #667eea;
}

.checkbox-item label {
    margin: 0;
    font-weight: 400;
    cursor: pointer;
    font-size: 14px;
}

button {
    width: 100%;
    padding: 12px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    margin-top: 20px;
}

button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}

button:active {
    transform: translateY(0);
}

.error-box {
    background: #fee;
    border-left: 4px solid #f44;
    color: #c33;
    padding: 12px;
    border-radius: 4px;
    margin-bottom: 20px;
}

.error-box ul {
    margin-left: 20px;
    margin-top: 8px;
}

.error-box li {
    margin-bottom: 4px;
}
```

### 5. `static/css/resultado.css` - Estilos de Resultados

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.container {
    background: white;
    border-radius: 10px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
    padding: 40px;
    width: 100%;
    max-width: 500px;
}

h1 {
    color: #333;
    margin-bottom: 30px;
    text-align: center;
    font-size: 28px;
}

.resultado-item {
    background: #f8f9fa;
    padding: 15px;
    border-radius: 5px;
    margin-bottom: 15px;
    border-left: 4px solid #667eea;
}

.resultado-label {
    font-weight: 600;
    color: #555;
    font-size: 14px;
    margin-bottom: 5px;
}

.resultado-valor {
    color: #333;
    font-size: 16px;
}

.intereses-list {
    list-style: none;
    padding-left: 0;
}

.intereses-list li {
    display: inline-block;
    background: #667eea;
    color: white;
    padding: 5px 12px;
    border-radius: 20px;
    margin-right: 8px;
    margin-bottom: 8px;
    font-size: 13px;
}

.button-group {
    display: flex;
    gap: 10px;
    margin-top: 30px;
}

button {
    flex: 1;
    padding: 12px;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}

.btn-volver {
    background: #ddd;
    color: #333;
}

.btn-volver:hover {
    background: #ccc;
    transform: translateY(-2px);
}

.btn-nuevo {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.btn-nuevo:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
}
```

---

## Flujo sin JavaScript

### Funcionamiento del formulario sin JavaScript

```
1. Usuario abre http://localhost:5000/
   ↓
2. Flask ejecuta index()
   ├─ Renderiza index.html
   ├─ Envía las categorías principales
   ↓ Navegador muestra formulario vacío

3. Usuario selecciona "Química" en el select
   ↓
4. onchange="this.form.submit()" envía el formulario automáticamente
   ├─ POST a /procesar-formulario
   ├─ El servidor recibe 'química' en request.form.get('categoria')
   ↓
5. Flask ejecuta procesar_formulario() con POST
   ├─ Lee: nombre='', categoria='química', subcategoria='', intereses=[]
   ├─ Valida (hay errores: nombre y subcategoría faltantes)
   ├─ Renderiza index.html nuevamente con:
   │  ├─ errores=['El nombre es obligatorio', ...]
   │  ├─ datos_anteriores={'categoria': 'química'}
   │  ├─ subcategorias_actuales=['Ácido-Base', 'Redox', ...]
   ↓ Navegador muestra el formulario con:
     ├─ El select de categoría sigue mostrando "Química"
     ├─ El select de subcategoría AHORA tiene las opciones
     ├─ Errores visibles

6. Usuario completa los datos y hace click en "Enviar"
   ↓
7. POST a /procesar-formulario con todos los datos
   ├─ nombre='Juan'
   ├─ categoria='química'
   ├─ subcategoria='Ácido-Base'
   ├─ intereses=['Ejercicios', 'Exámenes']
   ↓
8. Flask valida (sin errores)
   ├─ Ejecuta redirect(url_for('resultado', ...))
   ├─ Convierte datos a parámetros GET
   ├─ Redirige a /resultado?nombre=Juan&categoria=quimica&...
   ↓
9. Flask ejecuta resultado()
   ├─ Lee datos desde request.args (parámetros GET)
   ├─ Renderiza resultado.html
   ↓
10. Navegador muestra página de resultados
    ├─ Datos del usuario formateados
    ├─ Botón "Volver" (history.back())
    ├─ Botón "Nuevo Formulario" (vuelve a /)
```

### ¿Cómo funciona `onchange="this.form.submit()"`?

```html
<select id="categoria" name="categoria" onchange="this.form.submit()">
```

- **`onchange`**: Evento HTML que se ejecuta cuando cambia el valor del select
- **`this.form`**: Refiere al formulario que contiene el select
- **`.submit()`**: Envía el formulario automáticamente

**Resultado:** El formulario se envía automáticamente sin necesidad de JavaScript externo.

---

## Explicación Línea por Línea

### Parte 1: Importaciones

```python
from flask import Flask, render_template, request, redirect, url_for
```

- **`Flask`**: Clase principal para crear la aplicación
- **`render_template`**: Renderiza archivos HTML
- **`request`**: Accede a datos de la solicitud HTTP
- **`redirect`**: Redirige a otra ruta
- **`url_for`**: Genera URLs dinámicamente

### Parte 2: Diccionario de Datos

```python
datos_dinámicos = {
    'química': ['Ácido-Base', 'Redox', 'Termoquímica', 'Cinética'],
    'física': ['Mecánica', 'Termodinámica', 'Ondas', 'Óptica'],
    'biología': ['Genética', 'Ecología', 'Fisiología', 'Evolución']
}
```

Almacena categorías como **claves** y subcategorías como **valores**.

### Parte 3: Ruta GET (Mostrar Formulario Vacío)

```python
@app.route('/')
def index():
    return render_template('index.html', categorias=datos_dinámicos.keys())
```

- **`@app.route('/')`**: Maneja solicitudes a `http://localhost:5000/`
- **`render_template`**: Carga `index.html`
- **`categorias=...`**: Envía las categorías al template

### Parte 4: Ruta POST (Procesar Formulario)

```python
@app.route('/procesar-formulario', methods=['GET', 'POST'])
def procesar_formulario():
```

- **`methods=['GET', 'POST']`**: Acepta ambos tipos de solicitud
- **GET**: Mostrar formulario inicial
- **POST**: Procesar datos enviados

```python
nombre = request.form.get('nombre', '')
categoria = request.form.get('categoria', '')
intereses = request.form.getlist('interes')
```

- **`request.form.get()`**: Obtiene UN valor del formulario
- **`request.form.getlist()`**: Obtiene MÚLTIPLES valores (checkboxes)
- **`''` (segundo parámetro)**: Valor por defecto si no existe

### Parte 5: Validaciones

```python
if request.method == 'POST':
    if not nombre or len(nombre.strip()) == 0:
        errores.append('El nombre es obligatorio')
```

- **`request.method == 'POST'`**: Verifica que es una solicitud POST
- **`not nombre`**: Verifica que el campo no está vacío
- **`.strip()`**: Elimina espacios en blanco

### Parte 6: Renderizar con Errores

```python
return render_template(
    'index.html',
    categorias=datos_dinámicos.keys(),
    errores=errores,
    datos_anteriores={
        'nombre': nombre,
        'categoria': categoria,
        'subcategoria': subcategoria,
        'intereses': intereses
    },
    subcategorias_actuales=datos_dinámicos.get(categoria, [])
)
```

Envía al template:
- **`categorias`**: Para el primer select
- **`errores`**: Lista de errores a mostrar
- **`datos_anteriores`**: Rellenar campos con datos previos
- **`subcategorias_actuales`**: Las subcategorías de la categoría seleccionada

### Parte 7: Redirección

```python
return redirect(url_for('resultado', 
                       nombre=nombre,
                       categoria=categoria,
                       subcategoria=subcategoria,
                       intereses=','.join(intereses)))
```

- **`redirect()`**: Redirige a otra ruta
- **`url_for('resultado', ...)`**: Genera la URL a la función `resultado()`
- **Parámetros adicionales**: Se convierten en parámetros GET
- **`','.join(intereses)`**: Convierte lista `['A', 'B']` a string `'A,B'`

**URL generada:**
```
/resultado?nombre=Juan&categoria=quimica&subcategoria=Ácido-Base&intereses=Ejercicios,Exámenes
```

### Parte 8: Ruta de Resultados

```python
@app.route('/resultado')
def resultado():
    nombre = request.args.get('nombre', 'N/A')
    intereses_str = request.args.get('intereses', '')
    intereses = intereses_str.split(',') if intereses_str else []
```

- **`request.args.get()`**: Lee parámetros GET de la URL
- **`.split(',')`**: Convierte string `'A,B'` a lista `['A', 'B']`

### Parte 9: Cargando CSS con url_for

En el template HTML:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

**Explicación:**
- **`{{ ... }}`**: Sintaxis de Jinja2 para insertar variables
- **`url_for()`**: Función que genera URLs
- **`'static'`**: Indica que es un archivo estático
- **`filename='css/style.css'`**: Ruta dentro de la carpeta `static/`

**¿Qué genera?**
```
{{ url_for('static', filename='css/style.css') }}
↓
/static/css/style.css
```

**¿Por qué usar url_for en lugar de hardcodear?**

Sin url_for:
```html
<!-- Si cambias la estructura, esto se rompe -->
<link rel="stylesheet" href="/static/css/style.css">
```

Con url_for:
```html
<!-- Siempre genera la URL correcta automáticamente -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
```

### Parte 10: Mostrando datos en el template

```html
<input 
    type="text" 
    id="nombre" 
    name="nombre"
    value="{{ datos_anteriores.nombre if datos_anteriores else '' }}"
>
```

**Explicación:**
- **`{{ datos_anteriores.nombre }}`**: Accede a la variable enviada desde Flask
- **`if datos_anteriores else ''`**: Si no hay datos anteriores, muestra string vacío
- **`value=`**: Rellena el input con este valor

---

## Resumen de Conceptos Clave

### Métodos de lectura de datos

| Método | Usado para | Retorna |
|---|---|---|
| `request.form.get('x')` | POST - un valor | String o None |
| `request.form.getlist('x')` | POST - múltiples valores | Lista |
| `request.args.get('x')` | GET - un valor | String o None |
| `request.args.getlist('x')` | GET - múltiples valores | Lista |

### Funciones importantes

| Función | Uso |
|---|---|
| `render_template()` | Renderiza un archivo HTML |
| `redirect()` | Redirige a otra ruta |
| `url_for()` | Genera URLs dinámicamente |
| `request.method` | Obtiene el método HTTP (GET/POST) |

### Flujo sin JavaScript

```
1. Usuario selecciona categoría
   ↓ onchange envía formulario
2. POST a servidor
   ↓
3. Servidor actualiza subcategorías
   ↓ Renderiza template con datos actualizados
4. Formulario muestra nuevas opciones
   ↓
5. Usuario completa y envía
   ↓ POST a servidor
6. Servidor valida
   ↓ redirect a página de resultados
7. GET a página de resultados
   ↓
8. Muestra resultados
```

---

## Instalación y Ejecución

### 1. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalar Flask

```bash
pip install flask
```

### 3. Estructura final

```
proyecto/
├── venv/
├── app.py
├── templates/
│   ├── index.html
│   └── resultado.html
├── static/
│   └── css/
│       ├── style.css
│       └── resultado.css
└── requirements.txt
```

### 4. Crear requirements.txt

```bash
pip freeze > requirements.txt
```

Contenido:
```
Flask==3.0.0
Werkzeug==3.0.0
```

### 5. Ejecutar

```bash
python app.py
```

Luego abre `http://localhost:5000` en tu navegador.

---

## Notas Importantes

1. **Carpeta static**: Debe llamarse exactamente `static` para que Flask la sirva automáticamente
2. **url_for()**: Siempre úsalo para generar URLs a rutas y archivos estáticos
3. **GET vs POST**: GET para lectura, POST para crear/modificar datos
4. **Validación en servidor**: Nunca confíes solo en validación HTML, valida siempre en Python
5. **Redirect**: Cambiar la URL después de procesar datos es una buena práctica (evita reenvíos duplicados)
6. **request.form vs request.args**: 
   - `.form` para datos POST
   - `.args` para datos GET (en URL)
7. **Conversión de datos**: Recuerda convertir listas de strings a strings y viceversa cuando las usas como parámetros GET
