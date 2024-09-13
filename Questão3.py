#3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } 
# imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

# Problema adaptado para a linguagem python, como é possível ver ao executar o programa, o resultado do problema é 77!

def main():
    indice, soma, k = 12, 0, 1
    while k < indice:
        k = k + 1
        soma = soma + k
    print(soma)
    
if __name__ == "__main__":
    main()