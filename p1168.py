'''
João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza se
conseguirá montar o número desejado. Considerando a configuração dos leds dos números abaixo, faça um algoritmo que
ajude João a descobrir a quantidade de leds necessário para montar o valor.

acessar: https://www.beecrowd.com.br/judge/pt/problems/view/1168

Obs.: Para programadores de Javascript, recomenda-se o uso de "input.trim().split('\n')" para evitar erros conhecidos.

Entrada
A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste, seguido de N linhas, cada
linha contendo um número (1 ≤ V ≤ 10^100) correspondente ao valor que João quer montar com os leds.

Saída
Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para montar o valor desejado,
seguido da palavra "leds".
'''
n = int(input())

for l in range(n):
    leds = 0
    num = input() #string
    for i in range(0, len(num)):
        try:
            if num[i] == '0': leds += 6;
            if num[i] == '1': leds += 2;
            if num[i] == '2': leds += 5;
            if num[i] == '3': leds += 5;
            if num[i] == '4': leds += 4;
            if num[i] == '5': leds += 5;
            if num[i] == '6': leds += 6;
            if num[i] == '7': leds += 3;
            if num[i] == '8': leds += 7;
            if num[i] == '9': leds += 6;
        except EOFError as e:
            print(e)

    print("%d leds" %int(leds))

'''   
# include <stdio.h>
int
main() {
    int n, j;
    char num[101];
    long long leds;

    scanf("%d", & n);

    for (int i = 0; i < n; i++)
    {
        scanf("%s", & num);
        j = 0;
        leds = 0;
        while (true){
            if (num[j] == '') break;
            if (num[j] == '1') leds += 2;
            if (num[j] == '2') leds += 5;
            if (num[j] == '3') leds += 5;
            if (num[j] == '4') leds += 4;
            if (num[j] == '5') leds += 5;
            if (num[j] == '6') leds += 6;
            if (num[j] == '7') leds += 3;
            if (num[j] == '8') leds += 7;
            if (num[j] == '9') leds += 6;
            if (num[j] == '0') leds += 6;
            j++;
        }
        printf("%lld ledsn", leds);
    }
return 0;
}
'''