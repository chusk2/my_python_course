from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>Bienvenidos a Flask!</h1>"

@app.route("/info")
def info():
      return "<h1>Primeros pasos con Flask en el curso de Python con CodeSpace</h1>"

# permite que arranquemos la app usando:
# python minimal_app.py
if __name__ == '__main__':
    app.run(debug=True)