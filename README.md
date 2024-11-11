Proyecto Desarrollo de Herramientas de Software.

Cambios principales con respecto a la versión de 2022:

- Algunas reglas extra en la gramática.
- Cambio en Printer.py para imprimir un solo archivo de texto con los contextos, ya que antes generaba un archivo para cada contexto.
- Se añadió un ErrorListener para mostrar por terminal los errores sintácticos.
- Se expandió la lógica en el Listener para mostrar mejor los errores semánticos.

Problemas conocidos:

- No agrega a la tabla de símbolos de manera correcta al haber multiples declaraciones de variable en una misma línea. 
    Ejemplo: int a, b; 
    b es tomada como variable no declarada, por lo que salta como error semántico.

- Optimizar reglas de la gramática:
    - Si agrego un ; de más en algunos casos es tomado como válido en el árbol sintáctico, pero no debería ser correcto.
    - Agregar algunos paréntesis opcionales en casos como opal.

- Problemas con el contexto local en algunos casos.

- No reconoce si una variable de una funcion ha sido usada o no.

