import re

# patrones
patronIdentificador = re.compile('([a-z][0-9\_]{0,})*');
patronNumerico=re.compile('(([-0-9])*([0-9])+)(\.[0-9]+){0,1}');
patronOperador=re.compile('[\-\*\+\/\=]');

# clasificacion
def identificar(token):
  if(esNumerico(token)):
      return "num -> " + token
  elif(esIdentificador(token)):
    return "id -> " + token
  elif(esOperador(token)):
      return "op -> " + token
  else:
    return "no_valido -> " + token

# validaciones
def esNumerico(token):
  if(patronNumerico.match(token)!=None):
    return patronNumerico.match(token).group()==token
  else:
    return False;

def esIdentificador(token):
  if(patronIdentificador.match(token)!=None):
    return patronIdentificador.match(token).group()==token;
  else:
    return False;

def esOperador(token):
  if(patronOperador.match(token)!=None):
    return patronOperador.match(token).group()==token;
  else:
    return False;

# carga datos
entrada = open("operaciones.in", "r")
texto = ""
for linea in entrada:
  texto += linea
tokens = texto.split()
entrada.close()

#procesa y almacena informacion
writer = open("tokens.out", "w")
primeraLinea = True
for token in tokens:
  if(primeraLinea):
    writer.write(str(identificar(token)))
    primeraLinea = False
  else:
    writer.write("\n" + str(identificar(token)))
writer.close()

# test
print("- - - identificadores - - -")
print(identificar("1c4"))
print(identificar("c14c"))
print(identificar("_c14"))
print(identificar("c_14"))
print(identificar("c"))
print(identificar("c__c"))
print(identificar("c_c"))
print("\n- - - numeros - - -")
print(identificar("15"))
print(identificar("15.3"))
print(identificar("-15"))
print(identificar("-5"))
print(identificar("-15.3"))
print(identificar("0"))
print(identificar("1"))
print(identificar("0.03"))
print(identificar("0..7"))
print(identificar("0.7.3"))
print(identificar("11."))
print(identificar(".3"))
print(identificar("-15"))
print("\n- - - operadores - - -")
print(identificar("r+"))
print(identificar("r-"))
print(identificar("-r"))
print(identificar("+"))
print(identificar("-"))
print(identificar("*+"))
print(identificar("/"))
print(identificar("%"))
print(identificar("*"))
print(identificar("="))
