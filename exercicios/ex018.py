# Existem várias formas de buscar um item em uma lista no Python, dependendo do que você precisa: apenas saber se o item existe, descobrir a posição dele ou filtrar vários itens que atendam a um critério.
# Verificar se um item existe (in)
# Se o seu objetivo é apenas um "sim ou não", o operador in é a forma mais legível e rápida de escrever.

frutas = ["maçã", "banana", "cereja"]
if "maçã" in frutas: 
    print("Encontrei a maçã!")
else: 
    print("Não tem essa fruta na lista!")

# Encontrar o índice (posição) do item (index)
# Se você precisa saber onde o item está, use o método .index().
# Atenção: Se o item não estiver na lista, o Python retornará um erro (ValueError). Por isso, é boa prática verificar antes ou usar um bloco try/except.

frutas = ["maçã", "banana", "cereja"]
try:
    posicao = frutas.index("maçã")
    print(f"A maçã está na posição {posicao}")
except ValueError:
    print("Item não encontrado.")

# Busca Linear Manual (Loop for)
# Essa é a lógica "raiz". Você percorre item por item. É útil quando você precisa aplicar uma condição lógica mais complexa (ex: buscar nomes que começam com "A").

precos = [10, 25, 50, 100, 120]
busca = 50

for i in range(len(precos)):
    if precos[i] == busca:
        print(f"Item encontrado no índice {i}")
        break

# Filtrar múltiplos itens (List Comprehension)
# Se você quer encontrar todos os itens que atendem a uma regra, a List Comprehension é a ferramenta ideal.

numeros = [1, 5, 8, 10, 15, 20]

# Buscar todos os números maiores que 10
maiores_que_10 = [n for n in numeros if n > 10]

print(maiores_que_10) # Saída: [15, 20]

# Dica de Performance: Se você precisa fazer buscas o tempo todo em uma lista muito grande e a ordem não importa, considere transformar sua lista em um Set (set). A busca em sets é instantânea, enquanto em listas ela fica mais lenta conforme a lista cresce.