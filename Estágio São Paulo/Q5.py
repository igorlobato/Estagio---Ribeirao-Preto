#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

palavra_invertida = ""
print("Caso queira encerrar o programa digite 0\n")
while True:
    palavra = input("Digite uma palavra que irei a inverter: ")
    if palavra == '0':
        break
    else:
        for i in range(len(palavra) -1, -1, -1):
            palavra_invertida += palavra[i]
        print(f"\n{palavra_invertida}\n")
        palavra_invertida = ""
    
        