# Instrucciones para generación de ejercicios de Python

## Formato y estructura

Cuando el usuario solicite ejercicios, genera un archivo markdown siguiendo esta plantilla:

### Encabezado
- Título con emoji: `# 🏋️ Ejercicios: [Tema]`
- Subtítulo con conceptos clave separados por ·
- Leyenda de niveles: `**Niveles:** 🟢 Básico (1–5) · 🟡 Medio (6–8) · 🔴 Avanzado (9–10)`

### Distribución de ejercicios
- **5 ejercicios básicos (🟢)**: Conceptos fundamentales, uno por uno
- **3 ejercicios medios (🟡)**: Combinación de 2-3 conceptos
- **2 ejercicios avanzados (🔴)**: Integración de conceptos de la unidad actual + unidades previas

### Estructura de cada ejercicio

```markdown
### Ejercicio [N] — [Título descriptivo]

[Enunciado claro del problema, con contexto del mundo real]

**Ejemplo de salida esperada:**
```
[Muestra exacta de cómo debería verse el resultado]
```

<details>
<summary>💡 Pista</summary>

[Una pista útil sin revelar la solución completa]

</details>

<details>
<summary>✅ Solución</summary>

```python
# Código comentado línea por línea
# Explicando el razonamiento, no solo QUÉ hace sino POR QUÉ
```

</details>
```

### Tabla resumen final

Incluir siempre al final una tabla con:
- Columna 1: Número de ejercicio
- Columna 2: Nivel (emoji 🟢🟡🔴)
- Columna 3: Concepto principal trabajado

### Temática de ejercicios

**Distribución recomendada (en los 10 ejercicios):**
- 6-7 ejercicios: Situaciones cotidianas (finanzas personales, compras, conversiones, gestión de tiempo, recetas)
- 2-3 ejercicios: Aplicaciones técnicas reales (análisis de datos, automatización, cálculos científicos, procesamiento de información)
- 1 ejercicio: Problema laboral concreto (inventarios, nóminas, reportes, validaciones)

### Principios pedagógicos

1. **Progresión clara**: Cada ejercicio construye sobre el anterior
2. **Contextualización real**: Siempre vincular con tareas del mundo real
3. **Comentarios educativos**: No solo explicar QUÉ hace el código, sino POR QUÉ y CUÁNDO usarlo
4. **Soluciones simples**: Priorizar claridad sobre eficiencia o elegancia
5. **Ejemplos de salida**: Siempre mostrar el resultado esperado para que el alumno pueda validar

### Archivos complementarios

Si los ejercicios requieren datos:
- Generar CSV con 50-100 filas
- Datos realistas y coherentes con el contexto del ejercicio
- Nombres de columnas descriptivos en español

## Ejemplo de aplicación

Si el usuario pide "ejercicios sobre bucles for", generar:
- 🟢 Básicos: Iterar listas simples, range(), enumerate()
- 🟡 Medios: Bucles anidados, acumuladores, filtrado con if
- 🔴 Avanzados: Procesamiento de CSV, generación de reportes, validación de datos

---

## Cómo incorporar estas instrucciones

### Opción 1: Custom Instructions (para uso personal)

1. Haz clic en tu **perfil/avatar** (esquina superior derecha)
2. Selecciona **"Settings"** o **"Configuración"**
3. Busca **"Custom Instructions"** o **"Instrucciones personalizadas"**
4. En la segunda caja (la de "How would you like Claude to respond?"), pega este documento
5. Guarda los cambios

Esto aplicará a todas tus conversaciones con Claude.

### Opción 2: Project Knowledge (recomendada para este proyecto)

Si estás usando **Claude Projects**:

1. Ve a la vista del proyecto actual
2. Busca la sección **"Project Knowledge"** o **"Knowledge"**
3. Haz clic en **"Add content"** o el botón equivalente
4. Crea un nuevo documento llamado `"instrucciones_ejercicios.md"`
5. Pega el contenido de este archivo
6. Guarda

Esto hará que las instrucciones solo apliquen cuando trabajas en este proyecto específico.

### Opción 3: Incluir en cada conversación (manual)

Simplemente copia y pega las instrucciones al inicio de cada nueva conversación donde vayas a pedir ejercicios.

---

**Recomendación:** Usa la **Opción 2 (Project Knowledge)** si este es un proyecto dedicado a crear material educativo de Python.
