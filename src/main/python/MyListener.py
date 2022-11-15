# Generated from /home/nacho/Downloads/compiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from sys import modules
from antlr4 import *
from models.Tabla import *
from models.ID import *
from models.Variable import *
from models.Funcion import *
from models.Printer import *

if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class MyListener(ParseTreeListener):

    tabla = Tabla()
    impresora = Printer()



#Contexto global, desde el inicio hasta el final del programa.

    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Start")
        self.tabla.addContexto()

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.tabla.delContexto()
        print("End")

#Se agrega contexto en los bloques que siguen a if, for, while.

    # Enter a parse tree produced by compiladoresParser#estructuras_control.
    def enterEstructuras_control(self, ctx:compiladoresParser.Estructuras_controlContext):
        print("Inicio estructura control")
        self.tabla.addContexto()

    # Exit a parse tree produced by compiladoresParser#estructuras_control.
    def exitEstructuras_control(self, ctx:compiladoresParser.Estructuras_controlContext):
        self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.tabla.delContexto()
        print("Fin estructura control")

#Se agrega contexto al entrar a un bloque.

    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        print("Inicio bloque")
        self.tabla.addContexto()

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        print("Fin bloque")
        self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.tabla.delContexto()

#Se agregan variables a la Tabla de Simbolos.

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        var_id = ctx.ID().getText()
        asignacion = ctx.IGUAL() != None or ctx.UMAS() != None or ctx.UMENOS() != None
        var = Variable(var_id, '', asignacion, False)
        try:
            tipo_dato = ctx.parentCtx.tipo_dato().getText()
            var = Variable(var_id, tipo_dato, asignacion, False)
            self.tabla.addID(var)
        except:
            if self.tabla.buscarID(var):
                for d in self.tabla.ts[::-1]:
                    if var_id in d:
                        d[var_id].inicializada = asignacion
                        d[var_id].usada = True
                        break
            else:
                print(var_id, "No existe.")

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        if ctx.ID() != None:
            var_id = ctx.ID().getText()
            var = Variable(var_id, 'x', False, False)
            if self.tabla.buscarID(var):
                for d in self.tabla.ts[::-1]:
                    if var_id in d:
                        d[var_id].usada = True
                        break
            else:
                print(var_id, "No existe.")

    # Exit a parse tree produced by compiladoresParser#lista_asignables.
    def exitAsignables(self, ctx:compiladoresParser.AsignablesContext):
        if ctx.asignable().ID() != None:
            var_id = ctx.asignable().ID().getText()
            if var_id in self.tabla.ts[-1]:
                self.tabla.ts[-1][var_id].usada = True
            else:
                print(var_id, "No existe.")

#Se agrega un contexto al declarar una funcion seguida de bloque.

    # Exit a parse tree produced by compiladoresParser#firma.
    def exitFirma(self, ctx:compiladoresParser.FirmaContext):
        fun_id = ctx.ID().getText()
        acceso = ctx.acceso().getText() if ctx.acceso() != None else ''
        tipo = (acceso + ' ' if acceso != '' else '') + ctx.tipo_retorno().getText()

        parametros = []
        lista_actual = ctx.parametros()[0]
        while(lista_actual != None):
            par_id = lista_actual.parametro().ID().getText()
            par_tipo = lista_actual.parametro().tipo_dato().getText()
            par = Variable(par_id, par_tipo, True, False)

            parametros.append(par)
            lista_actual = lista_actual.parametros()

        self.tabla.addID(Funcion(fun_id, tipo, True, False, parametros))

        print("Contexto de funcion")
        self.tabla.addContexto()
        for par in parametros:
            self.tabla.addID(par)

    # Exit a parse tree produced by compiladoresParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.tabla.delContexto()
        print("Fin contexto de funcion")

del compiladoresParser