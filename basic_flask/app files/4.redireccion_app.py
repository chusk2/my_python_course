from flask import Flask, url_for, redirect
import json

app = Flask(__name__)

html_head = '''
      <!DOCTYPE html>
            <html lang="es">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Información de Reservas</title>
            <style>
                  * {
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                        font-family: sans-serif;
                  }

                  body {
                        background-color: #e8f0fe;
                        padding: 2rem;
                  }

                  table {
                        border-collapse: collapse;
                        margin-top: 1.5rem;
                        width: 100%;
                        max-width: 500px;
                        border: 2px solid #2c5f8a;
                  }

                  th, td {
                        border: 1px solid #2c5f8a;
                        padding: 0.6rem 1.2rem;
                        text-align: left;
                  }

                  th {
                        background-color: #1a3d5c;
                        color: #f0f8ff;
                        letter-spacing: 0.05em;
                        text-transform: uppercase;
                        font-size: 0.85rem;
                  }

                  tr:nth-child(odd) {
                        background-color: #ffffff;
                  }

                  tr:nth-child(even) {
                        background-color: #c8dff5;
                  }

                  tr:hover {
                        background-color: #f0c040;
                        color: #1a3d5c;
                  }
            </style>
            </head>
'''

# cargamos el archivo json son la info de
# las reservas de los restaurantes
with open("../data/reservas.json", 'r', encoding='utf-8') as file:
      reservations = json.load(file)

@app.route("/")
def index():
    html_code = html_head + '''
    <body>
          <h1>Bienvenido a la gestión de reservas</h1>
          <p>Esta web permite consultar las reservas semanales de los restaurantes
          de nuestra cadena en Andalucía.</p>

          <h2>Nuestros restaurantes</h2>
          <ul>
    '''

    for prov, data in reservations.items():
          html_code += f'<li>{data["nombre"]} ({prov.title()})</li>\n'

    html_code += '''
          </ul>

          <p>Para consultar las reservas de un restaurante, accede a la ruta
          <strong>/reservas/provincia</strong>. Por ejemplo: <em>/reservas/granada</em></p>
          
          </body>
          </html>
    '''

    return html_code

# ruta para página no encontrada
@app.errorhandler(404)
def page_not_found(error):
    return (
        '<h1>Error 404 - La página que buscas no existe.</h1>'
        '<p>Pulsa en este enlace para acceder a la página de inicio: '
        f'<a href="{url_for("index")}">Página de inicio</a></p>'
    ), 404



# hacemos uso de redirect
@app.route("/provincia-no-encontrada/<province>")
def province_not_found(province):
      html_code = html_head + f'''
      <body>
            <h2>No existe ningún restaurante en <em>{province.title()}</em></h2>
            <p>Nuestros restaurantes están disponibles en las siguientes provincias:</p>
            <ul>
      '''

      for province, weekday in reservations.items():
            html_code += f'<li><a href="{url_for("show_reservations", province=province)}">{province["nombre"]} ({province.title()})</a></li>\n'

      html_code += '''
            </ul>
      </body>
      </html>
      '''

      return html_code


@app.route("/reservas/<province>")
def show_reservations(province):
      if province not in reservations.keys():
            return redirect(url_for("province_not_found", province=province))
            
      restaurant = reservations[province]["nombre"]

      html_code = html_head + f'''
      <body>
            <h2>Reservas del restaurante <em>{restaurant}</em></h2>
            <table>
                  <thead>
                        <tr>
                              <th>Día semana</th>
                              <th>Reservas</th>
                        </tr>
                  </thead>
                  <tbody>
      '''

      for weekday, guests_count in reservations[province].items():
            if weekday == "nombre":
                  continue
            html_code += f'<tr><td>{weekday.title()}</td><td>{guests_count}</td></tr>\n'

      html_code += '''
                  </tbody>
            </table>
      </body>
      </html>
      '''
      
      return html_code

# permite que arranquemos la app usando:
# python minimal_app.py
if __name__ == '__main__':
    app.run(debug=True)

