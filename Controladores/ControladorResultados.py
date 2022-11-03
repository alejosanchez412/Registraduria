from Repositorios.ResultadosRepositorio import ResultadosRepositorio 
from Repositorios.MesasRepositorio import MesasRopositorio
from Repositorios.PartidosRepositorio import PartidosRepositorio
from Modelos.Resultados import Resultados
from Modelos.Mesas import Mesas
from Modelos.Partidos import Partidos

class ControladorResultados():

    def __init__(self):
        self.relsutadorepositorio = ResultadosRepositorio()
        self.partidorepositorio = PartidosRepositorio()
        self.mesarepositorio = MesasRopositorio()

    def index(self):
        return self.relsutadorepositorio.findAll()


    def create(self, inforesultado, id_partido, id_mesa):
        nuevoResultado = Resultados(inforesultado)
        elPartido = Partidos(self.partidorepositorio.findById(id_partido))
        laMesa = Mesas(self.mesarepositorio.findById(id_mesa))
        nuevoResultado.partido = elPartido
        nuevoResultado.mesa = laMesa
        return self.relsutadorepositorio.save(nuevoResultado)

    def show(self, id):
        elResultado = Resultados(self.relsutadorepositorio.findById(id))
        return elResultado.__dict__


    def update(self, id, inforesultado, id_partido, id_mesa):
        elResultado = Resultados(self.relsutadorepositorio.findById(id))
        elResultado.numero_votos = inforesultado["numero_votos"]
        elPartido = Partidos(self.partidorepositorio.findById(id_partido))
        laMesa = Mesas(self.mesarepositorio.findById(id_mesa))
        elResultado.partido = elPartido
        elResultado.mesa = laMesa
        return self.relsutadorepositorio.save(elResultado)

    def delete(self, id):
        return self.relsutadorepositorio.delete(id)

    def listarResultadosEnMesas(self, id_mesa):
        return self.relsutadorepositorio.getListadoResultadosEnMesas(id_mesa)
    