from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime
from json import dumps

app = Flask(__name__)
CORS(app)

operaciones = []

class Historial():
    def __init__(self, a, b, fecha, tipoOperacion, resultado):
        self.a = a
        self.b = b
        self.fecha = fecha
        self.tipoOperacion = tipoOperacion
        self.resultado = resultado



@app.route('/',methods=['GET'])
def index():
    return '<h2>Practica Presencial IPC1</h2>'

@app.route('/suma',methods=['POST'])
def suma():
    
    a = request.json['a']
    b = request.json['b']

    try:
        resultado = float(a) + float(b)
        mensaje = 'Operacion realizada con exito'
    except Exception as identifier:
        resultado = 0
        mensaje  = 'Ocurrio un error:' + str(identifier)

    
    fecha = datetime.datetime.now
    tipoOperacion = 'suma'
    new_operacion = Historial(a,b,fecha,tipoOperacion,resultado)
    operaciones.append(new_operacion)
    return jsonify(resultado=resultado,mensaje=mensaje)

    

@app.route('/resta',methods=['POST'])
def resta():
    a = request.json['a']
    b = request.json['b']

    try:
        resultado = float(a) - float(b)
        mensaje = 'Operacion realizada con exito'
    except Exception as identifier:
        resultado = 0
        mensaje  = 'Ocurrio un error:' + str(identifier)

    fecha = datetime.datetime.now
    tipoOperacion = 'resta'
    new_operacion = Historial(a,b,fecha,tipoOperacion,resultado)
    operaciones.append(new_operacion)

    return jsonify(resultado=resultado,mensaje=mensaje)


@app.route('/multiplicacion',methods=['POST'])
def multiplicacion():
    a = request.json['a']
    b = request.json['b']

    try:
        resultado = float(a) * float(b)
        mensaje = 'Operacion realizada con exito'
    except Exception as identifier:
        resultado = 0
        mensaje  = 'Ocurrio un error:' + str(identifier)

    fecha = datetime.datetime.now
    tipoOperacion = 'multiplicacion'
    new_operacion = Historial(a,b,fecha,tipoOperacion,resultado)
    operaciones.append(new_operacion)

    return jsonify(resultado=resultado,mensaje=mensaje)

@app.route('/division',methods=['POST'])
def division():
    a = request.json['a']
    b = request.json['b']

    try:
        resultado = float(a) / float(b)
        resultado = round(resultado,2)
        mensaje = 'Operacion realizada con exito'
    except Exception as identifier:
        resultado = -1
        mensaje  = 'Ocurrio un error:' + str(identifier)

    fecha = datetime.datetime.now
    tipoOperacion = 'division'
    new_operacion = Historial(a,b,fecha,tipoOperacion,resultado)
    operaciones.append(new_operacion)

    return jsonify(resultado=resultado,mensaje=mensaje)

@app.route('/potencia',methods=['POST'])
def potencia():
    a = request.json['a']
    b = request.json['b']

    try:
        resultado = float(a) ** float(b)
        mensaje = 'Operacion realizada con exito'
    except Exception as identifier:
        resultado = 0
        mensaje  = 'Ocurrio un error:' + str(identifier)

    fecha = datetime.datetime.now
    tipoOperacion = 'potencia'
    new_operacion = Historial(a,b,fecha,tipoOperacion,resultado)
    operaciones.append(new_operacion)

    return jsonify(resultado=resultado,mensaje=mensaje)

@app.route('/raiz',methods=['POST'])
def raiz():
    a = request.json['a']
    b = request.json['b']

    try:
        resultado = float(a) ** (1/float(b))
        mensaje = 'Operacion realizada con exito'
    except Exception as identifier:
        resultado = 0
        mensaje  = 'Ocurrio un error:' + str(identifier)

    fecha = datetime.datetime.now
    tipoOperacion = 'raiz'
    new_operacion = Historial(a,b,fecha,tipoOperacion,resultado)

    return jsonify(resultado=resultado,mensaje=mensaje)

@app.route('/historial',methods=['GET'])
def historial():
    
    data = []

    for o in operaciones:
        obj = {
            'a': o.a,
            'b': o.b,
            'fecha': o.fecha,
            'tipoOperacion' : o.tipoOperacion,
            'resultado':o.resultado
        }
        data.append(obj)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
