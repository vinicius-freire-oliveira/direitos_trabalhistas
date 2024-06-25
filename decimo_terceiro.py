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

import datetime

# Funções auxiliares para cálculo do INSS e IRRF
def calcular_inss(salario):
    if salario <= 1412.00:
        return salario * 0.075
    elif salario <= 2666.68:
        return 1412.00 * 0.075 + (salario - 1412.00) * 0.09
    elif salario <= 4000.03:
        return 1412.00 * 0.075 + (2666.68 - 1412.00) * 0.09 + (salario - 2666.68) * 0.12
    elif salario <= 7786.02:
        return 1412.00 * 0.075 + (2666.68 - 1412.00) * 0.09 + (4000.03 - 2666.68) * 0.12 + (salario - 4000.03) * 0.14
    else:
        return 1412.00 * 0.075 + (2666.68 - 1412.00) * 0.09 + (4000.03 - 2666.68) * 0.12 + (7786.02 - 4000.03) * 0.14

def calcular_irrf(salario):
    base_calculo = salario - calcular_inss(salario)
    if base_calculo <= 2112.00:
        return 0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 158.40
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 370.40
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 651.73
    else:
        return base_calculo * 0.275 - 884.96

# Função para calcular o décimo terceiro salário
def calcular_13_salario(data_admissao, data_demissao, salario_mensal):
    # Converter as datas para o formato datetime
    data_admissao = datetime.datetime.strptime(data_admissao, "%d-%m-%Y")
    data_demissao = datetime.datetime.strptime(data_demissao, "%d-%m-%Y")

    # Calcular o número de meses trabalhados
    meses_trabalhados = (data_demissao.year - data_admissao.year) * 12 + (data_demissao.month - data_admissao.month)

    # Verificar se o último mês foi trabalhado por mais de 15 dias
    if data_demissao.day > 15:
        meses_trabalhados += 1

    # Calcular o décimo terceiro salário proporcional
    if meses_trabalhados < 12:
        # Se o período de trabalho for inferior a 12 meses, calcular a fração do último ano
        frac_ultimo_ano = (12 - data_admissao.month + 1) / 12
        decimo_terceiro_proporcional = salario_mensal * frac_ultimo_ano
    else:
        # Se o período de trabalho for igual ou superior a 12 meses, calcular o valor total
        decimo_terceiro_proporcional = salario_mensal / 3  # 1/3 do salário para cada mês do último trimestre

    # Calcular o décimo terceiro salário indenizado (caso de demissão)
    decimo_terceiro_indenizado = salario_mensal / 12

    # Calcular os descontos de INSS e IRRF sobre o décimo terceiro proporcional
    desconto_inss_proporcional = calcular_inss(decimo_terceiro_proporcional)
    desconto_irrf_proporcional = calcular_irrf(decimo_terceiro_proporcional)

    # Calcular o total bruto, descontos e líquido
    total_bruto = decimo_terceiro_proporcional + decimo_terceiro_indenizado
    total_descontos = desconto_inss_proporcional + desconto_irrf_proporcional
    total_liquido = total_bruto - total_descontos

    # Definir a proporção trabalhada somente se o décimo terceiro for proporcional ao tempo trabalhado
    proporcao_trabalhada = f"{meses_trabalhados}/12" if meses_trabalhados < 12 else ""

    # Definir a proporção indenizada somente se o décimo terceiro for indenizado
    proporcao_indenizada = "1/12" if meses_trabalhados < 12 else ""

    return {
        "13º Salário Proporcional": round(decimo_terceiro_proporcional, 2),
        "Proporção Trabalhada": proporcao_trabalhada,
        "Desconto INSS sobre 13º Salário Proporcional": round(desconto_inss_proporcional, 2),
        "Desconto IRRF sobre 13º Salário Proporcional": round(desconto_irrf_proporcional, 2),
        "13º Salário Indenizado": round(decimo_terceiro_indenizado, 2),
        "Proporção Indenizada": proporcao_indenizada,
        "Desconto INSS sobre 13º Salário Indenizado": 0,
        "Desconto IRRF sobre 13º Salário Indenizado": 0,
        "Total Bruto 13º Salário": round(total_bruto, 2),
        "Total dos Descontos sobre o 13º Salário": round(total_descontos, 2),
        "Total Líquido 13º Salário": round(total_liquido, 2)
    }

# Solicitar dados do usuário
data_admissao = input("Informe a data de admissão (DD-MM-AAAA): ")
data_demissao = input("Informe a data de demissão (DD-MM-AAAA): ")
salario_mensal = float(input("Informe o salário base mensal em reais: "))

# Calcular 13º salário
resultado = calcular_13_salario(data_admissao, data_demissao, salario_mensal)

# Exibir resultados
print("\nCálculo detalhado do 13º Salário:")
for chave, valor in resultado.items():
    print(f"{chave}: R$ {valor}")

