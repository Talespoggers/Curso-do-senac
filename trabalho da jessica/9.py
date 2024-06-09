def idade():
    idade = int(input("Digite a idade do primeiro aluno: "));
    print("----------------------------------------------");
    menor_idade = idade
    contador = 1

    while(contador < 10):
        idade = int(input("Digite a idade do próximo aluno: "));
        contador += 1
        print(f"Já registrou {contador} alunos(as).");
        print("----------------------------------------------");
        
        if(idade < menor_idade):
            menor_idade = idade
            
    print("----------------------------------------------");
    print(f"|A menor idade entre os alunos é: {menor_idade}|");
    print("----------------------------------------------");
    
if __name__ == "__main__":
    idade()