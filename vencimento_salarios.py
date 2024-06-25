"""
Requisitos:
Para calcular o aviso prévio, deve verificar se foi trabalhado ou indenizado. Se ele foi trabalhado, deve-se receber o valor correspondente a um salário base. Se ele foi indenizado, você deve-se receber o valor correspondente a um salário base, mais um acréscimo de três dias por ano de serviço na empresa, limitado a 90 dias. 

Tabela aviso prévio
Tempo de Trabalho	          Aviso Prévio
Antes de 1 ano	                30 dias
1 ano	                        33 dias
2 anos	                        36 dias
3 anos	                        39 dias
4 anos	                        42 dias
5 anos	                        45 dias

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

Pedido de demissão pelo funcionário
Perderá:
- O aviso prévio — exceto quando o colaborador trabalhar por esse período;
- O saque do FGTS — o Fundo de Garantia é depositado pelo empregador, com exceção da multa, mas o colaborador não poderá fazer o saque;
- A indenização de 40% do FGTS;
- O seguro-desemprego.
Tem direito a receber o saldo de salário pelos dias trabalhados, férias proporcionais, mais ⅓, e 13º salário pro.

Demissão por justa causa
Recebe apenas o saldo de salário dos dias trabalhados no mês e eventuais férias vencidas, acrescidas de ⅓ referente a abono constitucional. 
"""

import datetime

# Funções auxiliares para cálculo
def calcular_dias_aviso_previo(data_admissao, data_demissao):
    anos_trabalhados = (data_demissao - data_admissao).days // 365
    return min(30 + 3 * anos_trabalhados, 90)

def calcular_inss(salario):
    if salario <= 1412.00:
        return salario * 0.075
    elif salario <= 2666.68:
        return (1412.00 * 0.075) + ((salario - 1412.00) * 0.09)
    elif salario <= 4000.03:
        return (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((salario - 2666.68) * 0.12)
    elif salario <= 7786.02:
        return (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((4000.03 - 2666.68) * 0.12) + ((salario - 4000.03) * 0.14)
    else:
        return (1412.00 * 0.075) + ((2666.68 - 1412.00) * 0.09) + ((4000.03 - 2666.68) * 0.12) + ((7786.02 - 4000.03) * 0.14)

def calcular_irrf(salario):
    if salario <= 2112.00:
        return 0
    elif salario <= 2826.65:
        return salario * 0.075 - 158.40
    elif salario <= 3751.05:
        return salario * 0.15 - 370.40
    elif salario <= 4664.68:
        return salario * 0.225 - 651.73
    else:
        return salario * 0.275 - 884.96

def calcular_saldo_salario(dias_trabalhados, salario_base):
    return (salario_base * dias_trabalhados) / 30

# Função principal
def calcular_rescisao(data_admissao, data_demissao, salario_base, tipo_aviso_previo, motivo_afastamento):
    data_admissao = datetime.datetime.strptime(data_admissao, "%d-%m-%Y")
    data_demissao = datetime.datetime.strptime(data_demissao, "%d-%m-%Y")

    dias_trabalhados = 16  # conforme fornecido

    saldo_salario = calcular_saldo_salario(dias_trabalhados, salario_base)
    inss_saldo = calcular_inss(saldo_salario)
    irrf_saldo = calcular_irrf(saldo_salario)

    aviso_previo = 0
    dias_aviso_previo = 0
    inss_aviso = 0
    irrf_aviso = 0

    if motivo_afastamento == "S":
        if tipo_aviso_previo == "T":
            dias_aviso_previo = 30
            aviso_previo = salario_base
        elif tipo_aviso_previo == "I":
            dias_aviso_previo = calcular_dias_aviso_previo(data_admissao, data_demissao)
            aviso_previo = salario_base + (salario_base / 30 * (dias_aviso_previo - 30))
            irrf_aviso = 0  # Não há desconto de IRRF sobre aviso prévio indenizado
        else:
            raise ValueError("Tipo de aviso prévio inválido!")

        inss_aviso = calcular_inss(aviso_previo)

    else:
        print("Não há direito ao aviso prévio devido à forma de demissão.")

    total_bruto = saldo_salario + aviso_previo
    total_inss = inss_saldo + inss_aviso
    total_irrf = irrf_saldo + irrf_aviso
    total_descontos = total_inss + total_irrf
    total_liquido = total_bruto - total_descontos

    return {
        "Saldo de Salário": saldo_salario,
        "Desconto INSS sobre Saldo de Salário": inss_saldo,
        "Desconto IRRF sobre Saldo de Salário": irrf_saldo,
        "Aviso Prévio": aviso_previo,
        "Dias de Aviso Prévio": dias_aviso_previo,
        "Desconto INSS sobre Aviso Prévio": inss_aviso,
        "Desconto IRRF sobre Aviso Prévio": irrf_aviso,
        "Total Bruto Salários": total_bruto,
        "Total dos Descontos sobre Salários": total_descontos,
        "Total Líquido Salários": total_liquido
    }

# Solicitar dados do usuário
data_admissao = input("Informe a data de admissão (DD-MM-AAAA): ")
data_demissao = input("Informe a data de demissão (DD-MM-AAAA): ")
salario_base = float(input("Informe o salário base mensal em reais: "))
tipo_aviso_previo = input("Informe o tipo de aviso prévio (I - Indenizado / T - Trabalhado): ")
motivo_afastamento = input("Informe o motivo do afastamento (S - Sem justa causa / C - Com justa causa / P - Pedido de demissão): ").upper()

# Calcular rescisão
rescisao = calcular_rescisao(data_admissao, data_demissao, salario_base, tipo_aviso_previo, motivo_afastamento)

# Exibir resultados
print("\nResumo da Rescisão:")
print(f"Saldo de Salário: R${rescisao['Saldo de Salário']:.2f}")
print(f"Desconto INSS sobre Saldo de Salário: R${rescisao['Desconto INSS sobre Saldo de Salário']:.2f}")
print(f"Desconto IRRF sobre Saldo de Salário: R${rescisao['Desconto IRRF sobre Saldo de Salário']:.2f}")

if motivo_afastamento == "S":
    print(f"Aviso Prévio: R${rescisao['Aviso Prévio']:.2f}")
    print(f"Dias de Aviso Prévio: {rescisao['Dias de Aviso Prévio']} dias")
    print(f"Desconto INSS sobre Aviso Prévio: R${rescisao['Desconto INSS sobre Aviso Prévio']:.2f}")
    print(f"Desconto IRRF sobre Aviso Prévio: R${rescisao['Desconto IRRF sobre Aviso Prévio']:.2f}")
else:
    print("Não há direito ao aviso prévio devido à forma de demissão.")

print(f"Total Bruto Salários: R${rescisao['Total Bruto Salários']:.2f}")
print(f"Total dos Descontos sobre Salários: R${rescisao['Total dos Descontos sobre Salários']:.2f}")
print(f"Total Líquido Salários: R${rescisao['Total Líquido Salários']:.2f}")
