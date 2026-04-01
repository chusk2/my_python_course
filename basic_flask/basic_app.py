from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello")
def hello():
	return "Hello Flask! Welcome to your first Flask app!"

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

# uso de parámetros en la url
## podemos definir varias rutas en función de
## si usamos el argumento en la url o no

# ruta con parámetro
@app.route("/greet/<string:name>")
# ruta sin parámetro name
@app.route("/greet")
def greet(name=None):
	if name:
		return f"<h2>¡Hola! ¿Cómo estás, {name}?</h2>"
	else:
		return "<h2>¡Hola, usuario! ¿Cómo estás?</h2>"

# uso un template html
# aplico css con este tag:
# <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
@app.route("/html_template")
def render():
	return render_template("basic_html.html")

# podemos obtener la lista de rutas disponibles
# con este código:

# for rule in app.url_map.iter_rules():
#     print(rule.rule, rule.methods, rule.endpoint)

@app.route("/routes")
def show_links():
	routes = [(i.endpoint, i.rule) for i in app.url_map.iter_rules()
		   if i.endpoint != "static"]
	return render_template("routes.html", routes = routes)
	

@app.route('/form', methods=['GET', 'POST'])
def form():
	# si es lectura del formulario,
	# renderiza la página del formulario
	if request.method == 'GET':
		cities = ["madrid", "barcelona", "valencia",
			"sevilla", "zaragoza", "málaga", "murcia",
			"palma", "las palmas", "bilbao" ]
    	# El usuario llegó a la página: simplemente mostramos el formulario
		return render_template('form.html', cities = cities)
	
	# si se envían los datos del formulario, los procesamos
	if request.method == 'POST':
	
	# request.form es un diccionario con los datos del POST
	# La clave es el atributo `name` del campo HTML
		name = request.form.get('name')          # str o None si no llegó
		age   = request.form.get('age', type=int)  # convierte a int automáticamente
		city = request.form.get('city')
		return f"Tu nombre es {name}, de {age} años, que vive en {city}" 

