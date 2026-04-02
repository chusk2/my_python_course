from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/form", methods = ["GET", "POST"])
def form():
    if request.method == "POST":
        data = {
        "name" : request.form.get["name"],
        "age" : request.form.get["age"],
        "company" : request.form.get["company"],
        "position" :request.form.get["position"],
        }
        return render_template("show_form_data.html", data = data)
    
    return render_template("basic_form.html")

# permite que arranquemos la app usando:
# python minimal_app.py
if __name__ == '__main__':
    app.run(debug=True)