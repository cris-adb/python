# Definindo a matriz 3x4
matriz = [
    [1.5, 2.0, 3.7, 4.2],
    [5.1, 6.8, 0.5, 8.9],
    [9.3, 2.4, 7.6, 1.1]
]

i = 0  # Contador das linhas
while i < 3:    # Enquanto i for menor que o número de linhas (0, 1, 2)
    j = 0       # Reinicia o contador de colunas para cada nova linha
    while j < 4:  # Enquanto j for menor que o número de colunas (0, 1, 2, 3)
        print(f"Elemento na posição [{i}][{j}]: {matriz[i][j]}")
        j += 1    # Incrementa a coluna
    
    print("-" * 20) # Linha divisória para organizar a visualização
    i += 1    # Incrementa a linha