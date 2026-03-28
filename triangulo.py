v1 = int(input("valor 1: "))
v2 = int(input("valor 2: "))
v3 = int(input("valor 3: "))

if(v1 < 0 or v2 < 0 or v3 < 0):
    print("Valores inválidos")
if (not (v1 + v2 > v3 and v2 + v3 > v1 and v3 + v1 > v2)):
    print("Triângulo inválido")
elif(v1 == v2 and v2 == v3):
    print("O triângulo é equilátero")
elif(v1 == v2 or v2 == v3 or v1 == v3):
    print("O triângulo é isósceles")
elif(v1 != v2 and v2 != v3 and v1 != v3):
    print("O triângulo é escaleno")
