import numpy as np

matriz = np.array([[2,3,1],
                   [4,5,6]])

print(matriz)
print(matriz[0])
print(matriz[1][2])

for i in range(matriz.shape[0]):
    print(f'valor da linha: {matriz[i]}')
    for j in range(matriz.shape[1]):
        print(f'colunas: {matriz[i][j]}')
