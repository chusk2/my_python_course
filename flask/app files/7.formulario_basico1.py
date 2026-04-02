from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route('/form', methods=['GET', 'POST'])
def form():
	# si es lectura del formulario,
	# renderiza la página del formulario
	if request.method == 'GET':
		cities = ["madrid", "barcelona", "valencia",
			"sevilla", "zaragoza", "málaga", "murcia",
			"palma", "las palmas", "bilbao" ]
    	# El usuario llegó a la página: simplemente mostramos el formulario
		return render_template('form1.html', cities = cities)
	
	# si se envían los datos del formulario, los procesamos
	if request.method == 'POST':
	
	# request.form es un diccionario con los datos del POST
	# La clave es el atributo `name` del campo HTML
		name = request.form.get('name')          # str o None si no llegó
		age   = request.form.get('age', type=int)  # convierte a int automáticamente
		city = request.form.get('city')
		return f"Tu nombre es {name}, de {age} años, que vive en {city}" 

