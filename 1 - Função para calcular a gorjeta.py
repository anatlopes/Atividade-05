
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Programa principal
valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))

valor_gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"A gorjeta é: R$ {valor_gorjeta:.2f}")
