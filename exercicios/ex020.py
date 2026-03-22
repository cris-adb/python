# A Busca Binária é o "divisor de águas" da eficiência. Enquanto na busca sequencial você olha item por item, na binária você usa a estratégia de dividir para conquistar.
# Imagine que você está procurando uma palavra em um dicionário físico de 1000 páginas. Você não começa da página 1; você abre no meio. Se a palavra que você quer vem depois daquela página, você descarta a primeira metade inteira e repete o processo na metade que sobrou.
# O Requisito Fundamental
# Para que a Busca Binária funcione, a sua lista DEVE estar ordenada (do menor para o maior). Se a lista estiver bagunçada, o algoritmo se perde.
# Como o Algoritmo Funciona:
# Encontre o meio da lista.
# O item no meio é o que você procura? Se sim, acabou!
# O item que você procura é menor que o do meio? Ignore a metade direita.
# O item que você procura é maior que o do meio? Ignore a metade esquerda.
# Repita o processo com a metade restante até encontrar ou a lista acabar.

def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        
        if lista[meio] == alvo:
            return meio  # Encontrou!
        elif lista[meio] < alvo:
            esquerda = meio + 1  # Busca na metade da direita
        else:
            direita = meio - 1   # Busca na metade da esquerda
            
    return -1  # Não encontrou

# Exemplo:
numeros_ordenados = [10, 20, 30, 40, 50, 60, 70, 80, 90]
resultado = (busca_binaria(numeros_ordenados, 50)) # Retorna o índice 
print(f"Elemento encontrado no índice: {resultado}")

# Resumo: Qual usar?
# Use Busca Sequencial se a lista for pequena ou se ela mudar o tempo todo (não valendo a pena o esforço de ordenar).# 
# Use Busca Binária se você tem uma lista gigante que permanece ordenada ou se você fará milhares de buscas na mesma lista.