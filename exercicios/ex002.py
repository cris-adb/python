def add(a, b):
	return a + b

def subtract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b == 0:
		return "Erro: divisão por zero"
	return a / b

print("Calculadora")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

choice = input("Escolha uma operação (1/2/3/4): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if choice == "1":
	print(f"Resultado: {add(num1, num2)}")
elif choice == "2":
	print(f"Resultado: {subtract(num1, num2)}")
elif choice == "3":
	print(f"Resultado: {multiply(num1, num2)}")
elif choice == "4":
	print(f"Resultado: {divide(num1, num2)}")
else:
	print("Operação inválida")