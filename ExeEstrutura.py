import numpy as np
# 1
list = [0]*5
for n in range(0,5):
    list[n] = int(input(f"Valor {n}: "))

#somar
soma = 0
for s in list:
    soma = soma + s

print(f'valor final é: {soma}')

# media dos alunos
notasAlunos = {}
for n in range(0,3):
    print("Digite a prima nota")
    notasAlunos[f'valor{n}'] = float(input())

somaDasNotas = 0
for chave,valor in notasAlunos.items():
    somaDasNotas = somaDasNotas + valor

print(f'A media do aluno foi: {somaDasNotas/3}')

#Somas dos elementos de uma matriz
matriz = np.array([[3,4,1],
                   [3,1,5]])

somaDosValoresDeUmaMatriz = 0
cont = 0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        somaDosValoresDeUmaMatriz = somaDosValoresDeUmaMatriz + matriz[i][j]
        cont += 1
print(f'Soma dos valores da matriz: {somaDosValoresDeUmaMatriz}')
print(f'Média: {somaDosValoresDeUmaMatriz/cont}')