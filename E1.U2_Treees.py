class Nodo:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.__tab = ""

    def insert(self, value):
        new_nodo = Nodo(value)

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
    
    def contains(self, value):
        def search(node=Nodo):
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

    def print_tree(self):
        def print_node(node=Nodo, level=0, position="Root"):
            if node is not None:
                print("|\t" * level + "|_" + position + ": " + str(node.value))
                print_node(node.right, level+1, "Right")
                print_node(node.left, level+1, "Left")
        print_node(self.root)


tree = BinaryTree()
