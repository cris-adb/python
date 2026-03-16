# Entendendo a Travessia "Em Ordem" (In-Order)Imagine que a função funciona como uma pessoa caminhando pela borda da árvore. No método In-Order, o computador segue esta lógica:"Vou o máximo que puder para a esquerda." "Quando não houver mais nada à esquerda, eu leio o valor do nó atual." "Depois, tento ir para a direita e repito o processo." Por que isso é útil? Ordenação: Como você viu, percorrer uma BST "em ordem" é uma maneira extremamente eficiente de ordenar dados. Expressões Matemáticas: Árvores são usadas por compiladores para entender contas como $(2 + 3) * 5$. A estrutura da árvore garante que a soma ocorra antes da multiplicação. Qual a diferença para os outros métodos? Pre-order (Raiz, Esq, Dir): Útil para criar uma cópia exata da árvore.Post-order (Esq, Dir, Raiz): Útil para deletar uma árvore (você apaga os filhos antes de apagar o pai).

class No:
    def __init__(self, chave):
        self.valor = chave
        self.esquerda = None
        self.direita = None

def inserir(raiz, valor):
    # Se a árvore estiver vazia, cria o primeiro nó
    if raiz is None:
        return No(valor)
    else:
        # Regra da BST: Menores à esquerda, maiores à direita
        if valor < raiz.valor:
            raiz.esquerda = inserir(raiz.esquerda, valor)
        else:
            raiz.direita = inserir(raiz.direita, valor)
    return raiz

def percorrer_em_ordem(raiz):
    """Visita: Esquerda -> Raiz -> Direita"""
    if raiz:
        percorrer_em_ordem(raiz.esquerda)
        print(raiz.valor, end=" ")
        percorrer_em_ordem(raiz.direita)

# --- Testando a Árvore ---
raiz = None
valores = [50, 30, 70, 20, 40, 60, 80]

for v in valores:
    raiz = inserir(raiz, v)

print("Elementos da árvore em ordem crescente:")
percorrer_em_ordem(raiz) 
# Saída esperada: 20 30 40 50 60 70 80