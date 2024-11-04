# MyListener.py

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

# Esta clase define un listener completo para el árbol de parseo producido por compiladoresParser.
class MyListener(ParseTreeListener):

    def __init__(self):
        self.tabla = Tabla()
        self.impresora = Printer()
        self.errores = []

    def registrar_error(self, mensaje):
        self.errores.append(mensaje)

    def enterPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Start")
        self.tabla.addContexto()

    def exitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        # Solo generar tabla de símbolos si no hay errores
        if not self.errores:
            self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.tabla.delContexto()
        print("End")

    def enterEstructuras_control(self, ctx: compiladoresParser.Estructuras_controlContext):
        print("Inicio estructura control")
        self.tabla.addContexto()

    def exitEstructuras_control(self, ctx: compiladoresParser.Estructuras_controlContext):
        # Solo genera archivos de contexto si no hay errores
        if not self.errores:
            self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.tabla.delContexto()
        print("Fin estructura control")

    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        print("Inicio bloque")
        self.tabla.addContexto()

    def exitBloque(self, ctx: compiladoresParser.BloqueContext):
        # Solo genera archivos de contexto si no hay errores
        if not self.errores:
            self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.tabla.delContexto()
        print("Fin bloque")

    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        var_id = ctx.ID().getText()
        asignacion = ctx.IGUAL() is not None or ctx.UMAS() is not None or ctx.UMENOS() is not None
        var = Variable(var_id, '', asignacion, False)
        try:
            tipo_dato = ctx.parentCtx.tipo_dato().getText()
            var = Variable(var_id, tipo_dato, asignacion, False)
            if self.tabla.buscarID(var):
                self.registrar_error(f"Error semántico: Doble declaración de identificador '{var_id}'")
            else:
                self.tabla.addID(var)
        except:
            if not self.tabla.buscarID(var):
                self.registrar_error(f"Error semántico: Uso de identificador no declarado '{var_id}'")

    def exitFactor(self, ctx: compiladoresParser.FactorContext):
        if ctx.ID() is not None:
            var_id = ctx.ID().getText()
            var = Variable(var_id, 'x', False, False)
            if not self.tabla.buscarID(var):
                self.registrar_error(f"Error semántico: Uso de identificador no declarado '{var_id}'")

    def exitAsignables(self, ctx: compiladoresParser.AsignablesContext):
        if ctx.asignable().ID() is not None:
            var_id = ctx.asignable().ID().getText()
            if var_id not in self.tabla.ts[-1]:
                self.registrar_error(f"Error semántico: Uso de identificador no declarado '{var_id}'")

    def exitFirma(self, ctx: compiladoresParser.FirmaContext):
        fun_id = ctx.ID().getText()
        acceso = ctx.acceso().getText() if ctx.acceso() is not None else ''
        tipo = (acceso + ' ' if acceso != '' else '') + ctx.tipo_retorno().getText()

        parametros = []
        lista_actual = ctx.parametros()[0]
        while lista_actual is not None:
            par_id = lista_actual.parametro().ID().getText()
            par_tipo = lista_actual.parametro().tipo_dato().getText()
            par = Variable(par_id, par_tipo, True, False)
            parametros.append(par)
            lista_actual = lista_actual.parametros()

        if self.tabla.buscarID(Funcion(fun_id, tipo, True, False, parametros)):
            self.registrar_error(f"Error semántico: Doble declaración de función '{fun_id}'")
        else:
            self.tabla.addID(Funcion(fun_id, tipo, True, False, parametros))
            print("Contexto de funcion")
            self.tabla.addContexto()
            for par in parametros:
                self.tabla.addID(par)

    def exitDeclaracion_funcion(self, ctx: compiladoresParser.Declaracion_funcionContext):
        # Solo genera archivos de contexto si no hay errores
        if not self.errores:
            self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.tabla.delContexto()
        print("Fin contexto de funcion")

del compiladoresParser
