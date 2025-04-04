def change():
    expense = 23.75
    money = 100
    
    print(f"ingresar gasto:")
    print (expense) 
    print("dinero recibido")
    print (money)
    print("\nvuelto\n")
    print("pesos:")
    vuelto = money-expense
    pesos=int(vuelto) 
    print (pesos)
    print ("centavos:")
    centavos= vuelto-pesos
    centavos_entero=int(centavos*100)
    print (centavos_entero)

change()
