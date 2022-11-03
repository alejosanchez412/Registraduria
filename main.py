from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorResultados import ControladorResultados

app = Flask(__name__)
cors = CORS(app)

miControladorResultados = ControladorResultados()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

#Endpoint para mostrar todos los Resultados
@app.route("/resultados",methods=['GET'])
def getEstudiantes():
    json = miControladorResultados.index()
    return jsonify(json)

#Endpoint para mostrar un Resultados por una llave
@app.route("/resultados/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorResultados.show(id)
    return jsonify(json)

#Endpoint para crear un Resultados
@app.route("/resultados",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json = miControladorResultados.create(data)
    return  jsonify(json)

#Endpoint para actualizar un Resultados
@app.route("/resultados/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json = miControladorResultados.update(id,data)
    return jsonify(json)

#Endpoint para eliminar un Resultados
@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json = miControladorResultados.delete(id)
    return jsonify(json)




# lee el archivo config.json
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
