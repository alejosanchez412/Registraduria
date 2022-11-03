from Modelos.Candidatos import Candidatos
from Repositorios.CandidatosRepositorio import CandidatosRepositorio

class ControladorCandidatos():

    def __init__(self):
        #print("Creando ControladorEstudiante")
        self.resultadosRepositorio = ResultadosRepositorio()

    #Func para listar los Resultados
    def index(self):
        print("Listar todos los estudiantes")
        """
        unEstudiante = {
            "_id": "abc123",
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return [unEstudiante]
        """
        return self.resultadosRepositorio.findAll()