def tabuada():
    print("O código a seguir irá calcular a tabuada do 7.");

    tabuada = 7

    x = 1

    while(x <= 10):
        resultado = (x * tabuada);
        print(f"{x} X {tabuada} = {resultado}");
        x += 1

if __name__ == "__main__":
    tabuada()
