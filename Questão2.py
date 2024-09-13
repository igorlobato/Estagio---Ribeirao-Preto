#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a 
# quantidade de vezes em que ela ocorre.

# Ops: A letra ã foi considerada diferente de A e a, pois não foi especificado na questão se ela deveria ser considerada ou não.

def verificarA(string):
    qtd = string.lower().count('a')
    if qtd > 0:
        print(f"A letra 'A' aparece {qtd} vezes. \n")
    else:
        print("A letra 'A' não aparece nenhuma vez na String \n")


def main():
    print("Caso queira encerrar o programa digite 0 \n")
    while True:
        string = input("Digite um texto e direi quantas vezes a letra A aparece! \n")
        verificarA(string)
        if string == '0':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()