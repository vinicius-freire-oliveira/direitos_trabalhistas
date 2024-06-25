def calcular_desconto_dias_falta(salario_bruto, dias_falta):
    # Calcula o valor diário do salário
    valor_diario = salario_bruto / 30
    
    # Calcula o desconto por falta
    desconto_falta = valor_diario * dias_falta
    
    # Calcula o salário restante após o desconto
    salario_restante = salario_bruto - desconto_falta
    
    return round(desconto_falta, 2), round(salario_restante, 2)

# Exemplo de uso
salario_bruto = float(input("Informe o salário bruto: "))
dias_falta = int(input("Informe o número de dias de falta: "))

desconto, salario_restante = calcular_desconto_dias_falta(salario_bruto, dias_falta)

print(f"Desconto por {dias_falta} dia(s) de falta: R$ {desconto}")
print(f"Salário restante após desconto: R$ {salario_restante}")
