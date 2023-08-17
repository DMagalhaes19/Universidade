import math
def fatores(num):
    aux =[]
    if(num < 0):
        return "Nao e' possivel fatorizar um numero negativo"
    else:
        while (num % 2==0):
            aux.append(2)
            num = num/2
        for i in range(3,int(math.sqrt(num))+1,2):
            while(num % i == 0):    
                aux.append(i)
                num = num / i
        if(num>2):
            aux.append(num)
    return aux

