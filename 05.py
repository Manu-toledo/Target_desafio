# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

print('-'*55)
print('Invertendo Strings')
print('-'*55)

palavraCerta = str(input('Digite uma palavra que deseje saber o inverso dela:'))

palavraInversa = palavraCerta[::-1]

print(f'O inverso da palavra {palavraCerta} é {palavraInversa}.')