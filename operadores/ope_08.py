# Solicita o preço do produto e a porcentagem de desconto ao usuário
preco = float(input("Digite o preço do produto: R$ "))
desconto_percentual = float(input("Digite a porcentagem de desconto: "))

# Calcula o valor do desconto
desconto = (preco * desconto_percentual) / 100

# Calcula o preço final do produto
preco_final = preco - desconto

# Exibe o valor do desconto e o preço final
print(f"O valor do desconto é: R$ {desconto:.2f}")
print(f"O preço final do produto com desconto é: R$ {preco_final:.2f}")
