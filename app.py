from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'restaurante'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carta', methods=['GET', 'POST'])
def carta():
    if request.method == 'POST':
        buscar = request.form["buscar"]
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM platos WHERE nomplato LIKE '%" + buscar + "%'")
        platos = cur.fetchall()
        cur.close()
        return render_template('carta.html', data=platos)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM `platos`')
    platos = cur.fetchall()
    return render_template('carta.html', data=platos)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        informacionPlato = {
            "idPlato" : request.form["idPlato"],
            "nombrePlato" : request.form["nombrePlato"],
            "valorPlato" : request.form["valorPlato"],
            "cantidadPlato" : request.form["cantidadPlato"],
        }
        return render_template('registro.html', informacionPlato = informacionPlato)
    return render_template('registro.html')

@app.route('/factura', methods=['GET', 'POST'])
def factura():
    if request.method == 'POST':
        idplato = request.form["idPlato"]
        cantidadPlato = request.form["cantidadPlato"]
        valorPlato = request.form["valorPlato"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        numero = request.form["numero"]
        cur = mysql.connection.cursor()
        valTotal = float(valorPlato) * float(cantidadPlato)
        cur.execute("INSERT INTO `factura` (`nombre`, `apellido`, `email`, `celular`, `idplato`, `cantidad`, `valTotal`) VALUES (%s,%s,%s,%s,%s,%s,%s)", (nombre, apellido, email, numero, idplato, cantidadPlato, valTotal))
        mysql.connection.commit()
        
        lastid = cur.lastrowid

        cur.execute("SELECT f.* , p.* FROM factura as f LEFT JOIN platos as p ON f.idplato = p.id WHERE f.id = " + str(lastid) + ";")
        informacionFactura = cur.fetchall()
        cur.close()
        return render_template('factura.html', informacionFactura = informacionFactura)
    return render_template('factura.html')


if __name__ == "__main__":
    app.run(debug=True)