from models.ID import *

class Funcion(ID):

    def __init__(self, nombre, tipo, inicializada, usada, parametros):
        super().__init__(nombre, tipo, inicializada, usada)
        self.parametros = parametros

    def __str__(self):
        return "FUNCION: Nombre: "+self.nombre+", Tipo: "+self.tipo+", Inicializada: "+str(self.inicializada)+", Usada: "+str(self.usada)

# Parametros
    @property
    def parametros(self):
        return self.__parametros

    @parametros.setter
    def parametros(self, val):
        self.__parametros = val
