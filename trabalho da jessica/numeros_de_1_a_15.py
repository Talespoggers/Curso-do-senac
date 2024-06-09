def numerosPares():
    numero = int(0);
    contador = int(0);
    soma = int(0);

    while(contador <= 15):
        if(contador % 2 == 0):
            soma += contador
            numero += 1
        contador += 1
        print(f"O numero par entre 1 e 15 é:\n {contador}")
        print(f"\nA soma dos valores é:{soma}")
        print(f"A quantidade de números pares acumulados é:{numero}")
        print("-------------------------------")
        
if __name__ == "__main__":
    numerosPares()
  

  
  