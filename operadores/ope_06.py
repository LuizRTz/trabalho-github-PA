# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Troca os valores usando operadores matemáticos
num1 = num1 + num2  # num1 agora contém a soma dos dois números
num2 = num1 - num2  # subtrai num2 do novo num1, resultando no valor original de num1
num1 = num1 - num2  # subtrai num2 (agora o valor original de num1) de num1, resultando no valor original de num2

# Exibe os resultados após a troca
print(f"Após a troca, o primeiro número é: {num1}")
print(f"Após a troca, o segundo número é: {num2}")
