a=str(input("Ingresa una palabra: ")).replace(" ","").upper()
b=str(input("Ingresa otra palabra: ")).replace(" ","").upper()
if len(a) == len(b) and set(a) == set(b):
    print("Son anagramas")