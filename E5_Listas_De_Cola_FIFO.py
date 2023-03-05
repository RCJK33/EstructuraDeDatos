class Nodo:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.back = None
    
    def enqueue(self, value):
        if self.front is None:
            self.front = Nodo(value)
            self.back = self.front
        else:
            self.back.next = Nodo(value)
            self.back = self.back.next
        
    def dequeue(self):
        if self.front is None:
            return "Queue vacio"
        value = self.front.value
        frontBackup = self.front.next  
        self.front.next = None
        self.front = frontBackup
        if self.front is None:
            self.back = None
        return value
    
""" 
dequeue()               => Reterona el valor del primer nodo y elimina dicho nodo.
enqueue(value)          => Añade el valor del paramtro al queue.
""" 

queue = Queue()