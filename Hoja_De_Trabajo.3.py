def verifica(co):
    x = "contraseña"
    if x == co:
        print("La contraseña coincide")
    else:
        print("La contranseña no coincide")


contra = input("Ingrese una contraseña: ")
contra_minus = contra.lower()

verifica(contra_minus)
print("")

nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su genero hombre(H) o mujer(M): ")
genero_minus = genero.lower()
nombre_minus = nombre.lower()

if genero_minus == "h":
    if nombre_minus > 'n':
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre_minus[0] < 'm':
        grupo = "A"
    else:
        grupo = "B"

print("Tu grupo es "+grupo)