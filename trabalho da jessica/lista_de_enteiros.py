def lista():

    inicio = int(0);
    final = int(0);

    print("Descubra quais numeros estão entro os que voce escolher!!");

    valor1 = int(input("Informe o Primeiro valor:\n"))
    valor2 = int(input("Informe o Segundo valor:\n"))

    inicio = min(valor1, valor2);
    final = max(valor1, valor2);

    print(f"Os numeros escolhidos para ser listados foram:\n{inicio}  e {final}");
    
    while(inicio <= final):
        print(inicio, end=" ");
        inicio += 1

if __name__ == "__main__":
    lista()