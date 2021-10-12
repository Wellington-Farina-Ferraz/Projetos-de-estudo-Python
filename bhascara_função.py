import math

def formula():

    a = float (input("Digite o valor de a: "))
    b = float (input("Digite o valor de b: "))
    c = float (input("Digite o valor de c: "))    
    raizes(a, b, c)
    

def raizes(a, b, c):

    d = delta(a, b, c)    
    
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print("A única raiz é: ", raiz1)
        
    else:
    
        if d<0:
            print("Esta equação não possui raízes reais")
            
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print("A primeira raiz é: ", raiz1)
            print("A segunda raiz é: ", raiz2)
            
        
def delta(a, b, c):
    return b ** 2 - 4 * a * c