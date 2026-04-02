from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/form", methods = ("GET", "POST"))
def form():
    if request.method == "POST":
        data = {
        "name" : request.form.get("employee_name"),
        "age" : request.form.get("age"),
        "company" : request.form.get("company"),
        "position" :request.form.get("position"),
        }
        # traducir a español
        keys_spanish = ["nombre", "edad", "empresa", "puesto"]
        data = {key_es:value for key_es, value in zip( keys_spanish, data.values() ) }

        # format empresa y puesto
        data["empresa"] = data["empresa"].title()
        data["puesto"] = data["puesto"].replace("_", " ").replace("eng", "Engineer")

        return render_template("show_form_data.html", data = data)
    
    # si el método es GET, renderiza el formulario
    # para capturar los datos

    companies = ["Google", "Microsoft", "OpenAI", "Anthropic", "Meta"]
    job_positions = ["Ingeniero de Software", "Científico de Datos", "Ingeniero de Machine Learning", "Ingeniero de Datos", "Analista de Datos"]

    return render_template("form2.html",
                           companies = companies,
                           job_positions = job_positions)

# permite que arranquemos la app usando:
# python minimal_app.py
if __name__ == '__main__':
    app.run(debug=True)