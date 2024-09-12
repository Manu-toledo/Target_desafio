# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente 
# definido no código;


print('-'*55)
print('Sequência de Fibonacci')
print('-'*55)

num = int(input('Digite um numero inteiro de sua preferencia, ao qual deseje saber se está na sequencia Fibonacci: '))
termo1 = 0
termo2 = 1

print('~'*50)

while termo1 < num:
    novo_termo = termo1 + termo2
    termo1 = termo2
    termo2 = novo_termo


if termo1 == num:
    print(f'O numero {num} pertence a sequencia de Fibonacci')
else:
    print(f'O numero {num} NAO pertence a sequencia de Fibonacci')

print('~'*50)