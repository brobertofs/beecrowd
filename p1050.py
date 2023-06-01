'''
Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD
pertence, considerando a tabela abaixo:

DDD | Destination
61      Brasilia
71      Salvador
11      São Paulo
21      Rio de Janeiro
32      Juiz de Fora
19      Campinas
27      Vitoria
31      Belo Horizonte

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

Entrada
A entrada consiste de um único valor inteiro.

Saída
Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD
correspondente ao número digitado.
'''
DDD = int(input())

if DDD == 61:
    print ("Brasilia")
elif DDD==71:
    print ("Salvador")
elif DDD==11:
    print ("Sao Paulo")
elif DDD==21:
    print ("Rio de Janeiro")
elif DDD==32:
    print ("Juiz de Fora")
elif DDD==19:
    print ("Campinas")
elif DDD==27:
    print ("Vitoria")
elif DDD==31:
    print ("Belo Horizonte")
else:
    print ("DDD nao cadastrado")