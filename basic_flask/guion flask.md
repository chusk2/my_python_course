# Guión Flask

1. Página básica Flask
```python

from flask import Flask

app = Flask(\_\_name\_\_)

@app.route("/")
def index():
    return "\<h1>Bienvenidos a Flask!\</h1>"

# permite que arranquemos la app usando:
# python minimal\_app.py

if __name__ == '__main__':

app.run(debug=True)
```
2. Crear ruta básica
```python
@app.route("/info")
def info():
    return "\<h1>Primeros pasos con Flask en el curso de Python con CodeSpace\</h1>"
```
2. Rutas con parámetros
   - ruta con parámetro
   - ruta con parámetro opcional: necesario usar *parámetro = None* en la función y además crear una ruta adicional sin parámetro.
    
3. Redirección
    -  Crear una ruta para casos en los que no existe la ruta
    -  Crear un decorador que capture el error 404 y redirija

   
   

   