import datetime

class Animal():
    def __init__(self,name,typeD,edad) -> None:
        self.name = name
        self.typeD = typeD
        self.edad = edad


class Nodo:
    def __init__(self, animal :Animal):
        self.animal = animal
        self.date = datetime.datetime.now()
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.front = None
        self.back = None
        print()

    def enqueue(self, animal :Animal):
        if not isinstance(animal,Animal):
            return False
        if self.front is None:
            self.front = Nodo(animal)
            self.back = self.front
        else:
            self.back.next = Nodo(animal)
            self.back = self.back.next
        
    def dequeue(self):
        if self.front is None:
            return "Ya no hay amiguitos disponibles."
        
        animal = self.front.animal
        frontBackup = self.front.next  
        self.front.next = None
        self.front = frontBackup
        if self.front is None:
            self.back = None

        return animal
    
    
""" 
dequeue()               => Reterona el valor del primer nodo y elimina dicho nodo.
enqueue(animal)          => Añade el valor del paramtro al queue.
""" 

queue = Queue()

queue.enqueue(Animal("Rudo","Dog",6))

