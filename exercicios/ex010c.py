# Filas (Queues) - FIFO A regra da fila é FIFO (First In, First Out): O primeiro a entrar é o primeiro a sair. Como uma fila de banco. Dica de Performance: Embora você possa usar list.pop(0), isso é lento em Python porque o PC precisa "puxar" todos os outros itens para frente. Para filas, usamos o deque da biblioteca collections. Uso comum: Impressoras, processamento de mensagens e sistemas de atendimento.

from collections import deque

# Criando uma fila
fila_atendimento = deque(["Ana", "Carlos", "Beatriz"])

# Adicionando à fila (Enqueue)
fila_atendimento.append("Daniel")

# Removendo da fila (Dequeue) - O primeiro a chegar sai primeiro
cliente_atendido = fila_atendimento.popleft()

print(f"Atendendo agora: {cliente_atendido}") # Saída: Ana
print(f"Próximos na fila: {list(fila_atendimento)}") # ['Carlos', 'Beatriz', 'Daniel']