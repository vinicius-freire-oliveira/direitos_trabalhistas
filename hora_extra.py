"""
Requisitos:
- Valor da hora base: salário bruto/220
- Adicional de hora extra diurna: 50% = valor da hora base * 1.5
- Adicional de hora extra noturna: 20% = valor da hora base * 1.2
- Hora noturna: 52 minutos e 30 segundos
- Adicional de hora extra noturna: 20% sobre a hora extra diurna = valor da hora extra diurna * 1.2
- Valor da hora extra domingos e feriados - 100%
- Limite diário de horas extras: 2 horas
- Carga horária semanal: Máximo de 44 horas
- Carga horária mensal: Máximo de 220 horas
- Limite diário de hora extra = 2 horas
"""

def calcular_horas_extras(salario_bruto, carga_horaria_mensal, horas_extras_diurnas, horas_extras_noturnas, horas_extras_100):
    # Verifica se a carga horária mensal ultrapassa o limite de 220 horas
    if carga_horaria_mensal > 220:
        return "Erro: A carga horária mensal ultrapassa o limite de 220 horas."
    
    # Verifica se a carga horária semanal ultrapassa o limite de 44 horas
    if carga_horaria_mensal / 5 > 44:
        return "Erro: A carga horária semanal ultrapassa o limite de 44 horas."
    
    # Calcula o valor da hora base
    valor_por_hora = salario_bruto / 220
    
    # Calcula o valor da hora extra diurna (50% adicional)
    valor_hora_extra_diurna = valor_por_hora * 1.5
    
    # Calcula o valor da hora extra noturna (20% adicional sobre a hora base)
    valor_hora_extra_noturna = valor_por_hora * 1.2
    
    # Calcula o adicional da hora extra noturna (20% sobre a hora extra diurna)
    adicional_hora_extra_noturna = valor_hora_extra_diurna * 1.2
    
    # Considera a hora noturna como 52 minutos e 30 segundos
    fator_hora_noturna = 52.5 / 60
    
    # Calcula o total de horas extras diurnas
    total_horas_extras_diurnas = horas_extras_diurnas * valor_hora_extra_diurna
    
    # Calcula o total de horas extras noturnas (ajustado pelo fator de hora noturna)
    total_horas_extras_noturnas = horas_extras_noturnas * adicional_hora_extra_noturna * fator_hora_noturna
    
    # Calcula o total de horas extras em dias especiais (100% adicional)
    total_horas_extras_100 = horas_extras_100 * (valor_por_hora * 2)
    
    # Soma do salário bruto com as horas extras
    salario_total = salario_bruto + total_horas_extras_diurnas + total_horas_extras_noturnas + total_horas_extras_100
    
    return {
        "Valor por Hora": round(valor_por_hora, 2),
        "Valor da Hora Extra Diurna": round(valor_hora_extra_diurna, 2),
        "Valor da Hora Extra Noturna": round(valor_hora_extra_noturna, 2),
        "Valor da Hora Extra Domingos e Feriados (100%)": round(valor_por_hora * 2, 2),
        "Total Horas Extras Diurnas": round(total_horas_extras_diurnas, 2),
        "Total Horas Extras Noturnas": round(total_horas_extras_noturnas, 2),
        "Total Horas Extras 100%": round(total_horas_extras_100, 2),
        "Salário Total": round(salario_total, 2)
    }

# Exemplo de uso
salario_bruto = float(input("Informe o salário bruto: "))
carga_horaria_mensal = int(input("Informe a carga horária mensal: "))
horas_extras_diurnas = int(input("Informe o total de horas extras diurnas: "))
horas_extras_noturnas = int(input("Informe o total de horas extras noturnas: "))
horas_extras_100 = int(input("Informe o total de horas extras em dias especiais (domingos, feriados e folgas): "))

resultado = calcular_horas_extras(salario_bruto, carga_horaria_mensal, horas_extras_diurnas, horas_extras_noturnas, horas_extras_100)

if isinstance(resultado, str):
    print(resultado)
else:
    print("Resultado:")
    for chave, valor in resultado.items():
        print(f"{chave}: R$ {valor}")
