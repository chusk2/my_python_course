from flask import Flask, render_template
import json

app = Flask(__name__)

# cargamos el archivo json son la info de
# las reservas de los restaurantes
with open("../data/elementos.json", 'r', encoding='utf-8') as file:
      elements = json.load(file)["elementos"]

# quiero reordenar las columnas
# orden original: nombre, simbolo, numero, categoria, masa
# orden final: nombre, simbolo, categoria, numero, masa
# (truco de cómo generar lista a partir de string)
new_order = ['nombre', 'simbolo', 'categoria', 'numero', 'masa']
elements = [
     {key:element[key] for key in new_order}
     for element in elements ]

@app.route("/")
@app.route("/index")
def index():
    headers = list(elements[0].keys())
    return render_template("chemical_elements.html",
                           headers = headers,
                           elements= elements)


# permite que arranquemos la app usando:
# python minimal_app.py
if __name__ == '__main__':
    app.run(debug=True)