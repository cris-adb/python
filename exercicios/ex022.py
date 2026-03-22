# Diferente da busca sequencial, a Busca Binária para múltiplos itens é um pouco mais "truculenta". O algoritmo padrão para assim que encontra a primeira ocorrência, mas quando temos valores duplicados (ex: buscar todos os números 50 em [10, 50, 50, 50, 80]), precisamos de uma estratégia para encontrar o intervalo (o primeiro e o último índice do item).

# A Estratégia dos "Limites" (Left & Right)
# Em vez de uma busca simples, fazemos duas buscas binárias modificadas:
# Busca à Esquerda: Encontra a primeira ocorrência.
# Busca à Direita: Encontra a última ocorrência.

import bisect

def busca_binaria_multipla(lista, alvo):
    # bisect_left: encontra o primeiro índice onde o alvo poderia ser inserido
    inicio = bisect.bisect_left(lista, alvo)
    
    # bisect_right: encontra o último índice + 1
    fim = bisect.bisect_right(lista, alvo)
    
    # Verifica se o alvo realmente existe no intervalo encontrado
    if inicio < len(lista) and lista[inicio] == alvo:
        return list(range(inicio, fim))
    else:
        return []

# Exemplo:
numeros = [10, 20, 30, 30, 30, 40, 50]
indices = busca_binaria_multipla(numeros, 30)

print(f"O número 30 aparece nos índices: {indices}") 
# Saída: [2, 3, 4]

#Expansão Lateral (Híbrida)Esta técnica encontra uma ocorrência usando a busca binária comum e depois "caminha" para os lados (sequencialmente) para ver até onde o número se repete.
# Atenção: Se houver muitos itens repetidos (ex: uma lista de 1 milhão de itens onde 900 mil são o mesmo número), essa técnica perde a eficiência e volta a ser $O(n)$.

def busca_binaria_expansiva(lista, alvo):
    esq, dir = 0, len(lista) - 1
    ponto_inicial = -1
    
    # 1. BUSCA BINÁRIA PADRÃO (Encontra QUALQUER uma das ocorrências)
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            ponto_inicial = meio
            break # Encontrou UM dos itens, agora para a busca binária
        elif lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
            
    # Se não encontrou o número na lista toda
    if ponto_inicial == -1: 
        return []

    # 2. EXPANSÃO (Caminha para os lados para pegar os vizinhos iguais)
    indices = [ponto_inicial]
    
    # Olhar para a esquerda (índices menores)
    i = ponto_inicial - 1
    while i >= 0 and lista[i] == alvo:
        indices.append(i)
        i -= 1
        
    # Olhar para a direita (índices maiores)
    i = ponto_inicial + 1
    while i < len(lista) and lista[i] == alvo:
        indices.append(i)
        i += 1
        
    return sorted(indices)

# --- DADOS DE TESTE ---
# Lista ordenada com vários números repetidos
notas = [4.5, 5.0, 6.5, 7.0, 7.0, 7.0, 8.5, 9.0, 10.0]
nota_procurada = 7.0

resultado = busca_binaria_expansiva(notas, nota_procurada)

print(f"Lista de Notas: {notas}")
print(f"Buscando pela nota: {nota_procurada}")
print(f"Encontrada nos índices: {resultado}")
# Saída esperada: [3, 4, 5]