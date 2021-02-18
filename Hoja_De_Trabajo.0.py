Kg = input("Ingrese su peso en Kilogramos ")
Altu = input("Ingrese su altura en Metros ")

imc = round(float(Kg)/float(Altu)**2,2)

print("Tu indice de masa corporal es", imc)