# Solicita dois números inteiros ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# Calcula o quociente inteiro e o resto da divisão
quociente = num1 // num2
resto = num1 % num2

# Exibe o resultado
print(f"O quociente da divisão de {num1} por {num2} é: {quociente}")
print(f"O resto da divisão de {num1} por {num2} é: {resto}")
