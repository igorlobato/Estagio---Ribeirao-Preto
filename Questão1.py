#1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente 
# definido no código;

def nFibonacci(n):
    a, b = 0, 1
    if n == 0 or n==1:
        return True
    while b < n:
        a, b = b, a + b
    return b == n

def main():
    print("Caso queira encerrar o programa digite 0")
    while True:
        try:
            n = int(input("Digite um número e direi se ele é um número de Fibonacci: "))
            if nFibonacci(n):
                print(f"O número {n} pertence a sequência de Fibonacci!")
            else:
                print(f"O número {n} não pertence a sequência de Fibonacci!")
            if n == 0:
                print("Programa encerrado.")
                break
        except ValueError:
            print("Erro! Digite um número inteiro válido.")

if __name__ == "__main__":
    main()