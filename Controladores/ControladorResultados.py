from Repositorios.ResultadosRepositorio import ResultadosRepositorio 
from Repositorios.MesasRepositorio import MesasRopositorio
from Repositorios.CandidatosRepositorio import CandidatosRepositorio
from Modelos.Resultados import Resultados
from Modelos.Mesas import Mesas
from Modelos.Candidatos import Candidatos

class ControladorResultados():

    def __init__(self):
        self.relsutadorepositorio = ResultadosRepositorio()
        self.candidatorepositorio = CandidatosRepositorio()
        self.mesarepositorio = MesasRopositorio()

    def index(self):
        return self.relsutadorepositorio.findAll()

#Asignacion estudiante y materia
    def create(self, inforesultado, id_candidato, id_mesa):
        nuevoResultado = Resultados(inforesultado)
        elCandidato = Candidatos(self.candidatorepositorio.findById(id_candidato))
        laMesa = Mesas(self.mesarepositorio.findById(id_mesa))
        nuevoResultado.candidato = elCandidato
        nuevoResultado.mesa = laMesa
        return self.relsutadorepositorio.save(nuevoResultado)

    def show(self, id):
        elResultado = ResultadosRepositorio(self.relsutadorepositorio.findById(id))
        return elResultado.__dict__


    def update(self, id, inforesultado, id_candidato, id_mesa):
        elResultado = Resultados(self.relsutadorepositorio.findById(id))
        elResultado.votos = inforesultado["votos"]
        elResultado.candidato = inforesultado["candidato"]
        elCandidato = Candidatos(self.candidatorepositorio.findById(id_candidato))
        laMesa = Mesas(self.mesarepositorio.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.relsutadorepositorio.save(elResultado)

    def delete(self, id):
        return self.relsutadorepositorio.delete(id)

    def listarResultadosEnMesas(self, id_mesa):
        return self.relsutadorepositorio.getListadoResultadosEnMesas(id_mesa)
    