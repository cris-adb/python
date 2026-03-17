# O Quicksort é um dos algoritmos de ordenação mais eficientes e populares. Ele utiliza a estratégia de "divisão e conquista": escolhemos um elemento chamado pivô, colocamos tudo que é menor que ele à esquerda e tudo que é maior à direita. Depois, repetimos o processo para essas duas metades.
# Por que ele é tão bom? Divisão Inteligente: Ao contrário de algoritmos que comparam um por um (como o Bubble Sort), o Quicksort "limpa o terreno" rapidamente ao redor do pivô. Complexidade: Em média, ele tem uma performance de $O(n \log n)$, o que o torna excelente para grandes volumes de dados. Recursividade: O código é elegante porque resolve o problema quebrando-o em problemas menores de mesma natureza. Dica de Performance: Nesta versão simples, usamos memória extra para criar novas listas. Em sistemas de alta performance (como bibliotecas padrão de C++ ou Java), o Quicksort costuma ser feito "in-place", ou seja, trocando os elementos de posição dentro da própria lista original para economizar memória.

def quicksort(lista):
    # Caso base: se a lista tem 0 ou 1 elemento, ela já está ordenada
    if len(lista) <= 1:
        return lista
    
    # Escolhemos o elemento central como pivô
    pivo = lista[len(lista) // 2]
    
    # Cria três sublistas:
    # 1. Elementos menores que o pivô
    esquerda = [x for x in lista if x < pivo]
    
    # 2. Elementos iguais ao pivô (importante para lidar com duplicatas)
    meio = [x for x in lista if x == pivo]
    
    # 3. Elementos maiores que o pivô
    direita = [x for x in lista if x > pivo]
    
    # Chamada recursiva: ordena a esquerda e a direita e junta tudo
    return quicksort(esquerda) + meio + quicksort(direita)

# Exemplo de uso:
numeros = [34, 7, 23, 32, 5, 62]
resultado = quicksort(numeros)
print(f"Lista ordenada: {resultado}")
