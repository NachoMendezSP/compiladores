# Generated from /home/nacho/Downloads/DHS-Mendez/compiladores/src/main/python/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#tipo_dato.
    def visitTipo_dato(self, ctx:compiladoresParser.Tipo_datoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#programa.
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#lineas.
    def visitLineas(self, ctx:compiladoresParser.LineasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#instruccion.
    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#estructuras_control.
    def visitEstructuras_control(self, ctx:compiladoresParser.Estructuras_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque.
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_alt.
    def visitBloque_alt(self, ctx:compiladoresParser.Bloque_altContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#estructuras.
    def visitEstructuras(self, ctx:compiladoresParser.EstructurasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignable.
    def visitAsignable(self, ctx:compiladoresParser.AsignableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#variable.
    def visitVariable(self, ctx:compiladoresParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion.
    def visitDeclaracion(self, ctx:compiladoresParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignacion.
    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignaciones.
    def visitAsignaciones(self, ctx:compiladoresParser.AsignacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#igualacion.
    def visitIgualacion(self, ctx:compiladoresParser.IgualacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#relacion.
    def visitRelacion(self, ctx:compiladoresParser.RelacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#comparacion.
    def visitComparacion(self, ctx:compiladoresParser.ComparacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#booleanos.
    def visitBooleanos(self, ctx:compiladoresParser.BooleanosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#expresion.
    def visitExpresion(self, ctx:compiladoresParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#termino.
    def visitTermino(self, ctx:compiladoresParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#factor.
    def visitFactor(self, ctx:compiladoresParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iif.
    def visitIif(self, ctx:compiladoresParser.IifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#iwhile.
    def visitIwhile(self, ctx:compiladoresParser.IwhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#ifor.
    def visitIfor(self, ctx:compiladoresParser.IforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#funcion.
    def visitFuncion(self, ctx:compiladoresParser.FuncionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#bloque_funcion.
    def visitBloque_funcion(self, ctx:compiladoresParser.Bloque_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#tipo_retorno.
    def visitTipo_retorno(self, ctx:compiladoresParser.Tipo_retornoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#acceso.
    def visitAcceso(self, ctx:compiladoresParser.AccesoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parametro.
    def visitParametro(self, ctx:compiladoresParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#parametros.
    def visitParametros(self, ctx:compiladoresParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#asignables.
    def visitAsignables(self, ctx:compiladoresParser.AsignablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#firma.
    def visitFirma(self, ctx:compiladoresParser.FirmaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#firma_prototipo.
    def visitFirma_prototipo(self, ctx:compiladoresParser.Firma_prototipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#prototipo_funcion.
    def visitPrototipo_funcion(self, ctx:compiladoresParser.Prototipo_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#declaracion_funcion.
    def visitDeclaracion_funcion(self, ctx:compiladoresParser.Declaracion_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#llamada_funcion.
    def visitLlamada_funcion(self, ctx:compiladoresParser.Llamada_funcionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by compiladoresParser#retorno.
    def visitRetorno(self, ctx:compiladoresParser.RetornoContext):
        return self.visitChildren(ctx)



del compiladoresParser