t = int(input("Introduzca el tamaño del triangulo: "))

for i in range(t):
    for j in range(i+1):
        print("*", end="")
    print("")

p = int(input("Introduzca un numero para verificar si es primo: "))

for i in range(2,p):
    if p%i == 0:
        print("No es un numero primo")
        r = 0
        break
    else: 
        print("Es un numero primo")
        break


