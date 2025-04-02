def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos  = int(vuelto)
    centavos = int((vuelto - pesos) * 100)
    print(f"ingresar gasto:\n {expense}")
    print(f"dinero recibido:\n {money}\n")
    print("vuelto\n")
    print(f"pesos:\n{pesos}")
    print(f"centavos:\n{centavos}")
