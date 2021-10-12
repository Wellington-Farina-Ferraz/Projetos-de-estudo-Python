numero1 = int (input("Digite o numero1: "))
numero2 = int (input("Digite o numero2: "))
numero3 = int (input("Digite o numero3: "))

if (numero1 < numero2) and (numero1 < numero3) and (numero2 < numero3):
    print("crescente")
    
else:
    print("não está em ordem crescente")