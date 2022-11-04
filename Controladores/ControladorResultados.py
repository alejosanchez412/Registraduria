from Modelos.Candidatos import Candidatos
from Modelos.Mesas import Mesas
from Modelos.Resultados import Resultados
from Repositorios.CandidatosRepositorio import CandidatosRepositorio
from Repositorios.MesasRepositorio import MesasRopositorio
from Repositorios.ResultadosRepositorio import ResultadosRepositorios
from bson import ObjectId


class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = ResultadosRepositorios()
        self.repositorioCandidato = CandidatosRepositorio()
        self.repositorioMesa = MesasRopositorio()

    def createResultado(self, infoResultado, idM, idC):
        elresultado = Resultados(infoResultado)
        lamesa = Mesas(self.repositorioMesa.findById(idM))
        elcandidato = Candidatos(self.repositorioCandidato.findById(idC))
        elresultado.mesa = lamesa
        elresultado.candidato = elcandidato
        return self.repositorioResultado.save(elresultado)

    def showidResultado(self, id):
        resultado = Resultados(self.repositorioResultado.findById(id))
        return resultado.__dict__

    def showallResultado(self):
        return self.repositorioResultado.findAll()

    def updateResultado(self, idR, idM, idC, infoResultado):
        resultadoactual = Resultados(self.repositorioResultado.findById(idR))
        lamesa = Mesas(self.repositorioMesa.findById(idM))
        elcandido = Candidatos(self.repositorioCandidato.findById(idC))
        resultadoactual.mesa = lamesa
        resultadoactual.candidato = elcandido
        resultadoactual.numero_votos = infoResultado["numero_votos"]
        return self.repositorioResultado.save(resultadoactual)

    def deleteResultado(self, id):
        return self.repositorioResultado.delete(id)

    def listarresultadoscandidato(self, idCa):
        return self.repositorioResultado.getlistResultadosCandidato(idCa)
    