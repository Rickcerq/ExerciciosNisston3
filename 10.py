i = int(input("Digite o número para pesquisar: "))
lista = [1, 2, 3, 5, 8, 9, 2]

if lista.count(i) > 1:
    while i in lista:
     lista.remove(i)
    print ('Elemento removido:', i)
    print ('Lista após a remoção', lista)
else:
    print("Esse numero não foi repetido, então não sera removido")
    print(lista)