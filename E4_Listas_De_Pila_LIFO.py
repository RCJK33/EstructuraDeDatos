class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkeList:
    def __init__(self) -> None:
        self.top = None
        self.height = 0

    def push(self,value):
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

listas = LinkeList()

listas.push(3)
listas.push(4)
listas.push(6)
listas.push(7)

listas.popL()

listas.printStack()