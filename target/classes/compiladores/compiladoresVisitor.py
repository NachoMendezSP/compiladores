# Generated from /home/nacho/Downloads/compiladores-main/src/main/java/compiladores/compiladores.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .compiladoresParser import compiladoresParser
else:
    from compiladoresParser import compiladoresParser

package compiladores;


# This class defines a complete generic visitor for a parse tree produced by compiladoresParser.

class compiladoresVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by compiladoresParser#s.
    def visitS(self, ctx:compiladoresParser.SContext):
        return self.visitChildren(ctx)



del compiladoresParser