# Entender a diferença entre Listas, Filas e Pilhas é fundamental para organizar dados de forma eficiente. Embora em Python possamos usar uma list para representar todas elas, a maneira como inserimos e removemos os itens muda completamente a lógica do algoritmo.
# Listas (Dinâmicas) A lista em Python é uma estrutura flexível onde você pode acessar, inserir ou remover elementos em qualquer posição através de um índice.Acesso: Aleatório (você acessa o índice 0, 10 ou 50 instantaneamente). Uso comum: Armazenar coleções de itens onde a ordem de chegada não é a única regra.

# Exemplo de Lista
compras = ["Arroz", "Feijão", "Carne"]
compras.append("Leite")  # Adiciona ao fim
compras.insert(1, "Ovo") # Insere na posição 1
compras.pop(2)           # Remove o item da posição 2 (Feijão)

print(compras) # ['Arroz', 'Ovo', 'Carne', 'Leite']