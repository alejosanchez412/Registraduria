from Modelos.Resultados import Resultados
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from bson import ObjectId

class ResultadosRepositorios(InterfaceRepositorio[Resultados]):
    def getlistResultadosCandidato(self,idC):
        laquery = {"Candidato.$id": ObjectId(idC)}
        return self.query(laquery)
