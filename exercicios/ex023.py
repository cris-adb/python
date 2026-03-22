import random

# Cria matriz 10x10 com números aleatórios
matriz = [[random.randint(0, 20) for j in range(10)] for i in range(10)]

# Exibe a matriz
for linha in matriz:
    print(linha)

# Conta quantos números são não nulos
nao_nulo = sum(1 for i in matriz for j in i if j != 0)

print(f"\nO número de posições não nulas é: {nao_nulo}")
