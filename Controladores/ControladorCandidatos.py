from Repositorios.CandidatosRepositorio import CandidatosRepositorio
from Modelos.Candidatos import Candidatos

class ControladorCandidato():

    def __init__(self):
        self.candidatoRepositorio = CandidatosRepositorio()

    def index(self):
        return self.candidatoRepositorio.findAll()

    def create(self, infoCandidato):
        nuevoCandidato = Candidatos(infoCandidato)
        return self.candidatoRepositorio.save(nuevoCandidato)

    def show(self, id):
        return self.candidatoRepositorio.findById(id)


    def update(self, id, infoCandidato):
        candidatoActual = Candidatos(self.candidatoRepositorio.findById(id))
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.numero_resulucion = infoCandidato["numero_resolucion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]

        return self.candidatoRepositorio.save(candidatoActual)

    def delete(self, id):
        return self.candidatoRepositorio.delete(id)
