def soma(num1, num2):
    
    
    while(num1 % 2 or num2 % 2):
        print("Pelo menos um dos números digitados não é par. Por favor, digite novamente.")
        num1 = int(input("Digite o valor do primeiro número:\n"))
        num2 = int(input("Digite o valor do segundo número:\n"))
    
    resultado = num1 + num2
    print(f"A soma dos dois números pares foi: {resultado}")

if __name__ == "__main__":
    num1 = int(input("Digite o valor do primeiro número:\n"))
    num2 = int(input("Digite o valor do segundo número:\n"))
    soma(num1, num2)