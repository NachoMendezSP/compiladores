# Generated from /home/nacho/Downloads/compiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete listener for a parse tree produced by compiladoresParser.
class compiladoresListener(ParseTreeListener):

    # Enter a parse tree produced by compiladoresParser#tipo_dato.
    def enterTipo_dato(self, ctx:compiladoresParser.Tipo_datoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tipo_dato.
    def exitTipo_dato(self, ctx:compiladoresParser.Tipo_datoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#programa.
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#lineas.
    def enterLineas(self, ctx:compiladoresParser.LineasContext):
        pass

    # Exit a parse tree produced by compiladoresParser#lineas.
    def exitLineas(self, ctx:compiladoresParser.LineasContext):
        pass


    # Enter a parse tree produced by compiladoresParser#instruccion.
    def enterInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#instruccion.
    def exitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#estructuras_comp.
    def enterEstructuras_comp(self, ctx:compiladoresParser.Estructuras_compContext):
        pass

    # Exit a parse tree produced by compiladoresParser#estructuras_comp.
    def exitEstructuras_comp(self, ctx:compiladoresParser.Estructuras_compContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque.
    def enterBloque(self, ctx:compiladoresParser.BloqueContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque.
    def exitBloque(self, ctx:compiladoresParser.BloqueContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque_alt.
    def enterBloque_alt(self, ctx:compiladoresParser.Bloque_altContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque_alt.
    def exitBloque_alt(self, ctx:compiladoresParser.Bloque_altContext):
        pass


    # Enter a parse tree produced by compiladoresParser#estructuras.
    def enterEstructuras(self, ctx:compiladoresParser.EstructurasContext):
        pass

    # Exit a parse tree produced by compiladoresParser#estructuras.
    def exitEstructuras(self, ctx:compiladoresParser.EstructurasContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignable.
    def enterAsignable(self, ctx:compiladoresParser.AsignableContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignable.
    def exitAsignable(self, ctx:compiladoresParser.AsignableContext):
        pass


    # Enter a parse tree produced by compiladoresParser#variable.
    def enterVariable(self, ctx:compiladoresParser.VariableContext):
        pass

    # Exit a parse tree produced by compiladoresParser#variable.
    def exitVariable(self, ctx:compiladoresParser.VariableContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion.
    def enterDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion.
    def exitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignacion.
    def enterAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignacion.
    def exitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignaciones.
    def enterAsignaciones(self, ctx:compiladoresParser.AsignacionesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignaciones.
    def exitAsignaciones(self, ctx:compiladoresParser.AsignacionesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#igualacion.
    def enterIgualacion(self, ctx:compiladoresParser.IgualacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#igualacion.
    def exitIgualacion(self, ctx:compiladoresParser.IgualacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#relacion.
    def enterRelacion(self, ctx:compiladoresParser.RelacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#relacion.
    def exitRelacion(self, ctx:compiladoresParser.RelacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#comparacion.
    def enterComparacion(self, ctx:compiladoresParser.ComparacionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#comparacion.
    def exitComparacion(self, ctx:compiladoresParser.ComparacionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#booleanos.
    def enterBooleanos(self, ctx:compiladoresParser.BooleanosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#booleanos.
    def exitBooleanos(self, ctx:compiladoresParser.BooleanosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#expresion.
    def enterExpresion(self, ctx:compiladoresParser.ExpresionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#expresion.
    def exitExpresion(self, ctx:compiladoresParser.ExpresionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#termino.
    def enterTermino(self, ctx:compiladoresParser.TerminoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#termino.
    def exitTermino(self, ctx:compiladoresParser.TerminoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#factor.
    def enterFactor(self, ctx:compiladoresParser.FactorContext):
        pass

    # Exit a parse tree produced by compiladoresParser#factor.
    def exitFactor(self, ctx:compiladoresParser.FactorContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iif.
    def enterIif(self, ctx:compiladoresParser.IifContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iif.
    def exitIif(self, ctx:compiladoresParser.IifContext):
        pass


    # Enter a parse tree produced by compiladoresParser#iwhile.
    def enterIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass

    # Exit a parse tree produced by compiladoresParser#iwhile.
    def exitIwhile(self, ctx:compiladoresParser.IwhileContext):
        pass


    # Enter a parse tree produced by compiladoresParser#ifor.
    def enterIfor(self, ctx:compiladoresParser.IforContext):
        pass

    # Exit a parse tree produced by compiladoresParser#ifor.
    def exitIfor(self, ctx:compiladoresParser.IforContext):
        pass


    # Enter a parse tree produced by compiladoresParser#funcion.
    def enterFuncion(self, ctx:compiladoresParser.FuncionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#funcion.
    def exitFuncion(self, ctx:compiladoresParser.FuncionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#bloque_funcion.
    def enterBloque_funcion(self, ctx:compiladoresParser.Bloque_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#bloque_funcion.
    def exitBloque_funcion(self, ctx:compiladoresParser.Bloque_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#tipo_retorno.
    def enterTipo_retorno(self, ctx:compiladoresParser.Tipo_retornoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#tipo_retorno.
    def exitTipo_retorno(self, ctx:compiladoresParser.Tipo_retornoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#acceso.
    def enterAcceso(self, ctx:compiladoresParser.AccesoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#acceso.
    def exitAcceso(self, ctx:compiladoresParser.AccesoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#parametro.
    def enterParametro(self, ctx:compiladoresParser.ParametroContext):
        pass

    # Exit a parse tree produced by compiladoresParser#parametro.
    def exitParametro(self, ctx:compiladoresParser.ParametroContext):
        pass


    # Enter a parse tree produced by compiladoresParser#parametros.
    def enterParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass

    # Exit a parse tree produced by compiladoresParser#parametros.
    def exitParametros(self, ctx:compiladoresParser.ParametrosContext):
        pass


    # Enter a parse tree produced by compiladoresParser#asignables.
    def enterAsignables(self, ctx:compiladoresParser.AsignablesContext):
        pass

    # Exit a parse tree produced by compiladoresParser#asignables.
    def exitAsignables(self, ctx:compiladoresParser.AsignablesContext):
        pass


    # Enter a parse tree produced by compiladoresParser#firma.
    def enterFirma(self, ctx:compiladoresParser.FirmaContext):
        pass

    # Exit a parse tree produced by compiladoresParser#firma.
    def exitFirma(self, ctx:compiladoresParser.FirmaContext):
        pass


    # Enter a parse tree produced by compiladoresParser#firma_prototipo.
    def enterFirma_prototipo(self, ctx:compiladoresParser.Firma_prototipoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#firma_prototipo.
    def exitFirma_prototipo(self, ctx:compiladoresParser.Firma_prototipoContext):
        pass


    # Enter a parse tree produced by compiladoresParser#prototipo_funcion.
    def enterPrototipo_funcion(self, ctx:compiladoresParser.Prototipo_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#prototipo_funcion.
    def exitPrototipo_funcion(self, ctx:compiladoresParser.Prototipo_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#declaracion_funcion.
    def enterDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#declaracion_funcion.
    def exitDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#llamada_funcion.
    def enterLlamada_funcion(self, ctx:compiladoresParser.Llamada_funcionContext):
        pass

    # Exit a parse tree produced by compiladoresParser#llamada_funcion.
    def exitLlamada_funcion(self, ctx:compiladoresParser.Llamada_funcionContext):
        pass


    # Enter a parse tree produced by compiladoresParser#retorno.
    def enterRetorno(self, ctx:compiladoresParser.RetornoContext):
        pass

    # Exit a parse tree produced by compiladoresParser#retorno.
    def exitRetorno(self, ctx:compiladoresParser.RetornoContext):
        pass



del compiladoresParser