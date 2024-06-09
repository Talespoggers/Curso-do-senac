def contar_sexo_idade():
    masculino = 0
    feminino = 0
    total_pessoas = 0

    while(total_pessoas < 10):
        print(f"Pessoa {total_pessoas + 1}:");
        idade = int(input("Digite a idade da pessoa:\n"));
        sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino):\n");

        if(sexo == 'M' or sexo == 'm'):
            masculino += 1
        elif(sexo == 'F' or sexo == 'f'):
            feminino += 1
        else:
            print("Sexo inválido. Por favor, insira M para masculino ou F para feminino.");

        total_pessoas += 1

    print(f"\nTotal de pessoas masculinas: {masculino} ({(masculino / total_pessoas) * 100:.2f}%)");
    print(f"\nTotal de pessoas femininas: {feminino} ({(feminino / total_pessoas) * 100:.2f}%)");

if __name__ == "__main__":
    contar_sexo_idade()
