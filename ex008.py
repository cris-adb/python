# Matriz inicial 3x4
matriz = [
    [1.5, 2.0, 3.7, 4.2],
    [5.1, 6.8, 0.5, 8.9],
    [9.3, 2.4, 7.6, 1.1]
]

print("--- Matriz Atual ---")
for l in matriz: print(l)

# 1. Escolhendo a Linha (com validação)
linha = -1
while linha < 0 or linha > 2:
    linha = int(input("\nDigite a linha que deseja alterar (0, 1 ou 2): "))
    if linha < 0 or linha > 2:
        print("Erro! A linha deve ser 0, 1 ou 2.")

# 2. Escolhendo a Coluna (com validação)
coluna = -1
while coluna < 0 or coluna > 3:
    coluna = int(input("Digite a coluna que deseja alterar (0, 1, 2 ou 3): "))
    if coluna < 0 or coluna > 3:
        print("Erro! A coluna deve ser entre 0 e 3.")

# 3. Alterando o valor
novo_valor = float(input(f"Digite o novo valor real para a posição [{linha}][{coluna}]: "))
matriz[linha][coluna] = novo_valor

print("\n--- Matriz Atualizada ---")
for l in matriz: print(l)