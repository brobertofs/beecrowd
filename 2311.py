'''
No jogo O Bruxo, Sigismund Dijkstra é o líder do Serviço Secreto Redaniano, por causa disso ele é uma das pessoas mais
importantes do mundo.

Além disso Dijkstra possui um grande tesouro, o qual possui diversos tipos de jóias.

Dijkstra está muito curioso para saber quantos tipos de jóias diferentes seu tesouro possui.

Sabendo que você é o melhor programador do continente Dijkstra te contratou para verificar quantos tipos de jóias
distintas ele tem em seu tesouro.

Entrada
A entrada consiste de várias linhas e cada uma contém uma string que descreve uma das jóias de Dijkstra. Essa string é
composta apenas dos caracteres '(' e ')', a soma do tamanho de todas as string não excede 106.

Saída
Imprima quantos tipos de jóias distintas Dijkstra tem.
'''

n = int(input())
for i in range(n):
    nome = input()
    gd = float(input())
    notas = [float(x) for x in input().split()]
    #pode usar um if com um for pra destronchar
    media = sum(sorted(notas)[1:6]) * gd
    print('%s %.2f' % (nome, media))

'''
#include <stdio.h>

int main()
{
    int tst, i, j;
    char name[1000];
    double dif, score;
    scanf("%d", &tst);
    for(i=1; i<=tst; i++)
    {
        double max = -10.00, min = 100.00, ans = 0.00;
        scanf("%s", name);
        scanf("%lf", &dif);
        for(j=1; j<=7; j++)
        {
            scanf("%lf", &score);
            if(score > max) max = score;
            if(score < min) min = score;
            ans += score;
        }
        ans -= (max+min);
        ans *= dif;
        printf("%s %.2lf\n", name, ans);
    }
    return 0;
}
'''