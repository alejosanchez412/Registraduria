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
        elCandidato = Candidatos(self.candidatoRepositorio.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        candidatoActual = Candidatos(self.candidatoRepositorio.findById(id))
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        candidatoActual.numero_resulucion = infoCandidato["numero_resolucion"]
        return self.candidatoRepositorio.save(candidatoActual)

    def delete(self, id):
        return self.candidatoRepositorio.delete(id)
