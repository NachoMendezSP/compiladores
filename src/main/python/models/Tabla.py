class Tabla():

    class __Tabla:
        def __init__(self):
            self.ts = []

        def buscarID(self, ID):
            for d in self.ts[::-1]:
                if ID.nombre in d:
                    print(f"Encontrado {ID.nombre} en la tabla de símbolos")
                    return d[ID.nombre]
            print(f"No encontrado {ID.nombre} en la tabla de símbolos")
            return None

        def buscarIDlocal(self, ID):
            return self.ts[-1].get(ID.nombre)

        def addID(self, ID):
            print(f"Agregando a la tabla de símbolos: {ID.nombre} con tipo {ID.tipo}, inicializada: {ID.inicializada}, usada: {ID.usada}")
            self.ts[-1].update({ID.nombre: ID})

        def addContexto(self):
            print("Contexto nuevo.")
            self.ts.append(dict())

        def delContexto(self):
            print("Fin del contexto.")
            del self.ts[-1]

    instance = None

    def __init__(self):
        if not Tabla.instance:
            Tabla.instance = Tabla.__Tabla()

    def __getattr__(self, name):
        return getattr(self.instance, name)
