# Generated from src/main/python/compiladores.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,38,241,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,2,1,3,4,3,91,8,3,11,3,12,3,
        92,1,4,4,4,96,8,4,11,4,12,4,97,1,4,1,4,4,4,102,8,4,11,4,12,4,103,
        1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,
        11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,
        18,1,18,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,22,1,
        22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,25,1,25,1,
        25,1,26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,29,1,29,1,29,1,
        29,1,29,1,29,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,
        36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,38,1,38,1,
        38,1,38,1,38,1,39,1,39,3,39,230,8,39,1,39,1,39,1,39,3,39,235,8,39,
        5,39,237,8,39,10,39,12,39,240,9,39,0,0,40,1,0,3,0,5,1,7,2,9,3,11,
        4,13,5,15,6,17,7,19,8,21,9,23,10,25,11,27,12,29,13,31,14,33,15,35,
        16,37,17,39,18,41,19,43,20,45,21,47,22,49,23,51,24,53,25,55,26,57,
        27,59,28,61,29,63,30,65,31,67,32,69,33,71,34,73,35,75,36,77,37,79,
        38,1,0,3,2,0,65,90,97,122,1,0,48,57,3,0,9,10,13,13,32,32,245,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,
        0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,
        0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,
        0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,
        0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,
        0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,
        0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,1,81,1,0,0,0,3,83,1,0,0,0,5,85,1,
        0,0,0,7,90,1,0,0,0,9,95,1,0,0,0,11,105,1,0,0,0,13,109,1,0,0,0,15,
        111,1,0,0,0,17,113,1,0,0,0,19,115,1,0,0,0,21,117,1,0,0,0,23,119,
        1,0,0,0,25,121,1,0,0,0,27,123,1,0,0,0,29,125,1,0,0,0,31,127,1,0,
        0,0,33,129,1,0,0,0,35,131,1,0,0,0,37,133,1,0,0,0,39,135,1,0,0,0,
        41,137,1,0,0,0,43,140,1,0,0,0,45,143,1,0,0,0,47,148,1,0,0,0,49,154,
        1,0,0,0,51,157,1,0,0,0,53,160,1,0,0,0,55,163,1,0,0,0,57,166,1,0,
        0,0,59,169,1,0,0,0,61,175,1,0,0,0,63,179,1,0,0,0,65,186,1,0,0,0,
        67,193,1,0,0,0,69,201,1,0,0,0,71,206,1,0,0,0,73,210,1,0,0,0,75,217,
        1,0,0,0,77,222,1,0,0,0,79,229,1,0,0,0,81,82,7,0,0,0,82,2,1,0,0,0,
        83,84,7,1,0,0,84,4,1,0,0,0,85,86,7,2,0,0,86,87,1,0,0,0,87,88,6,2,
        0,0,88,6,1,0,0,0,89,91,3,3,1,0,90,89,1,0,0,0,91,92,1,0,0,0,92,90,
        1,0,0,0,92,93,1,0,0,0,93,8,1,0,0,0,94,96,3,3,1,0,95,94,1,0,0,0,96,
        97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,101,5,46,
        0,0,100,102,3,3,1,0,101,100,1,0,0,0,102,103,1,0,0,0,103,101,1,0,
        0,0,103,104,1,0,0,0,104,10,1,0,0,0,105,106,5,39,0,0,106,107,3,1,
        0,0,107,108,5,39,0,0,108,12,1,0,0,0,109,110,5,59,0,0,110,14,1,0,
        0,0,111,112,5,44,0,0,112,16,1,0,0,0,113,114,5,123,0,0,114,18,1,0,
        0,0,115,116,5,125,0,0,116,20,1,0,0,0,117,118,5,40,0,0,118,22,1,0,
        0,0,119,120,5,41,0,0,120,24,1,0,0,0,121,122,5,61,0,0,122,26,1,0,
        0,0,123,124,5,60,0,0,124,28,1,0,0,0,125,126,5,62,0,0,126,30,1,0,
        0,0,127,128,5,43,0,0,128,32,1,0,0,0,129,130,5,45,0,0,130,34,1,0,
        0,0,131,132,5,42,0,0,132,36,1,0,0,0,133,134,5,47,0,0,134,38,1,0,
        0,0,135,136,5,37,0,0,136,40,1,0,0,0,137,138,5,43,0,0,138,139,5,43,
        0,0,139,42,1,0,0,0,140,141,5,45,0,0,141,142,5,45,0,0,142,44,1,0,
        0,0,143,144,5,116,0,0,144,145,5,114,0,0,145,146,5,117,0,0,146,147,
        5,101,0,0,147,46,1,0,0,0,148,149,5,102,0,0,149,150,5,97,0,0,150,
        151,5,108,0,0,151,152,5,115,0,0,152,153,5,101,0,0,153,48,1,0,0,0,
        154,155,5,38,0,0,155,156,5,38,0,0,156,50,1,0,0,0,157,158,5,124,0,
        0,158,159,5,124,0,0,159,52,1,0,0,0,160,161,5,61,0,0,161,162,5,61,
        0,0,162,54,1,0,0,0,163,164,5,33,0,0,164,165,5,61,0,0,165,56,1,0,
        0,0,166,167,5,105,0,0,167,168,5,102,0,0,168,58,1,0,0,0,169,170,5,
        119,0,0,170,171,5,104,0,0,171,172,5,105,0,0,172,173,5,108,0,0,173,
        174,5,101,0,0,174,60,1,0,0,0,175,176,5,102,0,0,176,177,5,111,0,0,
        177,178,5,114,0,0,178,62,1,0,0,0,179,180,5,114,0,0,180,181,5,101,
        0,0,181,182,5,116,0,0,182,183,5,117,0,0,183,184,5,114,0,0,184,185,
        5,110,0,0,185,64,1,0,0,0,186,187,5,112,0,0,187,188,5,117,0,0,188,
        189,5,98,0,0,189,190,5,108,0,0,190,191,5,105,0,0,191,192,5,99,0,
        0,192,66,1,0,0,0,193,194,5,112,0,0,194,195,5,114,0,0,195,196,5,105,
        0,0,196,197,5,118,0,0,197,198,5,97,0,0,198,199,5,116,0,0,199,200,
        5,101,0,0,200,68,1,0,0,0,201,202,5,118,0,0,202,203,5,111,0,0,203,
        204,5,105,0,0,204,205,5,100,0,0,205,70,1,0,0,0,206,207,5,105,0,0,
        207,208,5,110,0,0,208,209,5,116,0,0,209,72,1,0,0,0,210,211,5,100,
        0,0,211,212,5,111,0,0,212,213,5,117,0,0,213,214,5,98,0,0,214,215,
        5,108,0,0,215,216,5,101,0,0,216,74,1,0,0,0,217,218,5,99,0,0,218,
        219,5,104,0,0,219,220,5,97,0,0,220,221,5,114,0,0,221,76,1,0,0,0,
        222,223,5,98,0,0,223,224,5,111,0,0,224,225,5,111,0,0,225,226,5,108,
        0,0,226,78,1,0,0,0,227,230,3,1,0,0,228,230,5,95,0,0,229,227,1,0,
        0,0,229,228,1,0,0,0,230,238,1,0,0,0,231,235,3,1,0,0,232,235,3,3,
        1,0,233,235,5,95,0,0,234,231,1,0,0,0,234,232,1,0,0,0,234,233,1,0,
        0,0,235,237,1,0,0,0,236,234,1,0,0,0,237,240,1,0,0,0,238,236,1,0,
        0,0,238,239,1,0,0,0,239,80,1,0,0,0,240,238,1,0,0,0,7,0,92,97,103,
        229,234,238,1,6,0,0
    ]

class compiladoresLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    ENTERO = 2
    DECIMAL = 3
    CHARACTER = 4
    PYC = 5
    COMA = 6
    LA = 7
    LC = 8
    PA = 9
    PC = 10
    IGUAL = 11
    MENOR = 12
    MAYOR = 13
    MAS = 14
    MENOS = 15
    MUL = 16
    DIV = 17
    MOD = 18
    UMAS = 19
    UMENOS = 20
    TRUE = 21
    FALSE = 22
    AND = 23
    OR = 24
    EQUI = 25
    DIST = 26
    IF = 27
    WHILE = 28
    FOR = 29
    RETURN = 30
    PUBLIC = 31
    PRIVATE = 32
    VOID = 33
    INT = 34
    DOUBLE = 35
    CHAR = 36
    BOOL = 37
    ID = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "','", "'{'", "'}'", "'('", "')'", "'='", "'<'", "'>'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'++'", "'--'", "'true'", 
            "'false'", "'&&'", "'||'", "'=='", "'!='", "'if'", "'while'", 
            "'for'", "'return'", "'public'", "'private'", "'void'", "'int'", 
            "'double'", "'char'", "'bool'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ENTERO", "DECIMAL", "CHARACTER", "PYC", "COMA", "LA", 
            "LC", "PA", "PC", "IGUAL", "MENOR", "MAYOR", "MAS", "MENOS", 
            "MUL", "DIV", "MOD", "UMAS", "UMENOS", "TRUE", "FALSE", "AND", 
            "OR", "EQUI", "DIST", "IF", "WHILE", "FOR", "RETURN", "PUBLIC", 
            "PRIVATE", "VOID", "INT", "DOUBLE", "CHAR", "BOOL", "ID" ]

    ruleNames = [ "LETRA", "DIGITO", "WS", "ENTERO", "DECIMAL", "CHARACTER", 
                  "PYC", "COMA", "LA", "LC", "PA", "PC", "IGUAL", "MENOR", 
                  "MAYOR", "MAS", "MENOS", "MUL", "DIV", "MOD", "UMAS", 
                  "UMENOS", "TRUE", "FALSE", "AND", "OR", "EQUI", "DIST", 
                  "IF", "WHILE", "FOR", "RETURN", "PUBLIC", "PRIVATE", "VOID", 
                  "INT", "DOUBLE", "CHAR", "BOOL", "ID" ]

    grammarFileName = "compiladores.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


