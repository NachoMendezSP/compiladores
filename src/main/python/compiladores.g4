grammar compiladores;

fragment LETRA: [a-zA-Z];
fragment DIGITO: [0-9];

WS: [ \t\n\r] -> skip;

ENTERO: DIGITO+;

PYC: ';';
COMA: ',';
LA: '{';
LC: '}';
PA: '(';
PC: ')';
IGUAL: '=';
MENOR: '<';
MAYOR: '>';
MAS: '+';
MENOS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
UMAS: '++';
UMENOS: '--';

TRUE: 'true';
FALSE: 'false';
AND: '&&';
OR: '||';
EQUI: '==';
DIST: '!=';

IF: 'if';
WHILE: 'while';
FOR: 'for';

RETURN: 'return';
PUBLIC: 'public';
PRIVATE: 'private';
VOID: 'void';

INT: 'int';
DOUBLE: 'double';
CHAR: 'char';
BOOL: 'bool';
tipo_dato: INT | DOUBLE | CHAR | BOOL;

ID: (LETRA | '_') ((LETRA | DIGITO | '_'))*;

/* INICIO */

programa: lineas;

lineas: instruccion lineas | | EOF;

instruccion: 
	estructuras_control 
	| funcion 
	| variable PYC 
	| bloque;

estructuras_control:
	estructuras (
		estructuras_control
		| funcion
		| variable PYC
		| bloque_alt
	);

/* Distintos bloques para controlar mejor con 
redundancia los contextos en el listener */

bloque: LA lineas LC;
bloque_alt: LA lineas LC;

estructuras: iwhile | iif | ifor;

asignable:
	ID
	| ENTERO
	| booleanos
	| expresion
	| llamada_funcion;

variable: declaracion | asignacion;

declaracion: tipo_dato asignacion;

asignacion:
	ID (MAS | MENOS) IGUAL asignable asignaciones
	| ID IGUAL asignable asignaciones
	| ID (UMAS | UMENOS) asignaciones
	| ID asignaciones;

asignaciones: | COMA asignacion | IGUAL asignacion |;

igualacion: EQUI | DIST;

relacion:
	igualacion
	| MAYOR
	| MENOR
	| (MAYOR IGUAL)
	| (MENOR IGUAL)
	| AND
	| OR;

comparacion: asignable relacion asignable;

booleanos: TRUE | FALSE;

/* Jerarquía aritmética */
expresion:
	expresion igualacion termino
	| expresion MAS termino
	| expresion MENOS termino
	| expresion AND termino
	| expresion OR termino
	| termino;
termino:
	termino MUL factor
	| termino DIV factor
	| termino MOD factor
	| factor;
factor: PA expresion PC | ID | ENTERO | booleanos;

/* Estructuras de control */
/* if */
iif:
	IF PA comparacion PC
	| IF PA booleanos PC
	| IF PA ID PC
	| IF PA ENTERO PC;
/* while */
iwhile:
	WHILE PA comparacion PC
	| WHILE PA ENTERO PC
	| WHILE PA ID PC
	| WHILE PA booleanos PC;

/* for */
ifor:
	FOR PA (variable |) PYC (comparacion | booleanos |) PYC (asignacion	|) PC;

/* Funciones */

funcion:
	declaracion_funcion
	| prototipo_funcion
	| llamada_funcion;

bloque_funcion: 
	LA lineas LC
	| LA lineas retorno LC;

tipo_retorno: VOID | tipo_dato;
acceso: PUBLIC | PRIVATE;
parametro: tipo_dato ID | tipo_dato;
parametros: parametro COMA parametros | parametro;
asignables: asignable COMA asignables | asignable;

/* Dos firmas distintas, ya que el listener solo creara contexto 
con la firma de funcion, no de prototipos */

firma: (acceso |) tipo_retorno ID PA (parametros)* PC;
firma_prototipo: (acceso |) tipo_retorno ID PA (parametros)* PC;

prototipo_funcion: firma_prototipo PYC;

declaracion_funcion: firma bloque_funcion;

llamada_funcion: ID PA (asignables)* PC;

retorno: RETURN asignable PYC | RETURN PYC;
