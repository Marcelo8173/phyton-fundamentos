with open('arquivo.txt') as tex:
    for linha in tex:
        print(linha)

with open('arquivo.txt') as tex:
    r = tex.readlines()
print('a',r)

#criando
with open('new.txt','w') as text:
    text.write('Novo arquivo de texto')
