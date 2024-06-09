def somaContinua():
    soma = 0
    quantidade_numeros = 0

    while(True):
        numero_soma = int(input("Digite os valores que serão somados e digite 0 para somar tudo: "));

        if (numero_soma == 0):
            print(f"A soma dos números é:{soma}");
            print(f"A quantidade de números informados (excluindo 0) é:{quantidade_numeros}");
            break
        
        soma += numero_soma
        quantidade_numeros += 1
        
    
if __name__ == "__main__":
    somaContinua()