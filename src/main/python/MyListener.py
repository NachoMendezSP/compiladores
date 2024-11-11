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
        self.advertencias = []

    def registrar_error(self, mensaje):
        self.errores.append(mensaje)

    def registrar_advertencia(self, mensaje):
        self.advertencias.append(mensaje)

    def enterPrograma(self, ctx: compiladoresParser.ProgramaContext):
        print("Start")
        self.tabla.addContexto()

    def exitPrograma(self, ctx: compiladoresParser.ProgramaContext):
        if not self.errores:
            # Marcar la función 'main' como usada si existe
            main_func = self.tabla.buscarID(Funcion('main', '', True, False, []))
            if main_func:
                main_func.usada = True
                self.tabla.addID(main_func)

            # Emitir advertencias para funciones y variables no usadas o no inicializadas en todos los contextos
            for contexto in self.tabla.ts:  # Recorre todos los contextos, no solo el global
                for simbolo in contexto.values():
                    if isinstance(simbolo, Variable):
                        if not simbolo.usada:
                            self.registrar_advertencia(f"WARNING: La variable '{simbolo.nombre}' fue declarada pero no utilizada.")
                        if not simbolo.inicializada:
                            self.registrar_advertencia(f"WARNING: La variable '{simbolo.nombre}' fue declarada pero no inicializada.")
                    elif isinstance(simbolo, Funcion):
                        if not simbolo.usada:
                            self.registrar_advertencia(f"WARNING: La función '{simbolo.nombre}' fue declarada pero no utilizada.")
            self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        
        self.tabla.delContexto()
        print("End")

        # Imprimir todas las advertencias acumuladas
        if self.advertencias:
            print("\nAdvertencias:")
            for advertencia in self.advertencias:
                print(advertencia)

    def enterEstructuras_control(self, ctx: compiladoresParser.Estructuras_controlContext):
        print("Inicio estructura control")
        self.tabla.addContexto()

    def exitEstructuras_control(self, ctx: compiladoresParser.Estructuras_controlContext):
        if not self.errores:
            self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.emitir_advertencias_contexto()  # Verificar antes de eliminar contexto
        self.tabla.delContexto()
        print("Fin estructura control")

    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        print("Inicio bloque")
        self.tabla.addContexto()

    def exitBloque(self, ctx: compiladoresParser.BloqueContext):
        if not self.errores:
            self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.emitir_advertencias_contexto()  # Verificar antes de eliminar contexto
        self.tabla.delContexto()
        print("Fin bloque")

    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        var_id = ctx.ID().getText()
        # Buscar primero en el contexto local
        var = self.tabla.buscarIDlocal(Variable(var_id, '', False, False))
        # Verificar si se trata de una declaración
        tipo_dato = None
        if ctx.parentCtx and hasattr(ctx.parentCtx, 'tipo_dato') and ctx.parentCtx.tipo_dato() is not None:
            tipo_dato = ctx.parentCtx.tipo_dato().getText()
            if var is None:
                # Si no está en el contexto local y se trata de una declaración, crear y agregar la variable
                var = Variable(var_id, tipo_dato, False, False)
                self.tabla.addID(var)
            else:
                # Si se encuentra en el contexto local y es una declaración, es un error de doble declaración
                self.registrar_error(f"Error semántico: Doble declaración de identificador '{var_id}' en el contexto actual")
                return
        else:
            # Si no es una declaración, buscar en el contexto local y luego en contextos superiores si no está presente
            if var is None:
                var = self.tabla.buscarID(Variable(var_id, '', False, False))
                if var is None:
                    # Si no se encuentra en ningún contexto, es un error de uso no declarado
                    self.registrar_error(f"Error semántico: Uso de identificador no declarado '{var_id}'")
                    return

        # Si la variable existe (ya sea en el contexto local o se ha encontrado en contextos superiores)
        if var:
            # Obtener el tipo de la variable existente
            tipo_var = var.tipo if var.tipo else tipo_dato

            # Determinar el tipo del valor que se asigna
            asignable = ctx.asignable()
            tipo_asignable = None

            if asignable is not None:
                if asignable.ENTERO() is not None:
                    tipo_asignable = 'int'
                elif asignable.DECIMAL() is not None:
                    tipo_asignable = 'double'
                elif asignable.ID() is not None:
                    # Buscar el tipo del identificador en la tabla de símbolos
                    var_asignable = self.tabla.buscarID(Variable(asignable.ID().getText(), '', False, False))
                    if var_asignable:
                        tipo_asignable = var_asignable.tipo
                    else:
                        self.registrar_error(f"Error semántico: Uso de identificador no declarado '{asignable.ID().getText()}'")
                        return
                else:
                    tipo_asignable = 'unknown'

                # Verificar compatibilidad de tipos solo si ambos tipos son conocidos
                if tipo_asignable is not None and tipo_var is not None:
                    if tipo_var == 'int' and tipo_asignable == 'double':
                        self.registrar_error(f"Error semántico: Asignación incompatible de 'double' a 'int' para la variable '{var_id}'")
                    elif tipo_var == 'double' and tipo_asignable == 'int':
                        self.registrar_advertencia(f"Advertencia: Asignación de 'int' a 'double' para la variable '{var_id}' puede perder precisión")

            # Marcar como inicializada si es una asignación
            if ctx.IGUAL() is not None or ctx.UMAS() is not None or ctx.UMENOS() is not None:
                var.inicializada = True
            self.tabla.addID(var)  # Actualiza la tabla

    def exitComp(self, ctx: compiladoresParser.CompContext):
        for asignable_ctx in ctx.asignable():
            if asignable_ctx.ID() is not None:
                var_id = asignable_ctx.ID().getText()
                var = self.tabla.buscarID(Variable(var_id, '', False, False))
                if var:
                    if not var.inicializada:
                        self.registrar_error(f"Error semántico: Uso de identificador no inicializado '{var_id}' en línea {ctx.start.line}")
                    var.usada = True
                    self.tabla.addID(var)  # Marcar como usada
                else:
                    self.registrar_error(f"Error semántico: Uso de identificador no declarado '{var_id}' en línea {ctx.start.line}")

    def exitFactor(self, ctx: compiladoresParser.FactorContext):
        if ctx.ID() is not None:
            var_id = ctx.ID().getText()
            var = self.tabla.buscarID(Variable(var_id, 'x', False, False))
            if var:
                if not var.inicializada:
                    self.registrar_error(f"Error semántico: Uso de identificador no inicializado '{var_id}'")
                var.usada = True 
                self.tabla.addID(var)
            else:
                self.registrar_error(f"Error semántico: Uso de identificador no declarado '{var_id}'")

    def exitAsignables(self, ctx: compiladoresParser.AsignablesContext):
        if ctx.asignable().ID() is not None:
            var_id = ctx.asignable().ID().getText()
            var = self.tabla.buscarID(Variable(var_id, '', False, False))
            if var:
                if not var.inicializada:
                    self.registrar_error(f"Error semántico: Uso de identificador no inicializado '{var_id}'")
                var.usada = True
                self.tabla.addID(var)
            else:
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
        if not self.errores:
            self.impresora.lectura(self.tabla.ts[-1], len(self.tabla.ts))
        self.emitir_advertencias_contexto()
        self.tabla.delContexto()
        print("Fin contexto de funcion")

    def exitLlamada_funcion(self, ctx: compiladoresParser.Llamada_funcionContext):
        fun_id = ctx.ID().getText()
        funcion = self.tabla.buscarID(Funcion(fun_id, '', True, False, []))
        if funcion:
            funcion.usada = True
            self.tabla.addID(funcion)
        else:
            self.registrar_error(f"Error semántico: Llamada a función no declarada '{fun_id}'")

    def emitir_advertencias_contexto(self):
        # Verificar variables no usadas o no inicializadas en el contexto actual
        for simbolo in self.tabla.ts[-1].values():
            if isinstance(simbolo, Variable):
                if not simbolo.usada:
                    self.registrar_advertencia(f"WARNING: La variable '{simbolo.nombre}' fue declarada pero no utilizada.")
                if not simbolo.inicializada:
                    self.registrar_advertencia(f"WARNING: La variable '{simbolo.nombre}' fue declarada pero no inicializada.")

del compiladoresParser
