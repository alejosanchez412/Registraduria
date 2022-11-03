from Modelos.Resultados import Resultados
from Repositorios.ResultadosRepositorio import ResultadosRepositorio

class ControladorResultados():

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

    #func para crear un estudiante
    def create(self,elResultado):
        print("Crear un estudiante")
        #elEstudiante = Estudiante(elEstudiante)
        #return elEstudiante.__dict__
        elResultado = Resultados(elResultado)
        return self.resultadosRepositorio.save(elResultado)

    #Funcion para mostrar un estudiante por id
    def show(self,id):
        print("Mostrando un estudiante con id", id)
        """
        elEstudiante = {
            "_id": id,
            "cedula": "123",
            "nombre": "Juan",
            "apellido": "Perez"
        }
        return elEstudiante
        """
        elResultado = Resultados(self.resultadosRepositorio.findById(id))
        return elResultado.__dict__

    #Func para actualizar un estudiante
    def update(self, id, elResultado):
        print("Actualizando estudiante con id", id)
        #elEstudiante = Estudiante(elEstudiante)
        #return  elEstudiante.__dict__
        ResultadoActual = Resultados(self.resultadosRepositorio.findById(id))
        #estudianteActual.cedula = elEstudiante["cedula"]
        #estudianteActual.nombre = elEstudiante["nombre"]
        #estudianteActual.apellido = elEstudiante["apellido"]
        return self.resultadosRepositorio.save(ResultadoActual)

    #Func para eliminar un estudiante
    def delete(self, id):
        print("Eliminando estudiante con id", id)
        #return {"deleted_count": 1}
        return self.resultadosRepositorio.delete(id)