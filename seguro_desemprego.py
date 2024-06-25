"""
Requisitos:
O valor do benefício não poderá ser inferior ao valor do Salário Mínimo

1ª solicitação; pelo menos 12 (doze) meses nos últimos 18 (dezoito) meses imediatamente anteriores à data de dispensa, quando da primeira solicitação;

2ª solicitação; pelo menos 9 (nove) meses nos últimos 12 (doze) meses; imediatamente anteriores à data de dispensa, quando da segunda solicitação;

3ª solicitação; cada um dos 6 (seis) meses imediatamente anteriores à data de dispensa, quando das demais solicitações.

Para primeira solicitação
O trabalhador terá direito a 4 parcelas se comprovar vínculo empregatício com pessoa jurídica ou pessoa física a ela equiparada de, no mínimo 12 (doze) meses e, no máximo, 23(vinte e três) meses, no período de referência; ou
O trabalhador terá direito a 5 parcelas se comprovar vínculo empregatício com pessoa jurídica ou pessoa física a ela equiparada de, no mínimo, 24(vinte e quatro) meses, no período de referência.

Para segunda solicitação
O trabalhador terá direito a 3 parcelas se comprovar vínculo empregatício com pessoa jurídica ou pessoa física a ela equiparada de, no mínimo 9 (nove) meses e, no máximo, 11(meses) meses, no período de referência; ou
O trabalhador terá direito a 4 parcelas se comprovar vínculo empregatício com pessoa jurídica ou pessoa física a ela equiparada de, no mínimo 12 (doze) meses e, no máximo, 23(vinte e três) meses, no período de referência; ou
O trabalhador terá direito a 5 parcelas se comprovar vínculo empregatício com pessoa jurídica ou pessoa física a ela equiparada de, no mínimo, 24(vinte e quatro) meses, no período de referência.

Para terceira solicitação
O trabalhador terá direito a 3 parcelas se comprovar vínculo empregatício com pessoa jurídica ou pessoa física a ela equiparada de, no mínimo 6 (seis) meses e, no máximo, 11(meses) meses, no período de referência; ou
O trabalhador terá direito a 4 parcelas se comprovar vínculo empregatício com pessoa jurídica ou pessoa física a ela equiparada de, no mínimo 12 (doze) meses e, no máximo, 23(vinte e três) meses, no período de referência; ou
O trabalhador terá direito a 5 parcelas se comprovar vínculo empregatício com pessoa jurídica ou pessoa física a ela equiparada de, no mínimo, 24(vinte e quatro) meses, no período de referência.

Efetuar a média dos 3 últimos salários
Até R$ 2.041,39 multiplica-se salário médio por 0,80 ( 80% )
De R$ 2.041,40 até R$ 3.402,65 o que exceder a R$ 2.041,39 multiplica-se por 0,5 e soma-se com R$ 1.633,10
Acima de R$ 3.402,65 o valor da parcela será de R$ 2.313,74

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

def calcular_meses_trabalhados(data_admissao, data_demissao):
    data_admissao = datetime.strptime(data_admissao, '%d-%m-%Y')
    data_demissao = datetime.strptime(data_demissao, '%d-%m-%Y')
    meses = (data_demissao.year - data_admissao.year) * 12 + data_demissao.month - data_admissao.month
    if data_demissao.day >= data_admissao.day:
        meses += 1
    return meses

def calcular_numero_parcelas(meses_trabalhados, solicitacao):
    if solicitacao == 1:
        if meses_trabalhados >= 12:
            return 5
        elif meses_trabalhados >= 9:
            return 4
    elif solicitacao == 2:
        if meses_trabalhados >= 9:
            return 5
    elif solicitacao == 3:
        if 6 <= meses_trabalhados <= 11:
            return 3
        elif 12 <= meses_trabalhados <= 23:
            return 4
        elif meses_trabalhados >= 24:
            return 5
    return 0

def calcular_seguro_desemprego(salario1, salario2, salario3, data_admissao, data_demissao, solicitacao, motivo_afastamento):
    if motivo_afastamento in ['C', 'P']:
        return "Não terá direito ao seguro-desemprego devido ao tipo de demissão."
    
    meses_trabalhados = calcular_meses_trabalhados(data_admissao, data_demissao)
    if not verificar_direito(meses_trabalhados, solicitacao):
        return "Sem direito ao seguro. Deve ter trabalhado pelo menos os meses necessários de acordo com a solicitação."
    
    salarios = [salario1, salario2, salario3]
    media_salarial = sum(salarios) / len(salarios)
    if media_salarial <= 2041.39:
        valor_parcela = media_salarial * 0.8
    elif 2041.40 <= media_salarial <= 3402.65:
        valor_parcela = 1633.10 + ((media_salarial - 2041.39) * 0.5)
    else:
        valor_parcela = 2313.74
    
    numero_parcelas = calcular_numero_parcelas(meses_trabalhados, solicitacao)
    
    valor_total = valor_parcela * numero_parcelas
    
    return {
        "Quantidade de Meses Trabalhados": meses_trabalhados,
        "Média dos Três Últimos Salários": round(media_salarial, 2),
        "Quantidade de Parcelas": numero_parcelas,
        "Valor por Parcela": round(valor_parcela, 2),
        "Valor Total das Parcelas": round(valor_total, 2)
    }

def verificar_direito(meses_trabalhados, solicitacao):
    if solicitacao == 1:
        return meses_trabalhados >= 12
    elif solicitacao == 2:
        return meses_trabalhados >= 9
    elif solicitacao == 3:
        return True
    return False

# Exemplo de uso
salario1 = float(input("Informe o valor do primeiro salário: "))
salario2 = float(input("Informe o valor do segundo salário: "))
salario3 = float(input("Informe o valor do terceiro salário: "))
data_admissao = input("Informe a data de admissão (DD-MM-AAAA): ")
data_demissao = input("Informe a data de demissão (DD-MM-AAAA): ")
solicitacao = int(input("Informe o número da solicitação (1, 2 ou 3): "))
motivo_afastamento = input("Informe o motivo do afastamento (S - Sem justa causa / C - Com justa causa / P - Pedido de demissão): ").upper()

# Calcular seguro-desemprego
resultado = calcular_seguro_desemprego(salario1, salario2, salario3, data_admissao, data_demissao, solicitacao, motivo_afastamento)

if isinstance(resultado, str):
    print(resultado)
else:
    print("Cálculo do Seguro Desemprego:")
    for chave, valor in resultado.items():
        print(f"{chave}: {valor}")
