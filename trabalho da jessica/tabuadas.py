def tabuada():
    
    print("O código a seguir irá calcular a tabuada do 7.");
    
    while(True):
        tabuada = int(0)
        
        tabuada = int(input("Digite o valor da tabuada(ou digite [0] para encerrar):\n"));
        
        x = 1
        
        if(tabuada == 0):
            print("O codigo sera encerrado\nObriga pela preferencia...");
            break
    
        while(x <= 10):
            resultado = (x * tabuada);
            print(f"{x} X {tabuada} = {resultado}");
            x += 1

if __name__ == "__main__":
    tabuada()