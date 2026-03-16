# O Bubble Sort (ou Ordenação por Bolha) é um dos algoritmos de ordenação mais simples e intuitivos. Ele recebe esse nome porque os maiores elementos "flutuam" para o topo da lista a cada iteração, como bolhas em um copo de refrigerante.
# Como ele funciona? O algoritmo percorre a lista várias vezes. Em cada passagem, ele compara elementos adjacentes e os troca de lugar se estiverem na ordem errada (ex: o da esquerda maior que o da direita). Esse processo se repete até que nenhum elemento precise mais ser trocado.

def bubble_sort(lista):
    n = len(lista)
    
    # O loop externo percorre toda a lista
    for i in range(n):
        # O loop interno vai até n-i-1 porque os últimos i elementos já estão ordenados
        for j in range(0, n - i - 1):
            
            # Compara o elemento atual com o próximo
            if lista[j] > lista[j + 1]:
                
                # Se estiverem fora de ordem, realiza a troca (swap)
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                
    return lista

# Testando o algoritmo
numeros = [71, 99, 43, 8, 26, 12, -87]
print(f"Lista original: {numeros}")

lista_ordenada = bubble_sort(numeros)
print(f"Lista ordenada: {lista_ordenada}")