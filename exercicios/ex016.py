# O Shell Sort é uma versão otimizada do Insertion Sort. Enquanto o Insertion Sort move elementos uma posição por vez, o Shell Sort permite a troca de elementos que estão distantes, usando um intervalo (gap) que diminui gradualmente.

# Imagine que você está organizando uma fila: em vez de comparar apenas o vizinho imediato, você primeiro compara pessoas que estão a 5 posições de distância, depois a 3, e finalmente a 1. Isso "pré-ordena" a lista, facilitando o trabalho final.

# Como funciona o algoritmo?
# Escolha do Gap: Começamos com um intervalo grande (geralmente a metade do tamanho da lista).

# Ordenação por Intervalo: Comparamos elementos separados por esse intervalo. Se estiverem fora de ordem, eles trocam de lugar.

# Redução do Gap: Reduzimos o intervalo (dividindo por 2) e repetimos o processo.

# Finalização: O processo termina quando o intervalo chega a 1, o que equivale a um Insertion Sort comum, mas em uma lista que já está quase ordenada.
# Por que usar o Shell Sort?Eficiência: É muito mais rápido que o Bubble Sort ou o Insertion Sort comum para listas de tamanho médio.In-place: Não exige memória extra significativa para ordenar os dados.Complexidade: Depende da sequência de gaps escolhida, mas geralmente fica entre $O(n \log n)$ e $O(n^2)$. Nota Curiosa: O nome do algoritmo não tem nada a ver com "conchas" de praia ou o terminal do Linux; ele foi batizado em homenagem ao seu criador, Donald Shell, que o publicou em 1959.

def shell_sort(lista):
    n = len(lista)
    gap = n // 2  # Iniciamos com o gap sendo a metade do tamanho

    while gap > 0:
        # Realizamos um insertion sort para cada intervalo do gap
        for i in range(gap, n):
            temp = lista[i]
            j = i
            
            # Desloca os elementos anteriores se forem maiores que o temp
            while j >= gap and lista[j - gap] > temp:
                lista[j] = lista[j - gap]
                j -= gap
            
            # Coloca o temp na sua posição correta
            lista[j] = temp
            
        gap //= 2  # Reduz o gap pela metade
    return lista

# Testando o código
numeros = [12, 34, 54, 2, 3]
print(f"Lista original: {numeros}")
shell_sort(numeros)
print(f"Lista ordenada: {numeros}")