# O Selection Sort (Ordenação por Seleção) é um dos algoritmos de ordenação mais fundamentais na computação. Ele recebe esse nome porque sua lógica principal é selecionar repetidamente o menor elemento de uma lista e movê-lo para a posição correta.

# O que é?
# É um algoritmo de ordenação por comparação e in-place (em tradução livre, "no lugar"). Isso significa que ele não precisa de uma lista auxiliar ou memória extra para funcionar; ele reorganiza os itens dentro da própria lista original.

# Como funciona? (Passo a passo)
# Imagine que você tem uma lista de números desordenados. O algoritmo divide essa lista em duas partes imaginárias: uma sublista de itens já ordenados e uma sublista de itens não ordenados.

# Busca do Menor: O algoritmo varre a parte não ordenada da lista para encontrar o menor valor.

# Troca (Swap): Uma vez encontrado o menor valor, ele o troca de lugar com o primeiro item da parte não ordenada.

# Expansão: Agora, esse item faz parte da sublista "ordenada". O algoritmo repete o processo para o restante da lista, começando da próxima posição.
# Exemplo Visual:Lista: [20, 12, 10, 15]1ª Passagem: O menor é 10. Troca com o primeiro (20).Lista: [10, 12, 20, 15]2ª Passagem: O menor entre 12, 20, 15 é o 12. Ele já está no lugar certo.Lista: [10, 12, 20, 15]3ª Passagem: O menor entre 20, 15 é o 15. Troca com o 20.Lista: [10, 12, 15, 20] -> Ordenado! Qual a utilidade? Embora não seja o algoritmo mais rápido para grandes volumes de dados (como o Quick Sort ou Merge Sort), o Selection Sort tem nichos importantes: Sistemas com Memória Limitada: Como ele não cria cópias da lista, é extremamente eficiente em termos de uso de memória (espaço $O(1)$).Custo de Gravação (Writes): Ele é único porque faz o número mínimo de trocas de memória. Em sistemas onde "escrever" no disco ou na memória é muito caro ou desgasta o hardware (como memórias Flash antigas), ele pode ser vantajoso. Didática: É a porta de entrada para entender a lógica de algoritmos e complexidade computacional ($O(n^2)$). Resumo Técnico Complexidade de Tempo: $O(n^2)$ em todos os casos (melhor, médio e pior). Ele sempre verifica todos os itens, mesmo que a lista já esteja quase pronta. Complexidade de Espaço: $O(1)$. Estabilidade: Geralmente não é estável (pode mudar a ordem relativa de elementos iguais).

def selection_sort(lista):
    n = len(lista)
    
    # Percorre toda a lista
    for i in range(n):
        # Começamos assumindo que o primeiro item não ordenado é o menor
        indice_do_menor = i
        
        # Este loop procura o verdadeiro menor item no restante da lista
        for j in range(i + 1, n):
            if lista[j] < lista[indice_do_menor]:
                indice_do_menor = j
        
        # Após encontrar o menor, trocamos ele com o item da posição atual (i)
        # Em Python, podemos trocar dois valores de lugar de forma simples:
        lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]
        
    return lista

# Testando o algoritmo
numeros = [64, 25, 12, 22, 11]
print(f"Lista original: {numeros}")

lista_ordenada = selection_sort(numeros)
print(f"Lista ordenada: {lista_ordenada}")