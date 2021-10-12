def get_primes(count):
    result = []
    x=2
    while len(result) in range(count):
        i=2
        flag=0
        for i in range(2,x):
            if x%i == 0:
                flag+=1
                break
            i=i+1
        if flag == 0:
            result.append(x)
        x+=1
    pass
    return result