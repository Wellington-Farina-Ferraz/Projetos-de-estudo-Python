def fatorial(n):
    fat = 1
    while (n >1):
        fat = fat * n
        n = n - 1
    return fat
    
def testa_fatorial():
    if fatorial(1) == 1:
        print("funciona para 1")
    else:
        print("funciona para 1")
    if fatorial(2) == 2:
        print("funciona para 2")
    else:
        print("funciona para 2")
    if fatorial(0) == 1:
        print("funciona para 0")
    else:
        print("funciona para 0")
    if fatorial(5) == 120:
        print("funciona para 5")
    else:
        print("funciona para 5")
            