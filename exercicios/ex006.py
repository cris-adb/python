# Uma matriz é uma estrutura de dados bidimensional (tabela com linhas e colunas)
# Função: Armazenar e organizar dados em formato de tabela
# Para que usar: Útil para operações matemáticas, jogos (como sudoku), processamento de imagens, etc.

# Criar a matriz 9x9 preenchida com zeros
matriz = [[0 for _ in range(9)] for _ in range(9)]

# Exibir a matriz
for linha in matriz:
	print(linha)

# Exemplo: Preenchendo a matriz com números de 1 a 81
matriz_preenchida = [[i * 9 + j + 1 for j in range(9)] for i in range(9)]

print("\nMatriz preenchida de 1 a 81:")
for linha in matriz_preenchida:
	print(linha)