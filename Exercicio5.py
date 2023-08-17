def function(p1,p2): #exercicio 5
    num_x = p1 #numero inserido
    num_n = p2 #valor do modulo
    resto = 1 
    num_b = 1
    quociente = int((num_x * num_b)/num_n)
    num_1 = (num_x * num_b)
    num_2 = (quociente*num_n + resto)
    while num_1 != num_2 and num_b < num_n: #ciclo para verificar todos os numeros validos para ver se são o inverso do numero inserido
        num_b += 1
        quociente = int((num_x * num_b)/num_n)
        num_2 = int((quociente*num_n + resto))
        num_1 = int((num_x * num_b))
    if num_b == num_n or num_b == num_x: #verificar se existe o inverso
        num_b = "não existe inverso"
    else:
        inverso = num_b 
        num_b = "o inverso do número {} em módulo {} é: {}.". format(num_x,num_n,inverso)
    return num_b
