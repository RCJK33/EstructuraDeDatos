class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self) -> None:
        self.top = None
        self.height = 0

    def pushL(self,value):
        if not self.top:
            self.top = Nodo(value)
        else:
            newNodo = Nodo(value)
            newNodo.next = self.top
            self.top = newNodo
        self.height += 1
    
    def popL(self):
        try:
            nodoBackup = self.top.next
            self.top.next = None
            self.top = None
            self.top = nodoBackup
            self.height += -1
        except:
            print("No existen nodos")

    def printStack(self):
        nodo = self.top
        while nodo:
            print(nodo.value)
            nodo = nodo.next

""" 
pushL(value)            => Guarda el valor del parametro en un nodo nuevo del stack.
popL()                  => Elimina el ultimo nodo guardado en el stack.
printStack()            => Imprime el valor de los nodos guardados en el Stack.
"""        

listas = Stack()
