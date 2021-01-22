
#  conceito de chave e valor
# ojbjeto no javaScrit
dicionario = {'nome':1,'idade':2}
print(dicionario)

# imprimir a quantidade
print(dicionario['nome'])

# add novo elemtno
dicionario['data'] = 5
print(dicionario)
# apagar
del(dicionario)['data']
print(dicionario)

print(dicionario.items())
print(dicionario.keys())
print(dicionario.values())

#update
dicionario1 = {'nom21':21,'valor':2}
dicionario.update(dicionario1)
print(dicionario)

# for
for key,valor in dicionario.items():
    # print('chave',key,"--",'valor:',valor)
    print(f'chave {key} e valor {valor}')

c1 = {1,2,3,4}
c2 = {3,4,5,6}
c3 = c1.intersection(c1)
print(c3)