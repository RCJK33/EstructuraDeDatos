import math


class HashTable:
    def __init__(self,length: int = 101,magic_number: int = 2) -> None:
        # Se recomienda utilizar numeros primos para el tamaño de la lista
        # Se recomienda dejar el numero magico en 2 o 1 (puedes probar a ver cual da menos coluciones)
        self.__hashList = list(None for i in range(length))
        self.__length = length
        self.__magicNumber = magic_number
        self.length = 0

    # Esta version del metodo no hacer Rehash
    """ def __hash__(self,key: str) -> int:
        hs = 0
        index = 1
        keyLength = len(key)
        
        for i in range(keyLength):
            # Formula Hash [Funcion lineal con los parametros 
            # i++ (ascii de Char) + (2 (o 1) + ascii char)]
            # Funcion que depende del numero de iteracion lo que significa que si hay otra letra igual, la funcion no sera igual.
            hs += i * (ord(key[i])) + 2 + ord(key[(keyLength-1)-i])
        index = hs % self.__length

        print("{:<15}{:<3}{:<15}{:<2}".format(key,index,str(self.__hashList[index]),1))
        return index """

    # Metodo basado en el metodo de Direccionamiento abierto o Hasing Cerrado (Rehash)
    # Mas info en https://ccia.ugr.es/~jfv/ed1/tedi/cdrom/docs/tablash.html
    def __hash__(self,key: str) -> int:
        def rehash(keyLength: int,intents: int = 1):
            hash = 0
            for it in range(keyLength):
                # Formula Hash [Funcion lineal con los parametros 
                # i++ (ascii de Char) + (no. de intentos + ascii char)]
                # Funcion que depende del numero de iteracion lo que significa que si hay otra letra igual, la funcion no sera igual.

                hash += it * (ord(key[it])) + intents + ord(key[(keyLength-1)-it])
            return int(hash)
        
        i = self.__magicNumber
        while True:
            index = rehash(len(key),i) % self.__length

            if self.__isAvailable(index):
                print("{:<15}{:<10}{:<15}{:<2}".format(key,index,str(self.__hashList[index]),i))
                return index
            elif i < 6:
                i += 1
            else:
                print(f"Numero de intentos de rehash superado -> {key}.")
                break
    
    def __isAvailable(self, index: int):
        try:
            if self.__hashList[index] is None:
                return True
        except:
            return False
        return False
    
    def add(self, key: str):
        index = self.__hash__(key)
        if self.__isAvailable(index):
            self.__hashList[index] = key
            self.length += 1


""" 
obj_name = HashTable(value)     => La instanciacion de la clase HashTable, indica en el parametro el tamaño de la tabla.
add("Cadena de texto")          => Metodo que añade un nuevo valor a la tabla hash.
__isAvailable(index)            => Metodo privado que se asegura de saber si un modulo ya esta en uso o no. En caso de ser asi, retorna True, de lo contrario False
__hash__("Cadena de texto")     => Metodo privado que calcula el indice en el que se almacenara un elemento
"""


hash_list = HashTable(29)
# print("{:<15}{:<10}{:<15}{:<2}".format('key','index','value','Intentos'))

hash_list.add("Mario")
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
hash_list.add("adnanre")
hash_list.add("oiciruaM")
hash_list.add("oiraM")

