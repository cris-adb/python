# Exemplo simples de uma matriz em Python

# Uma matriz é uma estrutura de dados bidimensional (linhas e colunas)
# Em Python, usamos listas de listas para criar matrizes

# Criando uma matriz 3x3
matriz = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

# Exibindo a matriz
print("Matriz:")
for linha in matriz:
	print(linha)

# Acessando um elemento específico (linha 0, coluna 1)
print("\nElemento na posição [0][1]:", matriz[0][1])

# Iterando sobre todos os elementos
print("\nTodos os elementos:")
for i in range(len(matriz)):
	for j in range(len(matriz[i])):
		print(matriz[i][j], end=" ")
	print()