def algoritmo_euclides(a,b):
    aux = []
    while b!=0:
        r= a % b
        a=b
        b=r
        aux.append(r)
    return aux

#Algoritmo de euclides com o uso de recursividade
def Alg_euclides(a,b):
    return a if not b else Alg_euclides(b, a % b)