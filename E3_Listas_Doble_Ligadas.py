class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prer = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def appendL(self,*args):
        for i in range(len(args)):
            self._auxAppendL(args[i])

    def prependL(self,value):
        if self.head is None:
            self.appendL(value)
            return
        else:
            nuevo_nodo = Nodo(value)
            self.head.prer = nuevo_nodo
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
            self.length+=1

    def popL(self):
        try:
            self.tail = self.tail.prer
            self.tail.next.prer = None
            self.tail.next = None
            self.length+= -1
        except:
            self.head = None
            self.tail = None
            self.length = 0
    
    def pop_firstL(self):
        try:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head.next
                self.head = None
                temp.prer = None
                self.head = temp
            self.length+= -1 
        except Exception as err:
            print(f"No hay nodos:pop_firstL => {type(err)}")

    def insertL(self,value,position):
        if self.length+1 == position:
            self.appendL(value)
            return
        if position == 0:
            self.prependL(value)
            return
        try:
            temp = self._auxPositioner(position-1)
            nuevoNodo = temp.next
            temp.next = Nodo(value)
            temp.next.prer = temp
            temp.next.next = nuevoNodo
            temp.next.next.prer = temp.next
            self.length+= 1
        except Exception as err:
            print(f"No existe el nodo:InsertL => {type(err)}")

    def removeL(self,position):
        if self.length-1 == position:
            self.popL()
            return
        if position == 0:
            self.pop_firstL()
            return
        temp = self._auxPositioner(position-1)
        try:
            replace = temp.next.next
            temp.next = None
            replace.prer = temp 
            temp.next = replace
            self.length+= -1
        except Exception as err:
            print(f"No existe el nodo:RemoveL => {type(err)}")

    def setL(self,value,position):
        try:
            self._auxPositioner(position).value = value
        except Exception as err:
            print(f"No existe el nodo:setL => {type(err)}")

    def getL(self,position):
        return self._auxPositioner(position).value

    def printL(self):
        if self.head is not None:
            nodosIn = self.head
            while nodosIn.next:
                print(nodosIn.value)
                nodosIn = nodosIn.next
            print(nodosIn.value)  
        else:
            print("No hay nodos:printL")

    def printTailBackL(self):
        if self.tail is not None:
            nodosIn = self.tail
            while nodosIn.prer:
                print(nodosIn.value)
                nodosIn = nodosIn.prer
            print(nodosIn.value)  
        else:
            print("No hay nodos:printL")

    def _auxAppendL(self, value):
        if self.head is None:
            self.head = Nodo(value)
            self.tail = self.head
        else:
            self.tail.next = Nodo(value)
            self.tail.next.prer = self.tail
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
prepend(value)          => Añade el valor del parametro al principio de la lista.
insertL(value,position) => Añade el valor del parametro en la posicion ingresada en el segundo parametro.
popL()                  => Elimina el ultimo nodo la lista.
pop_firstL()            => Elimina el primer nodo de la lista.
removeL(position)       => Elimina el nodo de la posicion especificada de la lista.
setL(value,position)    => Modifica el valor del nodo en la posicion especidicada.
getL(position)          => Retorna el valor del nodo especificado.
printL()                => Imprime el valor de todos los elementos en la lista.
printTailBackL()        => Imprime el valor de todos los elementos de la lista de manera inversa.
_auxAppendL()           => Metodo privado que añade valores a la lista.
_auxPositioner()        => Metodo privado que retorna un Nodo en especifico.
"""

my_linked_List = LinkedList()

my_linked_List.appendL(1,2,3,4,5,6,7)
my_linked_List.insertL(3,3)
my_linked_List.removeL(3)
my_linked_List.printL()
my_linked_List.printTailBackL()