class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        # A lista nasce vazia, sem nenhuma cabeça (início)
        self.cabeca = None

    def inserir_no_final(self, dado):
        novo_no = No(dado)
        
        # Se a lista estiver vazia, o novo nó é o primeiro
        if self.cabeca is None:
            self.cabeca = novo_no
            return

        # Se não estiver vazia, precisamos "caminhar" até o último
        atual = self.cabeca
        while atual.proximo:
            atual = atual.proximo
        
        # Quando chegamos no último (onde proximo é None), conectamos o novo
        atual.proximo = novo_no

    def exibir(self):
        atual = self.cabeca
        while atual:
            print(f"{atual.dado} -> ", end="")
            atual = atual.proximo
        print("None")

# --- TESTANDO O CÓDIGO ---
minha_lista = ListaEncadeada()
minha_lista.inserir_no_final(10)
minha_lista.inserir_no_final(20)
minha_lista.inserir_no_final(30)

print("Conteúdo da lista:")
minha_lista.exibir()