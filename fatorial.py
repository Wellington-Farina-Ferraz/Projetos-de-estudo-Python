n = int(input("Digite o valor n: "))
i     = 1  # contador
n_fat = 1  

while i <= n:
    n_fat = n_fat * i 
    i = i + 1

print(n_fat)