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

No cálculo de rescisão pedido de demissão não há direito ao Saque do FGTS e nem a multa de 40% sobre o FGTS; porém o Saldo do FGTS permanece depositado na Caixa Econômica Federal e é corrigido mensalmente.

Quem pede demissão não tem direito a solicitar o Seguro Desemprego.

Aviso prévio: deve verificar se ele foi trabalhado ou indenizado. Se ele foi trabalhado, você deve receber o valor correspondente a um salário base. Se ele foi indenizado, você deve receber o valor correspondente a um salário base, mais um acréscimo de três dias por ano de serviço na empresa, limitado a 90 dias.

Mês completo é o mês em que você trabalhou 15 dias ou mais.
"""
# Função para calcular o total bruto da rescisão
def calcular_total_bruto_rescisao(salario_liquido, decimo_terceiro_liquido, ferias):
    return salario_liquido + decimo_terceiro_liquido + ferias

# Função para calcular o total geral dos descontos
def calcular_total_geral_descontos(descontos_salarios, descontos_decimo_terceiro):
    return descontos_salarios + descontos_decimo_terceiro

# Função para calcular o total líquido da rescisão
def calcular_total_liquido_rescisao(total_bruto_rescisao, total_geral_descontos):
    return total_bruto_rescisao - total_geral_descontos

# Função para calcular o valor total (rescisão + FGTS + Seguro Desemprego)
def calcular_valor_total_rescisao(total_liquido_rescisao, total_fgts_com_multa, seguro_desemprego):
    return total_liquido_rescisao + total_fgts_com_multa + seguro_desemprego

# Dados fornecidos
salario_liquido = float(input("Informe o valor do salário líquido: "))
decimo_terceiro_liquido = float(input("Informe o valor do 13º salário líquido: "))
ferias = float(input("Informe o valor das férias: "))
total_fgts_com_multa = float(input("Informe o valor total do FGTS com 40% de multa: "))
seguro_desemprego = float(input("Informe o valor do seguro desemprego: "))
descontos_salarios = float(input("Informe o valor total dos descontos sobre salários: "))
descontos_decimo_terceiro = float(input("Informe o valor total dos descontos sobre o 13º salário: "))

# Calcula o total bruto da rescisão
total_bruto_rescisao = calcular_total_bruto_rescisao(salario_liquido, decimo_terceiro_liquido, ferias)

# Calcula o total geral dos descontos
total_geral_descontos = calcular_total_geral_descontos(descontos_salarios, descontos_decimo_terceiro)

# Calcula o total líquido da rescisão
total_liquido_rescisao = calcular_total_liquido_rescisao(total_bruto_rescisao, total_geral_descontos)

# Calcula o valor total (rescisão + FGTS + Seguro Desemprego)
valor_total_rescisao = calcular_valor_total_rescisao(total_liquido_rescisao, total_fgts_com_multa, seguro_desemprego)

# Imprime os resultados
print("Resultados:")
print(f"Total bruto da rescisão: R$ {total_bruto_rescisao:.2f}")
print(f"Total geral dos descontos: R$ {total_geral_descontos:.2f}")
print(f"Total líquido da rescisão: R$ {total_liquido_rescisao:.2f}")
print(f"Total FGTS com 40% de multa: R$ {total_fgts_com_multa:.2f}")
print(f"Seguro Desemprego: R$ {seguro_desemprego:.2f}")
print(f"Valor total (rescisão + FGTS + Seguro Desemprego): R$ {valor_total_rescisao:.2f}")
