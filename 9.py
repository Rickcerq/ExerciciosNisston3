lista1 = [1, 2, 8, 9, 10]
lista2 = [2, 3, 4, 5, 7]

numero_pesquisar = int(input('Qual número você deseja pesquisar?: '))

presente_em_ambas = False
presente_apenas_em_uma = False

for a, b in zip(lista1, lista2):
    if numero_pesquisar == a == b:
        presente_em_ambas = True
    elif numero_pesquisar == a or numero_pesquisar == b:
        presente_apenas_em_uma = True

if presente_em_ambas:
    print('O número', numero_pesquisar, 'está presente em ambas as listas.')
elif presente_apenas_em_uma:
    print('O número', numero_pesquisar, 'está presente apenas em uma das listas.')
else:
    print('O número', numero_pesquisar, 'não está presente em nenhuma das listas.')