from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorCandidatos import ControladorCandidato
from Controladores.ControladorMesas import ControladorMesas
from Controladores.ControladorPartidos import ControladorPartidos
from Controladores.ControladorResultados import ControladorResultados

app = Flask(__name__)
cors = CORS(app)

miControladorCandidatos = ControladorCandidato()
miControladorMesas = ControladorMesas()
miControladorPartidos = ControladorPartidos()
miControladorResultados = ControladorResultados()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

#Carga el archivo json ,lo lee y lo resonator
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

#####################Servicios Candidato#########################################################################
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json = miControladorCandidatos.index()
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json = miControladorCandidatos.show(id)
    return jsonify(json)

@app.route("/candidatos",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidatos.create(data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidatos.update(id,data)
    return jsonify(json)

@app.route("/candidatos/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidatos.delete(id)
    return jsonify(json)


#################################################################################################################

#####################Servicios Mesas M######################################################################
@app.route("/mesas",methods=['POST'])
def crearMesas():
    data = request.get_json()
    json = miControladorMesas.create(data)
    return jsonify(json)

@app.route("/mesas",methods=['GET'])
def getMesas():
    json = miControladorMesas.index()
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesas(id):
    data = request.get_json()
    json = miControladorMesas.update(id,data)
    return jsonify(json)

@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesas(id):
    json = miControladorMesas.delete(id)
    return jsonify(json)


#################################################################################################################



#####################Servicios Partidos##########################################################################
@app.route("/partidos",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json = miControladorPartidos.create(data)
    return jsonify(json)

@app.route("/partidos",methods=['GET'])
def getPartidos():
    json = miControladorPartidos.index()
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartidos.update(id,data)
    return jsonify(json)

@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json = miControladorPartidos.delete(id)
    return jsonify(json)

@app.route("/partidos/<string:id>/candidatos/<string:id_candidato>",methods=['PUT'])
def asignarCandidato(id, id_candidato):
    json = miControladorPartidos.asignarCandidato(id, id_candidato)
    return jsonify(json)


#################################################################################################################

###################################Servicios Resultados#########################################################
@app.route("/resultados",methods=['GET'])
def getResultados():
    json = miControladorResultados.index()
    return jsonify(json)

@app.route("/resultados/partidos/<string:id_partido>/mesas/<string:id_mesa>",methods=['POST'])
def crearResultado(id_partido, id_mesa):
    data = request.get_json()
    json = miControladorResultados.create(data, id_partido, id_mesa)
    return jsonify(json)

@app.route("/resultados/<string:id>",methods=['DELETE'])
def eliminarResuldato(id):
    json = miControladorResultados.delete(id)
    return jsonify(json)


@app.route("/resultados/mesas/<string:id_mesa>",methods=['GET'])
def resultadosenMesas(id_mesa):
    json = miControladorResultados.listarResultadosEnMesas(id_mesa)
    return jsonify(json)

#################################################################################################################

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
