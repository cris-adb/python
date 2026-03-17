# O Insertion Sort (ou Ordenação por Inserção) funciona de maneira muito semelhante a como organizamos cartas de baralho na mão: você pega uma carta por vez e a "insere" na posição correta em relação às que já estão ordenadas. 
# Como funciona a lógica? O algoritmo percorre a lista da esquerda para a direita. Para cada elemento, ele olha para trás (para a esquerda) e o desloca até encontrar o seu lugar correto entre os elementos que já foram processados.

def insertion_sort(lista):
    # Começamos do segundo elemento (índice 1), pois um único 
    # elemento (índice 0) já é considerado "ordenado" por si só.
    for i in range(1, len(lista)):
        
        chave = lista[i]  # O elemento que vamos tentar encaixar
        j = i - 1         # O índice do elemento imediatamente à esquerda
        
        # Enquanto não chegarmos no início da lista E o elemento da esquerda 
        # for maior que a nossa 'chave', movemos o da esquerda para a direita.
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
            
        # Quando o loop para, encontramos a posição correta (j + 1)
        # e inserimos a chave ali.
        lista[j + 1] = chave

    return lista

# Testando o algoritmo
numeros = [12, 11, 13, 5, 6]
print(f"Lista original: {numeros}")

ordenados = insertion_sort(numeros)
print(f"Lista ordenada: {ordenados}")