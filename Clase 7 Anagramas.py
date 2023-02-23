a = sorted(str(input("Palabra 1: ")).replace(" ","").upper())
b = sorted(str(input("Palabra 2: ")).replace(" ","").upper())
if a == b:
    print("Son Acronimos")
else:
    print("No son Acronimos")
