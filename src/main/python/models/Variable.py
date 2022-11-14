from models.ID import *


class Variable(ID):
    def __str__(self):
        return "VARIABLE: Nombre: "+self.nombre+", Tipo: "+self.tipo+", Inicializada: "+str(self.inicializada)+", Usada: "+str(self.usada)
