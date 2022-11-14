from models.ID import *

class Printer():

    num_contextos = {}

    def __init__(self):
        pass

    def lectura(self, contexto, index):
        print("Index: ", index)
        print(contexto)
        if index in self.num_contextos:
            self.num_contextos[index] += 1
        else:
            self.num_contextos[index] = 0

        index_full = str(index) + "-" + str(self.num_contextos[index])

        path = "output/contexto"
        # path = "../txt/contexto"

        archivo = open(path + index_full + ".txt", mode="w+", encoding="utf-8")
        archivo.write("****** Contexto " + index_full + " ******\n")
        for clave in contexto:
            archivo.write(str(contexto[clave]))
            archivo.write("\n")
