class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def appendL(self,chars):
        inicio = 0
        chars = str(chars).upper().replace(" ","")
        for i in range(inicio,len(chars)):
            self._auxAppendL(chars[i])
    
    def simpleAppendL(self,chars):
        inicio = 0
        chars = sorted(str(chars).upper().replace(" ",""))
        for i in range(inicio,len(chars)):
            self._auxAppendL(chars[i])

    def printL(self):
        if self.head is not None:
            nodosIn = self.head
            while nodosIn.next:
                print(nodosIn.value)
                nodosIn = nodosIn.next
            print(nodosIn.value)  
        else:
            print("No hay nodos:printL")
        
    def isAcronymL(self,otherself):
        if isinstance(otherself,LinkedList):
            nodosIn = self.head
            nodosInOther = otherself.head
            if self.length == otherself.length:
                """ si se requiere hacer el sort aqui """
                for i in range(self.length):
                    evaluador = nodosIn.value == nodosInOther.value
                    if evaluador:
                        nodosIn = nodosIn.next
                        nodosInOther = nodosInOther.next
                    else:
                        return False
                return True
        return False

    """ def sortL(self):
        nodoIn = self.head
        pivote = nodoIn.value
        i=0
        ifor = 1
        while nodoIn.next:
            if pivote > nodoIn.next.value:
                self._flip(i,ifor) """

    def _flip(self,position_1,position_2):
        tempA = self._auxPositioner(position_1)
        tempB = self._auxPositioner(position_2)
        tempA.value, tempB.value = tempB.value, tempA.value

    def _auxAppendL(self, value):
        if self.head is None:
            self.head = Nodo(value)
            self.tail = self.head
        else:
            self.tail.next = Nodo(value)
            self.tail = self.tail.next
        self.length+=1

    def _auxPositioner(self,position):
        if self.head is not None and position < self.length:
            nodosIn = self.head
            for i in range(position):
                nodosIn = nodosIn.next
            return nodosIn


""" 
appendL(*value)         => Añade el valor del parameto o parametros a la lista.
simpleAppendL(*value)   => Añade el valor del parameto o parametros a la lista de forma ordenada con funcion sorted() (funcion ya hecha).
printL()                => Imprime el valor de todos los elementos en la lista.
isAcronymL(LinkedList)   => Recibe una instancia de la misma clase y retorna un valor voleano si ambas listas son iguales.
[Metodo sort() en proceso]
_flip(position,position)=> Metodo privado que intercambia los valores de los nodos de las posiciones especificas
_auxAppendL()           => Metodo privado que añade valores a la lista.
_auxPositioner()        => Metodo privado que retorna un Nodo en especifico.
"""

my_linked_List = [LinkedList(),LinkedList()]

for i in range(len(my_linked_List)):
    my_linked_List[i].simpleAppendL(str(input(f"Ingresa la palabra {i+1}: ")))

if my_linked_List[0].isAcronymL(my_linked_List[1]):
    print("Son acronimos")
else:
    print("No son acronimos")