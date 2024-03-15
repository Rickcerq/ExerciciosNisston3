palavras = ['anaconda', 'cobra', 'batata', 'amendoim', 'bola']
c = 0

for i in palavras:
    if i[0].upper()=='A':
        c+=1

print ('A quantidade de palavras que começam com "a" é de', c)