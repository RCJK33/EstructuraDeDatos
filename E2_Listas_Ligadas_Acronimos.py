class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def sortedAppendL(self,chars):
        inicio = 0
        chars = sorted(str(chars).replace(" ","").upper())
        for i in range(inicio,len(chars)):
            self._auxAppendL(chars[i])
        
    def isAcronymL(self,otherself):
        if not isinstance(otherself,LinkedList):
            return False
        if self.length != otherself.length:
            return False
        
        nodosIn = self.head
        nodosInOther = otherself.head
        for i in range(self.length):
            if nodosIn.value == nodosInOther.value:
                nodosIn = nodosIn.next
                nodosInOther = nodosInOther.next
            else:
                return False
        return True

    def _auxAppendL(self, value):
        if self.head is None:
            self.head = Nodo(value)
            self.tail = self.head
        else:
            self.tail.next = Nodo(value)
            self.tail = self.tail.next
        self.length+=1

""" 
simpleAppendL(*value)   => Añade el valor del parameto o parametros a la lista de forma ordenada con funcion sorted() (funcion ya hecha).
isAcronymL(LinkedList)  => Recibe una instancia de la misma clase y retorna un valor voleano si ambas listas son iguales.
_auxAppendL()           => Metodo privado que añade valores a la lista.
"""

my_linked_List = [LinkedList(),LinkedList()]

for i in range(len(my_linked_List)):
    my_linked_List[i].sortedAppendL(input(f"Ingresa la palabra {i+1}: "))

if my_linked_List[0].isAcronymL(my_linked_List[1]):
    print("Son acronimos")
else:
    print("No son acronimos")   
