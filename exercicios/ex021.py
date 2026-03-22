# Quando precisamos encontrar múltiplos itens (ou todas as ocorrências de um item) em uma lista, a busca sequencial muda um pouco de figura. Em vez de parar no primeiro resultado com um return ou break, nós precisamos percorrer a lista até o final e armazenar os achados em uma nova estrutura.

# Usando um Loop for Simples
# Esta é a abordagem clássica: criamos uma lista vazia e "penduramos" nela cada posição onde encontramos o que buscamos.

def buscar_todos(lista, alvo):
    indices_encontrados = []
    
    for i in range(len(lista)):
        if lista[i] == alvo:
            indices_encontrados.append(i)
            
    return indices_encontrados

# Exemplo:
precos = [10, 50, 20, 50, 30, 50]
print(buscar_todos(precos, 50))  # Saída: [1, 3, 5]

# Usando List Comprehension (A forma "Pythonica")
# Se você quer um código limpo e rápido, a compreensão de lista com a função enumerate é a melhor escolha. O enumerate nos dá o índice e o valor ao mesmo tempo.

lista = ["a", "b", "a", "c", "a"]
alvo = "a"

# "Me dê o índice (i) para cada valor (v) na lista se o valor for o alvo"
indices1 = [i for i, v in enumerate(lista) if v == alvo]

print(indices1)  # Saída: [0, 2, 4]

# Busca por Critérios (Filtro)
# Às vezes, "múltiplos itens" não significa o mesmo valor, mas itens que seguem uma regra (ex: todos os números pares).

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Busca sequencial por todos os pares
pares = [n for n in numeros if n % 2 == 0]
indices = [n for n in numeros if n % 2 != 0]
print(pares)  # Saída: [2, 4, 6, 8, 10, 12]
print(indices) # Saída: [1, 3, 5, 7, 9, 11]