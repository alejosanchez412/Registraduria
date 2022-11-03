from Repositorios.MesasRepositorio import MesasRopositorio
from Modelos.Mesas import Mesas

class ControladorMesas():

    def __init__(self):
        self.mesasRepositorio = MesasRopositorio()

    def index(self):
        return self.mesasRepositorio.findAll()

    def create(self, infoMesas):
        nuevaMesa = Mesas(infoMesas)
        return self.mesasRepositorio.save(nuevaMesa)

    def show(self, id):
        laMesa = Mesas(self.mesasRepositorio.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesas):
        MesasActual = Mesas(self.mesasRepositorio.findById(id))
        MesasActual.numero = infoMesas["numero"]
        MesasActual.cantidad_inscritos = infoMesas["cantidad_inscritos"]
        return self.mesasRepositorio.save(MesasActual)

    def delete(self, id):
        return self.mesasRepositorio.delete(id)