# Ejercicios CSV
## Nivel Básico (Ejercicios 1-5)

### Ejercicio 1: Lectura de CSV y conteo simple
**Tema:** Trabajo con archivos CSV, lectura de datos, variables

Carga el archivo `servidores_logs.csv` y cuenta cuántas líneas contiene (sin contar la cabecera). Imprime el resultado.

**Pista:** Usa `csv.reader()` y un bucle `for`.

**Solución esperada:** Un número aproximado a 50.

---

### Ejercicio 2: Filtrado por columna
**Tema:** CSV, condicionales, listas

Lee `transacciones_tienda.csv` y filtra solo las transacciones con `estado == 'completada'`. Imprime cuántas hay.

**Pista:** Usa `csv.DictReader()` para acceder por nombre de columna.

**Solución esperada:** Un número entre 30-40.

---

### Ejercicio 3: Suma de valores numéricos
**Tema:** CSV, conversión de tipos, bucles

Lee `transacciones_tienda.csv` y suma el total de dinero en la columna `monto`. Imprime el resultado.

**Pista:** Recuerda convertir strings a números con `float()`.

**Solución esperada:** Un número aproximado a 5000-8000.

---

### Ejercicio 4: Búsqueda en datos
**Tema:** CSV, condicionales, búsqueda

Lee `usuarios_registro.csv` y encuentra todos los usuarios cuya edad sea mayor a 30. Imprime sus nombres.

**Pista:** `int()` para convertir la edad.

**Solución esperada:** Una lista de nombres.

---

### Ejercicio 5: Escritura de datos filtrados
**Tema:** CSV lectura y escritura, bucles

Lee `transacciones_tienda.csv`, filtra solo las transacciones del mes '03' (columna `mes`), y escribe el resultado en un nuevo archivo `transacciones_marzo.csv`.

**Pista:** Usa `csv.DictReader()` para leer y `csv.DictWriter()` para escribir.

**Solución esperada:** Un archivo CSV con ~8-12 transacciones de marzo.

---

## Nivel Medio (Ejercicios 6-8)

### Ejercicio 6: Agregación por categoría
**Tema:** CSV, diccionarios, bucles anidados

Lee `transacciones_tienda.csv` y calcula el total de dinero por categoría de producto (`categoria`). Imprime un resumen tipo:
```
electrónica: 2500.50
ropa: 1200.30
alimentos: 800.20
```

**Pista:** Usa un diccionario para acumular montos por categoría.

**Solución esperada:** 3-5 categorías con totales.

---

### Ejercicio 7: Análisis de logs con estadísticas
**Tema:** CSV, listas, tipos de dato

Lee `servidores_logs.csv` y:
- Cuenta cuántas líneas tienen `nivel == 'ERROR'`
- Cuenta cuántas tienen `nivel == 'WARNING'`
- Cuenta cuántas tienen `nivel == 'INFO'`
- Calcula el porcentaje de cada uno

Imprime un resumen.

**Pista:** Usa tres contadores o un diccionario.

**Solución esperada:** Porcentajes aproximados (ej: ERROR 15%, WARNING 35%, INFO 50%).

---

### Ejercicio 8: Usuarios activos por rango de edad
**Tema:** CSV, condicionales compuestos, diccionarios

Lee `usuarios_registro.csv` y agrupa usuarios por rango de edad:
- 18-25
- 26-40
- 41+

Escribe el resultado en un archivo `usuarios_por_rango.csv` con columnas: `rango_edad, cantidad_usuarios`.

**Pista:** Define los rangos con condiciones `if` anidados.

**Solución esperada:** Un CSV con 3 filas (los 3 rangos) y sus conteos.

---

## Nivel Avanzado (Ejercicios 9-10)

### Ejercicio 9: Detección de anomalías en logs
**Tema:** CSV, lógica compleja, filtrado múltiple

Lee `servidores_logs.csv` y detecta "anomalías" definidas como:
- Líneas con `nivel == 'ERROR'` Y `tiempo_respuesta > 5000` (ms)

Escribe las anomalías detectadas en un archivo `anomalias.csv` preservando todas las columnas originales.

**Pista:** Usa condiciones compuestas con `and`. Necesitarás convertir `tiempo_respuesta` a número.

**Solución esperada:** Un CSV con 3-8 anomalías detectadas.

---

### Ejercicio 10: Reporte combinado multi-fuente
**Tema:** CSV múltiples, agregación compleja, escritura estructurada

Lee TODOS los 3 archivos CSV y genera un reporte en archivo `reporte_general.txt` que contenga:

1. **Resumen de Logs:** Total de errores, warnings, info. Servidor más problemático (con más ERRORs).
2. **Resumen de Transacciones:** Total de transacciones, monto total, categoría más vendida.
3. **Resumen de Usuarios:** Total de usuarios, edad promedio, usuario más joven.

El archivo debe ser legible y bien formateado.

**Pista:**
- Lee los 3 archivos y acumula datos en variables/diccionarios
- Para "servidor más problemático", usa `max()` o un diccionario con conteos
- Para "edad promedio", suma edades y divide por cantidad
- Usa `.write()` con `\n` para estructura el texto

**Solución esperada:** Un archivo de texto con 3 secciones bien definidas y datos resumidos.

---

## Notas generales

- Todos los ejercicios usan los CSVs proporcionados
- Usa `encoding='utf-8'` al abrir archivos
- Maneja bien los tipos de dato (strings → números cuando sea necesario)
- Los básicos se enfocam en lectura; los medios en agregación; los avanzados en lógica combinada
