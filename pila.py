class Pila:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def add(self, item):
         self.items.append(item)

     def removeFirst(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

pila = Pila()
pila.add(15)
pila.add(16)
print(pila.items, pila.size())
