from flask import Flask, url_for, redirect, render_template
import json

app = Flask(__name__)

# cargamos el archivo json son la info de
# las reservas de los restaurantes
with open("reservas.json", 'r', encoding='utf-8') as file:
      reservations = json.load(file)

@app.route("/")
def index():
    return render_template("index.html", reservations= reservations)

# ruta para página no encontrada
@app.errorhandler(404)
def page_not_found(error):
    return render_template("not_found.html")

@app.route("/provincia-no-encontrada/<province>")
def province_not_found(province, reservations):
      data = [(province, data["nombre"]) for province, data in reservations.items()]

      return render_template('province_not_found.html',
                             province = province, data = data)


@app.route("/reservas/<province>")
def show_reservations(province):
      if province not in reservations.keys():
            return render_template("province_not_found.html",
                                           province=province,
                                           reservations = reservations)
            
      return render_template("reservations.html",
                                     province = province,
                                     reservations = reservations[province]
                                     )

# permite que arranquemos la app usando:
# python minimal_app.py
if __name__ == '__main__':
    app.run(debug=True)

