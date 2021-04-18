class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y verificar si está vacía. """
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items = []

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción. """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def en_orden(arbol):
    if arbol == None:
        return ''
    elif arbol.valor in ['+', '-', '*', '/']:
        return "(" + en_orden(arbol.izquierda) + str(arbol.valor) + en_orden(
            arbol.derecha) + ")"
    else:
        return str(arbol.valor)

def evaluar(arbol):
    if arbol == None:
        pass
    else:
        if arbol.valor == '+':
            return evaluar(arbol.izquierda) + evaluar(arbol.derecha)
        if arbol.valor == '-':
            return evaluar(arbol.izquierda) - evaluar(arbol.derecha)
        if arbol.valor == '*':
            return evaluar(arbol.izquierda) * evaluar(arbol.derecha)
        if arbol.valor == '/':
            return evaluar(arbol.izquierda) // evaluar(arbol.derecha)
        return int(arbol.valor)

# Guardamos cada línea en la pila
f = open("operaciones.txt", "r")
pila = Pila()
for linea in f:
  pila.apilar(linea[:-1])
f.close()

# por cada linea se convierte a un árbol y se muestra la información procesada
while (not pila.es_vacia()):
    linea = pila.desapilar()
    inicio = 0
    valores = Pila()
    for i in range(len(linea)):
        valor = ""
        # Tokeniza en nodos
        if linea[i] == " ":
          valor = linea[inicio:i]
          valores.apilar(Nodo(valor))
          inicio = i + 1
        elif i == len(linea) - 1:
          valor = linea[inicio:i + 1]
          valores.apilar(Nodo(valor))
        # Organiza los nodos
        if (valor in ['+', '-', '*', '/']):
          operador=valores.desapilar().valor  # Desapilar símbolo
          b = valores.desapilar() # Desapila valor b
          a = valores.desapilar() # Desapila valor a
          nodo = Nodo(operador, a, b) # Guarda todo en un nodo
          valores.apilar(nodo) # Apila el nodo resultante
    # Muestra el ultimo valor resultante
    arbol = valores.desapilar()
    print("Nueva línea de operaciones:")
    print(linea+" = "+str(en_orden(arbol))+" = "+str(evaluar(arbol)))