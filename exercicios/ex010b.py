# Pilhas (Stacks) - LIFO A regra de ouro da pilha é LIFO (Last In, First Out), ou seja: O último a entrar é o primeiro a sair. Imagine uma pilha de pratos: você sempre coloca o novo prato no topo e, ao retirar, retira o do topo também. Operação Principal: append() para empilhar e pop() (sem índice) para desempilhar. Uso comum: Histórico de navegação (botão voltar) e funções de "Desfazer" (Ctrl+Z).

historico = []

# Empilhando (Push)
historico.append("google.com")
historico.append("github.com")
historico.append("python.org")

# Desempilhando (Pop)
pagina_atual = historico.pop() 
print(f"Saindo de: {pagina_atual}") # Saída: python.org
print(f"Pilha restante: {historico}") # ['google.com', 'github.com']