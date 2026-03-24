# A Tabela Hash (ou Hash Table) é uma das estruturas de dados mais poderosas e eficientes na computação. No Python, você já a usa o tempo todo, mesmo sem saber: o dicionário (dict) e o conjunto (set) são implementações de tabelas hash.

# O que é uma Tabela Hash?
# Imagine que você tem um armário gigante com milhares de gavetas. Se você guardar uma meia em uma gaveta aleatória, levará horas para achar. Mas, se você tiver uma fórmula mágica que diz: "Meias azuis sempre ficam na gaveta 42", você a encontra instantaneamente.

# A Tabela Hash funciona assim:
# Chave (Key): O nome do dado que você quer guardar (ex: "ID_usuario").
# Função Hash: Um algoritmo que transforma essa "Chave" em um índice numérico (o número da gaveta).
# Valor (Value): O conteúdo guardado naquela posição.
# A grande vantagem é a velocidade. Na Tabela Hash, você aplica a função na chave e vai direto ao ponto. O tempo de busca, inserção e remoção é, em média, constante, ou seja, $O(1)$.

# Criando nossa "Tabela Hash" (Dicionário)
estoque = {}

# Inserindo dados - O(1)
estoque["teclado"] = 50
estoque["mouse"] = 120
estoque["monitor"] = 30

# Buscando um valor - O(1)
item = "teclado"
print(f"Quantidade de {item}: {estoque[item]}")

# Removendo um dado - O(1)
del estoque["monitor"]

print(estoque)

# O que acontece "por baixo do capô"?
# Se você estivesse construindo uma do zero, precisaria lidar com dois conceitos fundamentais:

# A Função Hash
# O Python possui uma função interna chamada hash(). Ela transforma objetos em números inteiros.

# Colisões
# O que acontece se duas chaves diferentes gerarem o mesmo índice? Isso é uma colisão.

# Encadeamento (Chaining): Cada posição da tabela armazena uma lista. Se houver colisão, os itens ficam na mesma "gaveta".

# Endereçamento Aberto: O sistema procura a próxima gaveta vazia. O Python usa uma variação sofisticada disso para manter a performance.

# Regra de Ouro: Imutabilidade
# Para que um objeto seja usado como Chave em uma tabela hash no Python, ele deve ser hashable (imutável).

# Pode ser chave: Strings, Números, Tuplas.

# NÃO pode ser chave: Listas, Dicionários (pois podem mudar de valor e alterariam o hash, "perdendo" o objeto no armário).