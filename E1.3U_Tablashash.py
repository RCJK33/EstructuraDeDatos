import math

""" Para la materia de Estructura de datos 
    Version: TH-R2-1
    (Nombre - Numero de Rama - version)
"""

class HashElment:
    # Estructura del elemento que se almacenara en la tabla hash
    def __init__(self,key: str, object = None) -> None:
        self.key = key # key del objeto
        self.object = object # Objeto que se alamacena


class HashTable:
    """def __init__(self,length: int = 29,magic_number: int = 7,rehash_Limit: int = 6) -> None: """
    def __init__(self,length: int = 29,magic_number: int = 7,rehash_Limit: int = 6) -> None:
        # Se recomienda utilizar numeros primos para el length de la lista
        # Se recomienda dejar el numero magico en 7, 2 o 1 (puedes probar a ver cual da menos coluciones)
        #   de preferencia un numero primo relativo del length de la lista
        self.__hashList = list([] for i in range(length))
        self.__lengthTable = length        # Tamaño de la tabla
        """ self.__rehashLimit = rehash_Limit       # Limite de intentos de rehash """

        # Numero magico, se utiliza para dar un cambio a la ecuacion Hash si se ncesita
        self.__magicNumber = magic_number
        self.length = 0     # Cantidad de elementos introduciodos

    def __hash__(self,key: str) -> int:
        # Metodo para calcular el hash (No hace rehash)
        hs = 0
        index = 1
        keyLength = len(key)
        
        for i in range(keyLength):
            # Formula Hash [Funcion lineal con los parametros 
            # i++ (ascii de Char) + numero Maico]
            # Funcion que depende del numero de iteracion lo que significa que si hay otra letra igual, la funcion no sera igual.
            hs += (i+1) * (ord(key[i])) + self.__magicNumber
        index = hs % self.__lengthTable
        return index

    """ def __hash__(self,key: str) -> int:
        # Metodo inspirado en el metodo de Direccionamiento abierto o Hasing Cerrado (Rehash)
        # Mas info en https://ccia.ugr.es/~jfv/ed1/tedi/cdrom/docs/tablash.html
        # ## NO UTILIZAR, METODO NO COMPATIBLE CON ESTA VERSION
        def rehash(keyLength: int, intents: int = 1):
            hash = 0
            for it in range(keyLength):
                # Formula Hash [Funcion lineal con los parametros 
                #   i++ (ascii de Char) + no. de intentos]
                # Funcion que depende del numero de iteracion lo que significa que si hay otra letra igual, la funcion no sera igual.

                hash += (it + 1) * (ord(key[it])) + intents

                # Nota: una variacion importante, es hacer que el ciclo vaya de 2 en 2 caracteres (sumar ambos o multiplicarlos)
            return int(hash)
        
        ints = 0
        while True:
            index = rehash(len(key), (ints + self.__magicNumber)) % self.__lengthTable

            if self.containsKey(index):
                print("{:<15}{:<10}{:<2}".format(key, index, ints+1))
                return index
            elif ints < self.__rehashLimit:
                ints += 1
            else:
                print(f"Hash no disponible  -> {key} | [{ints} intentos].")
                break """
    
    def __retunSubIndexByKey(self, key: str) -> int:
        index = self.__hash__(key)
        for i in range(len(self.__hashList[index])):
            obj: HashElment = self.__hashList[index][i]
            if obj.key == key:
                return i
        return None
    
    def containsKey(self, key: str) -> bool:
        if self.__retunSubIndexByKey(key) is not None:
            return True
        return False
    
    
    def add(self, key: str, object = None) -> None:
        if not self.containsKey(key):
            index = self.__hash__(key)
            obj = HashElment(key, object)
            self.__hashList[index].append(obj)
            self.length += 1
    
    def put(self, key: str, object = None) -> None:
        index = self.__hash__(key)
        obj = HashElment(key, object)
        if not self.containsKey(key):
            self.__hashList[index].append(obj)
            self.length += 1
        else:
            subIndex = self.__retunSubIndexByKey(key)
            self.__hashList[index][subIndex] = obj

    def get(self, key: str) -> HashElment:
        contains = self.containsKey(key)
        if not contains:
            return None
        index = self.__hash__(key)
        subIndex = self.__retunSubIndexByKey(key)
        obj: HashElment = self.__hashList[index][subIndex]
        return obj
    
    def remove(self, key: str):
        try:
            index = self.__hash__(key)
            subIndex = self.__retunSubIndexByKey(key)
            self.__hashList[index].pop(subIndex)
        except:
            pass

    def printTableHash(self):
        print("|{:<5} | {:<10}| {:<10}|".format('Index','key','O'))
        for i in range(self.__lengthTable):
            array = self.__hashList[i]
            print(f"|{i}")
            for i2 in range(len(array)):
                obj: HashElment = self.__hashList[i][i2]
                print(" --|{:<5} | {:<13}| {:<10}|".format(i2,obj.key,str(None)))


hash_list = HashTable(23)

""" hash_list.add("Mario")
hash_list.add("Mauricio")
hash_list.add("Fernanda")
hash_list.add("Noemi")
hash_list.add("Gael")
hash_list.add("Luis")
hash_list.add("Villegas")
hash_list.add("Carlos")
hash_list.add("Elisa") 
hash_list.add("Hoper")
hash_list.add("Karina")

hash_list.add("aniraK")
hash_list.add("repoH")
hash_list.add("asilE")
hash_list.add("solraC")
hash_list.add("sagelliV")
hash_list.add("siuL")
hash_list.add("leaG")
hash_list.add("imeoN")
hash_list.add("adnanreF")
hash_list.add("oiciruaM")
hash_list.add("oiraM") """
