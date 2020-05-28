cheque1 = int(input("Ingrese el primer importe"))
cheque2 = int(input("Ingrese el segundo importe"))
cheque3 = int(input("Ingrese el tercer importe"))
total = cheque1 + cheque2 + cheque3
if total == 50000:
    print("Avisar en Gerencia")
else:
    if total > 70000:
        print("Pedir Auditoria")
    else:
        if total < 30000:
            print("Guardar para el día siguiente")
        else:
            print("Depositar")
