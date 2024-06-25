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

def calcular_ferias(data_admissao, data_demissao, salario_mensal, ferias_vencidas, dias_ferias, vender_abono):
    # Converter as datas para o formato datetime
    data_admissao = datetime.datetime.strptime(data_admissao, "%d-%m-%Y")
    data_demissao = datetime.datetime.strptime(data_demissao, "%d-%m-%Y")
    
    # Calcular meses trabalhados
    meses_trabalhados = (data_demissao.year - data_admissao.year) * 12 + (data_demissao.month - data_admissao.month)
    if data_demissao.day > 15:
        meses_trabalhados -= 1
    
    # Calcular férias vencidas e proporcionais
    valor_ferias_vencidas = salario_mensal * (ferias_vencidas == "S")
    valor_ferias_proporcionais = salario_mensal / 12 * 11
    
    # Calcular férias indenizadas
    valor_ferias_indenizadas = salario_mensal / 12
    
    # Calcular 1/3 sobre férias
    um_terco_ferias_vencidas = valor_ferias_vencidas / 3
    um_terco_ferias_proporcionais = valor_ferias_proporcionais / 3
    um_terco_ferias_indenizadas = valor_ferias_indenizadas / 3
    
    # Calcular valor do abono pecuniário
    valor_abono_pecuniario = salario_mensal * (vender_abono == "S") * (30 - dias_ferias) / 30
    um_terco_abono_pecuniario = valor_abono_pecuniario / 3
    
    # Calcular total férias
    total_ferias = valor_ferias_vencidas + um_terco_ferias_vencidas + valor_ferias_proporcionais + um_terco_ferias_proporcionais + valor_ferias_indenizadas + valor_abono_pecuniario + um_terco_ferias_indenizadas
    
    return {
        "Férias vencidas": round(valor_ferias_vencidas, 2),
        "1/3 sobre férias vencidas": round(um_terco_ferias_vencidas, 2),
        "Férias proporcionais": round(valor_ferias_proporcionais, 2),
        "1/3 sobre férias proporcionais": round(um_terco_ferias_proporcionais, 2),
        "Férias indenizadas": round(valor_ferias_indenizadas, 2),
        "1/3 sobre férias indenizadas": round(um_terco_ferias_indenizadas, 2),
        "Valor do Abono Pecuniário": round(valor_abono_pecuniario, 2),
        "1/3 sobre Abono": round(um_terco_abono_pecuniario, 2),
        "Total férias": round(total_ferias, 2)
    }

# Solicitar dados do usuário
data_admissao = input("Informe a data de admissão (DD-MM-AAAA): ")
data_demissao = input("Informe a data de demissão (DD-MM-AAAA): ")
salario_mensal = float(input("Informe o valor do salário mensal em reais: "))
ferias_vencidas = input("As férias são vencidas (S/N)? ").strip().upper()
dias_ferias = int(input("Informe a quantidade de dias de férias: "))
vender_abono = input("Deseja vender o abono pecuniário (S/N)? ").strip().upper()

# Calcular as férias
resultado_ferias = calcular_ferias(data_admissao, data_demissao, salario_mensal, ferias_vencidas, dias_ferias, vender_abono)

# Exibir resultados
print("\nCálculo das Férias:")
for chave, valor in resultado_ferias.items():
    print(f"{chave}: R$ {valor}")
