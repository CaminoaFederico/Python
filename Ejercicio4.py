edad_alum = int(input("Ingrese la edad del alumno"))
if edad_alum == 18:
    print("Puede sacar registro")
else:
    if edad_alum < 18:
        print("Consultar")
    else:
        print("Más grande")
