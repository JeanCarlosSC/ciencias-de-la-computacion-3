# pila
class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)

# operaciones solicitadas
def suma(pila):
  suma = pila.extraer() + pila.extraer()
  pila.incluir(suma)

def resta(pila):
  suma = pila.extraer() - pila.extraer()
  pila.incluir(suma)

def producto(pila):
  suma = pila.extraer() * pila.extraer()
  pila.incluir(suma)

def division(pila):
  suma = pila.extraer() / pila.extraer()
  pila.incluir(suma)

# entrada de datos
cadena = input()
pila = Pila()
for x in cadena.split(" "):
  pila.incluir(int(x))
operacion = input()
iteraciones = int(input())

# validacion
if(iteraciones > pila.tamano()):
  iteraciones = pila.tamano()

# calculo
for i in range(iteraciones-1):
  if(operacion == "suma"):
    suma(pila)
  elif(operacion == "resta"):
    resta(pila)
  elif(operacion == "producto"):
    producto(pila)
  elif(operacion == "division"):
    division(pila)

# resultado
print(pila.extraer())