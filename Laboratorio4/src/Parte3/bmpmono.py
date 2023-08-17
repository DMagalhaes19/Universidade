# -*- coding: utf-8 -*-
import Cores.bmplib as imag

def converter_imagem(ficheiro):
    Img = imag.ler_imagem(ficheiro)
    tuplo = ()
    lst1 = []
    for idx in Img:
        lst =list(idx)
        if(lst[0] == 255 or lst[1] == 255 or lst[2] == 255):
            lst1.append(lst)
            tuplo=tuple(lst1)
        else:
            lst[0] = 0
            lst[1] = 0
            lst[2] = 0
            lst1.append(lst)
            tuplo= tuple(lst1)
            idx=tuple(lst)
    Write = imag.escrever_imagem(ficheiro, "monocromatico.bmp", tuplo)
    return Write

converter_imagem("imagem.bmp")
        
      

