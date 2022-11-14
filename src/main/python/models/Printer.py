from models.ID import *

class Printer():

    subcontextos = {}

    def __init__(self):
        pass

    def lectura(self, contexto, index):
        print("Index:", index)
        print(contexto)
        if index in self.subcontextos:
            self.subcontextos[index] += 1
        else:
            self.subcontextos[index] = 0

        index_full = str(index) + "-" + str(self.subcontextos[index])

        #Genera un archivo para cada contexto y subcontexto.
        archivo = open("output/contexto" + index_full + ".txt", mode="w+", encoding="utf-8")
        archivo.write("Contexto: " + index_full + "\n")
        for clave in contexto:
            archivo.write(str(contexto[clave]))
            archivo.write("\n")
