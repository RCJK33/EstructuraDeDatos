class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def appendL(self,*args):
        inicio = 0
        if self.head is None:
            self.auxAppendL(args[0])
            inicio = 1
        for i in range(inicio,len(args)):
            self.auxAppendL(args[i])

    def prependL(self,value):
        if self.head is None:
            self.appendL(value)
            return
        else:
            nuevo_nodo = Nodo(value)
            nuevo_nodo.next = self.head
            self.head = nuevo_nodo
            self.length+=1

    def insertL(self,value,position):
        if self.length+1 == position:
            self.appendL(value)
            return
        if position == 0:
            self.prependL(value)
            return
        try:
            temp = self.auxPositioner(position-1)
            nuevoNodo = temp.next
            temp.next = Nodo(value)
            temp.next.next = nuevoNodo
            self.length+= 1
        except Exception as err:
            print(f"No existe el nodo:InsertL => {type(err)}")

    def popL(self):
        try:
            nodosIn = self.head
            while nodosIn.next.next:
                nodosIn = nodosIn.next
            nodosIn.next = None
            self.tail = nodosIn
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
                self.head = temp
            self.length+= -1 
        except Exception as err:
            print(f"No hay nodos:pop_firstL => {type(err)}")

    def removeL(self,position):
        if self.length-1 == position:
            self.popL()
            return
        if position == 0:
            self.pop_firstL()
            return
        temp = self.auxPositioner(position-1)
        try:
            replace = temp.next.next
            temp.next = None 
            temp.next = replace
            self.length+= -1
        except Exception as err:
            print(f"No existe el nodo:RemoveL => {type(err)}")

    def setL(self,value,position):
        try:
            self.auxPositioner(position).value = value
        except Exception as err:
            print(f"No existe el nodo:setL => {type(err)}")

    def getL(self,position):
        return self.auxPositioner(position).value

    def printL(self):
        if self.head is not None:
            nodosIn = self.head
            while nodosIn.next:
                print(nodosIn.value)
                nodosIn = nodosIn.next
            print(nodosIn.value)  
        else:
            print("No hay nodos:printL")

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
prependL(value)         => Añade el valor del parametro al principio de la lista.
insertL(value,position) => Añade el valor del parametro en la posicion ingresada en el segundo parametro.
popL()                  => Elimina el ultimo nodo la lista.
pop_firstL()            => Elimina el primer nodo de la lista.
removeL(position)       => Elimina el nodo de la posicion especificada de la lista.
setL(value,position)    => Modifica el valor del nodo en la posicion especidicada.
getL(position)          => Retorna el valor del nodo especificado.
printL()                => Imprime el valor de todos los elementos en la lista.
_auxAppendL()           => Metodo privado que añade valores a la lista.
_auxPositioner()        => Metodo privado que retorna un Nodo en especifico.
"""

    
my_linked_List = LinkedList() 
my_linked_List.appendL(1)
print(my_linked_List.length)
print(my_linked_List.head.value)
print(my_linked_List.tail.value)
