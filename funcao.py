
# definindo funcao
def msg(texto):
    print(texto)

texto = input("Qual msg voce quer mandar")
msg(texto)

def nome(name):
    print(f"Seu nome é: {name}")

nome('Marelo')

def somar(n1,n2):
    return n1+n2

soma = somar(1,2)
print(soma)

def media(soma):
    return soma/2

media = media(somar(1,2))
print(media)

valor = {'item': 4}
def exi(valor):
    print(valor)

print(valor)