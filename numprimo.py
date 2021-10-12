n = int(input("Digite um número inteiro: "))

cont = 2
Primo = True

while (cont < n and Primo):

    Primo = not ((n % cont) == 0)
    cont += 1
    
    if (Primo):
        print("primo")
    else:
        n -= 1