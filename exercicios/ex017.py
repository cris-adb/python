# O Heapsort é um algoritmo de ordenação eficiente que utiliza uma estrutura de dados chamada Heap (amontoado). Para entendê-lo, imagine uma árvore binária onde cada "pai" é sempre maior que seus "filhos".
# Como o Heapsort funciona?
# O processo pode ser dividido em duas etapas principais:
# Construir o Max-Heap: Transformamos a lista bagunçada em uma estrutura de árvore onde o maior elemento está no topo (raiz).
# Extração e Reordenocação: * Pegamos o maior elemento (raiz) e o trocamos pelo último elemento da lista.
# "Diminuímos" o tamanho da árvore (já que o maior agora está no final, na posição correta).
# Refazemos o Heap para que o novo maior elemento suba para a raiz.
# Repetimos até que todos os elementos estejam ordenados.

def heapify(arr, n, i):
    """
    Transforma uma subárvore em um Max-Heap.
    n é o tamanho do heap, i é o índice do nó raiz da subárvore.
    """
    maior = i          # Inicializa o maior como raiz
    esquerda = 2 * i + 1 
    direita = 2 * i + 2  

    # Verifica se o filho da esquerda existe e é maior que a raiz
    if esquerda < n and arr[i] < arr[esquerda]:
        maior = esquerda

    # Verifica se o filho da direita existe e é maior que o maior atual
    if direita < n and arr[maior] < arr[direita]:
        maior = direita

    # Se o maior não for a raiz, troca e continua o processo
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]  # Swap
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)

    # 1. Constrói o Max-Heap (organiza a lista original)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2. Extrai os elementos um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move a raiz atual para o fim
        heapify(arr, i, 0)               # Chama heapify na árvore reduzida

# Testando o código
lista = [12, 11, 13, 5, 6, 7]
heap_sort(lista)
print(f"Lista ordenada: {lista}")