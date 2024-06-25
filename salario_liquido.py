"""
Requisitos:
Salário Mínimo (2024): R$ 1.412,00

Tabela INSS 2024
Salário de contribuição        Alíquota (%)
Até 1.412,00                       7,50
De 1.412,01 até 2.666,68           9,00
De 2.666,69 até 4.000,03          12,00
De 4.000,04 até 7.786,02          14,00

Tabela IRRF
Faixa salarial (R$)            Alíquota (%)           Parcela a deduzir do IRPF (R$)
Até 2.112,00                       0                               0
De 2.112,01 até 2.826,65           7,50                          158,40
De 2.826,66 até 3.751,05          15,00                          370,40
De 3.751,06 até 4.664,68          22,50                          651,73
Acima de 4.664,68                 27,50                          884,96
"""

def calcular_inss(salario_bruto):
    if salario_bruto <= 1412.00:
        return salario_bruto * 0.075
    elif salario_bruto <= 2666.68:
        return 1412.00 * 0.075 + (salario_bruto - 1412.00) * 0.09
    elif salario_bruto <= 4000.03:
        return 1412.00 * 0.075 + (2666.68 - 1412.00) * 0.09 + (salario_bruto - 2666.68) * 0.12
    elif salario_bruto <= 7786.02:
        return 1412.00 * 0.075 + (2666.68 - 1412.00) * 0.09 + (4000.03 - 2666.68) * 0.12 + (salario_bruto - 4000.03) * 0.14
    else:
        return 1412.00 * 0.075 + (2666.68 - 1412.00) * 0.09 + (4000.03 - 2666.68) * 0.12 + (7786.02 - 4000.03) * 0.14

def calcular_irrf(salario_base):
    if salario_base <= 2112.00:
        return 0
    elif salario_base <= 2826.65:
        return salario_base * 0.075 - 158.40
    elif salario_base <= 3751.05:
        return salario_base * 0.15 - 370.40
    elif salario_base <= 4664.68:
        return salario_base * 0.225 - 651.73
    else:
        return salario_base * 0.275 - 884.96

def calcular_salario_liquido(salario_bruto):
    desconto_inss = calcular_inss(salario_bruto)
    salario_base_irrf = salario_bruto - desconto_inss
    desconto_irrf = calcular_irrf(salario_base_irrf)
    salario_liquido = salario_bruto - desconto_inss - desconto_irrf
    total_descontos = desconto_inss + desconto_irrf

    return {
        "Salário Bruto": round(salario_bruto, 2),
        "Desconto INSS": round(desconto_inss, 2),
        "Salário Base IRRF": round(salario_base_irrf, 2),
        "Desconto IRRF": round(desconto_irrf, 2),
        "Total de Descontos": round(total_descontos, 2),
        "Salário Líquido": round(salario_liquido, 2)
    }

# Exemplo de uso
salario_bruto = float(input("Informe o valor do salário bruto: "))

resultado = calcular_salario_liquido(salario_bruto)
print("Cálculo do Salário Líquido:")
for chave, valor in resultado.items():
    print(f"{chave}: R$ {valor}")
