class Tabla():

    class __Tabla:
        def __init__(self):
            self.ts = []

        def buscarID(self, ID):
            for d in self.ts[::-1]:
                if ID.nombre in d:
                    return True

        def buscarIDlocal(self, ID):
            return ID.nombre in self.ts[-1]

        def addID(self, ID):
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
