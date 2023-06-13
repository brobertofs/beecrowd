nome = input()
salario = float(input())
total_vendas = float(input())
comissao = total_vendas * 0.15
salario_total = salario + comissao
print ("TOTAL = R$ %.2f" %salario_total)
