"""
Requisitos:
Mensalmente a empresa deposita 8% sobre o salário do funcionário numa conta aberta na Caixa Econômica Federal, essa porcentagem não é descontada do trabalhador. 

Mês completo é o mês em que você trabalhou 15 dias ou mais.

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

from datetime import datetime

def calcular_meses_completos(data_admissao, data_demissao):
    data_admissao = datetime.strptime(data_admissao, '%d-%m-%Y')
    data_demissao = datetime.strptime(data_demissao, '%d-%m-%Y')

    meses_completos = 0
    mes_atual = data_admissao.month
    ano_atual = data_admissao.year

    while (ano_atual < data_demissao.year or
           (ano_atual == data_demissao.year and mes_atual <= data_demissao.month)):
        meses_completos += 1
        mes_atual += 1
        if mes_atual > 12:
            mes_atual = 1
            ano_atual += 1

    return meses_completos

def calcular_fgts(data_admissao, data_demissao, salario_bruto):
    deposito_fgts_mes = salario_bruto * 0.08
    meses_completos = calcular_meses_completos(data_admissao, data_demissao)
    saldo_fgts = meses_completos * deposito_fgts_mes
    multa_40 = saldo_fgts * 0.4
    total_fgts_com_multa = saldo_fgts + multa_40

    return deposito_fgts_mes, saldo_fgts, multa_40, total_fgts_com_multa, meses_completos

# Solicitação de dados
data_admissao = input("Informe a data de admissão (DD-MM-AAAA): ")
data_demissao = input("Informe a data de demissão (DD-MM-AAAA): ")
salario_bruto = float(input("Informe o valor do salário bruto: "))
tipo_demissao = input("Informe a forma de demissão (S-Sem justa causa/ C-Com justa causa/ P-Pedido de demissão): ").upper()

# Verificação do tipo de demissão e cálculo do FGTS
if tipo_demissao == 'S':
    deposito_fgts_mes, saldo_fgts, multa_40, total_fgts_com_multa, meses_completos = calcular_fgts(data_admissao, data_demissao, salario_bruto)

    # Exibição dos resultados
    print("Cálculo do FGTS e Multa em caso de demissão:")
    print(f"Depósito FGTS/mês (8%): R$ {deposito_fgts_mes:.2f}")
    print(f"Quantidade de meses trabalhados: {meses_completos}")
    print(f"Saldo FGTS: R$ {saldo_fgts:.2f}")
    print(f"Multa 40%: R$ {multa_40:.2f}")
    print(f"Total FGTS com 40% de multa em caso de demissão: R$ {total_fgts_com_multa:.2f}")
else:
    print("Não há direito ao FGTS devido ao tipo de demissão.")
