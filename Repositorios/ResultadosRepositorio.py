from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados

class ResultadosRepositorio(InterfaceRepositorio[Resultados]):

        def getListadoResultadosEnMesas(self, id_mesa):
        theQuery = {"mesas.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

