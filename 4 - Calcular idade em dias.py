
def idade_em_dias(ano_nascimento, ano_atual):
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365

# Programa principal
ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade_dias = idade_em_dias(ano_nasc, ano_atual)
print(f"Sua idade aproximada em dias é: {idade_dias} dias")
