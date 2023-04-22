import random


class Nodo:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.__tab = ""

    def insert(self, value: int):
        new_nodo = Nodo(value)

        if self.contains(value):
            print("Ese valor ya se encuentra dentro")
            return

        if self.root is None:
            self.root = new_nodo
        else:
            branch = self.root
            new_branch = None

            while True:
                new_branch = branch

                if value < branch.value:
                    branch = branch.left

                    if branch is None:
                        new_branch.left = new_nodo
                        return
                else:
                    branch = branch.right

                    if branch is None:
                        new_branch.right = new_nodo
                        return
    
    def contains(self, value: int):
        def search(node: Nodo):
            if node is None:
                return False
            elif node.value == value:
                return True
            elif search(node.right):
                return True
            elif search(node.left):
                return True
            return False
        return search(self.root)
    
    def min(self):
        branch = self.root
        while branch is not None:
            if branch.left:
                branch = branch.left
            else:
                return branch.value            
    
    def closesvalue(self,value):
        def searchNodes(node: Nodo, value: int):
            difL = difR = None
            if node.left is not None:
                value_left = searchNodes(node.left,value)
                difL = value_left - value
            if node.right is not None:
                value_right = searchNodes(node.right,value)
                difR = value_right - value

            difThis = node.value - value
    
            if difL is not None and difR is not None:
                if abs(difL) < abs(difThis):
                    return value_left
                elif abs(difR) < abs(difThis):
                    return value_right
                else:
                    return node.value
            elif difL is not None:
                if abs(difL) < abs(difThis):
                    return value_left
                else:
                    return node.value
            elif difR is not None:
                if abs(difR) < abs(difThis):
                    return value_right
                else:
                    return node.value
            else:
                return node.value
            
        if self.root:
            return searchNodes(self.root,value)
        else:
            print("No hay ningun nodo")
            

    def print_tree(self):
        def print_node(node: Nodo, level=0, position="Root"):
            if node is not None:
                print("|\t" * level + "|_" + position + ": " + str(node.value))
                print_node(node.right, level+1, "Right")
                print_node(node.left, level+1, "Left")
        print_node(self.root)


""" 
insert(value)           => Guarda el valor del parametro en el arbol.
contains(value)         => Verifica si el valor del parametro se encuentra dentro del arbol retornando true en caso de ser asi y false de lo contrario.
min()                   => Retorna el minimo valor del arbol binario.
closesvalue(value)      => Retorna el valor mas cercano al valor del parametro que se encuentre dentro del arbol.
print_tree()            => Imprime todos los valores del arbol binario indicando el nivel y el lado (derecha o izquierda).
""" 

tree = BinaryTree()
