from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>Rutas parametrizadas con Flask!</h1>"

html_head = '''
      <!DOCTYPE html>
            <html lang="es">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Información Lenguaje de Programación</title>
            <style>
                  * {{
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                        font-family: sans-serif;
                  }}

                  body {{
                        background-color: #e8f0fe;
                        padding: 2rem;
                  }}
            </style>
            </head>
'''

# cargamos el archivo json son la info de
# los lenguajes de programación
with open("../data/lenguajes.json", 'r', encoding='utf-8') as file:
      languages = json.load(file)

# cargamos el archivo json son la info de
# las reservas de los restaurantes
with open("../data/reservas.json", 'r', encoding='utf-8') as file:
      reservations = json.load(file)


@app.route("/reservas/<province>/<weekday>")
def show_reservations(province, weekday):
      restaurant = reservations[province]["nombre"]
      guests_count = reservations[province][weekday]

      html_code = html_head + f'''
      <body>
                  <h2>Información sobre reservas del restaurante <em>{restaurant}</em></h2>
                  <p>
                  Nuestro restaurante situado en {province.title()} tiene confirmadas
                  {guests_count} reservas para el {weekday.title()} de la próxima semana.
                  </p>
            </body>
      ''' + "</html>"
      
      return html_code

@app.route("/lang_info/")
@app.route("/lang_info/<language>")
def info(language = None):
      if language:
            language = languages[language]
      else:
            language = languages["python"]
      
      html_code = html_head + f'''
      <body>
                  <h2>Información sobre {language["nombre"]}</h2>
                  <p>
                  El lenguage de programación {language["nombre"]} fue creado en {language["año"]} por {language["creador"]}.
                  <br/>
                  Para crear un <strong>Hola, Mundo!</strong>, el código necesario es:
                  
                  </br></br>
                  
                  <code>{language["hola_mundo"]}</code>
                  </p>
            </body>
      ''' + "</html>"
      
      return html_code

# permite que arranquemos la app usando:
# python minimal_app.py
if __name__ == '__main__':
    app.run(debug=True)

