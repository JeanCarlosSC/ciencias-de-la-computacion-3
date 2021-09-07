# Identificador de tokens

Dadas las entradas de operaciones aritméticas en un archivo identificar los tokens valido y no validos de la entrada

__ejemplo de entrada en un archivo:__
<pre>
a = 25 + 3
b1 = 50 * 32
d = a - b1
z = 4 % -5
</pre>

__ejemplo de salida en un archivo:__ (tokens.out)
<pre>
id -> a
op -> =
num -> 25
op -> +
num -> 3
...
no_valido -> %
num -> -5
</pre>
