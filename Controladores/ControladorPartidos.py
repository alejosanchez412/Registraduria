from Repositorios.PartidosRepositorio import PartidosRepositorio
from Repositorios.CandidatosRepositorio import CandidatosRepositorio
from Modelos.Partidos import Partidos
from Modelos.Candidatos import Candidatos

class ControladorPartidos():

    def __init__(self):
        self.partidoRepositorio = PartidosRepositorio()
        self.candidatoRepositorio = CandidatosRepositorio()

    def index(self):
        return self.partidoRepositorio.findAll()

    def create(self, infoPartido):
        nuevoPartido = Partidos(infoPartido)
        return self.partidoRepositorio.save(nuevoPartido)

    def show(self, id):
        elPartido = Partidos(self.partidoRepositorio.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        PartidoActual = Partidos(self.partidoRepositorio.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.partidoRepositorio.save(PartidoActual)

    def delete(self, id):
        return self.partidoRepositorio.delete(id)

    #relacion dep y mat

    def asignarCandidato(self, id, id_candidato):
        partidoActual = Partidos(self.partidoRepositorio.findById(id))
        candidatoActual = Candidatos(self.candidatoRepositorio.findById(id_candidato))
        partidoActual.candidato = candidatoActual
        return self.partidoRepositorio.save(partidoActual)

