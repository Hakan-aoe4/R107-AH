

def table_multiplication(n):
    table = []


    for i in range(10):
        result = round(n * i, 1)
        table.append(result)


    print(f"Vous cherchez la table de multiplication de quel nombre ?\n")
    for i, result in enumerate(table):
        print(f"{n} * {i} = {result}")



nombre = float(input("Veuillez entrer un nombre réel : "))
table_multiplication(nombre)




