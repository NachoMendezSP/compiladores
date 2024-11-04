import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from compiladoresLexer import compiladoresLexer
from compiladoresParser import compiladoresParser
from MyListener import MyListener

# Listener personalizado para capturar errores de sintaxis
class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.hay_error = False
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.hay_error = True
        error_msg = f"Error de sintaxis en línea {line}, columna {column}: {msg}"
        self.errores.append(error_msg)
        print(error_msg)

def main(argv):
    archivo = "input/entrada.txt"
    if len(argv) > 1:
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)

    # Configuro el listener de errores de sintaxis y ejecuta el parser
    syntax_error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_error_listener)

    parser.programa()

    # Si hubo errores de sintaxis, detengo el análisis y muestro el reporte
    if syntax_error_listener.hay_error:
        print("Análisis detenido debido a errores de sintaxis.")
        return

    # Si no hubo errores de sintaxis, realizar el análisis semántico con MyListener
    parser.reset()
    tree = parser.programa()
    miListener = MyListener()
    ParseTreeWalker().walk(miListener, tree)

    if miListener.errores:
        print("Errores semánticos detectados:")
        for error in miListener.errores:
            print(error)
    else:
        print("Análisis completado exitosamente. Tabla de símbolos generada.")

if __name__ == '__main__':
    main(sys.argv)
