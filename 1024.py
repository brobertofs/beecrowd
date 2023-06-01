'''
Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar
mensagens codificadas sem que alguém consiga lê-las. O processo é muito simples. São feitas três passadas em todo o
texto.
Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a
direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim
sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer
caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII.
Neste caso, 'b' vira 'a' e 'a' vira '`'.
Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”.
O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos
caracteres da metade em diante, o resultado final deve ser “3# rvzgV”.
Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*104),
indicando a quantidade de linhas que o problema deve tratar. As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103)
caracteres.
Saída
Para cada entrada, deve-se apresentar a mensagem criptografada.
'''

from math import ceil

n = int(input())
while n > 0:
    n -= 1
    msg = str(input())
    msg2 = ''
    for x in msg:
        if (x.isalpha() == True):
            msg2 += chr(ord(x) + 3)
        else:
            msg2 += x

    msg3 = msg2[::-1]
    s = ceil(len(msg3)/2)
    msg4 = msg3[-s:]
    msg5 = ''
    for y in msg4:
        msg5 += chr(ord(y) - 1)
    emsg = msg3.replace(msg4, msg5)

    print(emsg)


'''
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
    int n, size;
    string s;
    cin >> n;
    for(int i = 0; i <= n; ++i) {
        getline(cin, s);
        if(i == 0) continue;
        size = s.length();
        vector<char> v(size);
        for(int j = 0; j < size; ++j){ v[j] = s[j]; }
        for(int j = 0; j < size; ++j){
            if((v[j] >= 'a' && v[j] <= 'z') || (v[j] >= 'A' && v[j] <= 'Z'))
                v[j] = v[j] + 3;
        }
        reverse(v.begin(), v.begin() + size);
        for(int j = (size/2); j < size; ++j){ v[j] = v[j] - 1; }
        for(int j = 0; j < (size/2); ++j){ cout << v[j]; }
        for(int j = (size/2); j < size; ++j){ cout << v[j]; }
        cout << endl;
    }
    return 0;
}
'''