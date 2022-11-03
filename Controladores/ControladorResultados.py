from Modelos.Resultados import Resultados
from Repositorios.ResultadosRepositorio import ResultadosRepositorio

class ControladorResultados():

    def __init__(self):
        self.resultadosRepositorio = ResultadosRepositorio()

    #Func para listar los Resultados
    def index(self):
        return self.resultadosRepositorio.findAll()

    #func para crear un estudiante
    def create(self,elResultado):
        elResultado = Resultados(elResultado)
        return self.resultadosRepositorio.save(elResultado)

    #Funcion para mostrar un estudiante por id
    def show(self,id):
        elResultado = Resultados(self.resultadosRepositorio.findById(id))
        return elResultado.__dict__

    #Func para actualizar un estudiante
    def update(self, id, elResultado):
        ResultadoActual = Resultados(self.resultadosRepositorio.findById(id))
        ResultadoActual.numero_mesa = elResultado["numero_mesa"]
        ResultadoActual.id_partido = elResultado["id_partido"]
        return self.resultadosRepositorio.save(ResultadoActual)

    #Func para eliminar un estudiante
    def delete(self, id):
        return self.resultadosRepositorio.delete(id)