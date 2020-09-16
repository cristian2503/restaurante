from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'restaurante'

@app.route('/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre= details['NOMBRE']
        apellido= details['APELLIDO']
        cur.excute("INSERT INTO clientes")
    return render_template('registro.html')

'''@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def carta():
    return render_template('carta.html')
'''

if __name__ == "__main__":
    app.run(debug=True)