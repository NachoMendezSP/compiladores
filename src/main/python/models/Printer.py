from models.ID import *

class Printer:
    def __init__(self):
        # Abrir un solo archivo para toda la salida de la tabla de símbolos
        self.archivo = open("output/tabla_de_simbolos.txt", mode="w", encoding="utf-8")
        self.archivo.write("Tabla de Símbolos:\n\n")
        self.subcontextos = {}

    def lectura(self, contexto, index):
        if index in self.subcontextos:
            self.subcontextos[index] += 1
        else:
            self.subcontextos[index] = 0

        index_full = f"{index}-{self.subcontextos[index]}"
        self.archivo.write(f"Contexto: {index_full}\n")

        # Escribir cada entrada de contexto en el archivo único
        for clave in contexto:
            self.archivo.write(f"{str(contexto[clave])}\n")
        self.archivo.write("\n")  # Agrega una línea en blanco entre contextos para mejor legibilidad

    def cerrar(self):
        # Cerrar el archivo al finalizar
        self.archivo.close()
