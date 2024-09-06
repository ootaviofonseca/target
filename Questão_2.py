def existe_A (entrada):
    cont = 0
    
    for i in entrada:
        if i == 'A' or i == 'a':
            cont += 1
            

    return cont


entrada = input()
cont = existe_A(entrada)
if  cont > 0:
    print(f"A letra A está presente {cont} vezes")
else:
    print("A letra A não está presente")
    