import controllers.function_controller as fc

def main():
    while True:
        command = input("").lower().split()
        try:
            if "dd" == command[0]:
                fc.DD(command[1])
            elif "rc" == command[0]:
                i = 2
                commandAux = []
                for i in range(2,len(command)):
                    commands = "".join(command[i])
                    commandAux.append(commands)
                commando = listToString(commandAux)
                fc.RC(command[1],commando)
            elif "rp" == command[0]:
                i = 1
                commandAux = []
                for i in range(1,len(command)):
                    commands = "".join(command[i])
                    commandAux.append(commands)
                commando = listToString(commandAux)
                fc.RP(commando)
            elif "rs" == command[0]:
                i = 1
                commandAux = []
                for i in range(1,len(command)):
                    commands = "".join(command[i])
                    commandAux.append(commands)
                commando = listToString(commandAux)
                fc.RS(commando)
            elif "re" == command[0]:
                i = 4
                commandAux = []
                for i in range(4,len(command)):
                    commands = "".join(command[i])
                    commandAux.append(commands)
                commando = listToString(commandAux)
                fc.RE(command[1],command[2],command[3],commando)
            elif "ap" == command[0]:
                fc.AP(command[1],command[2])
            elif "cp" == command[0]:
                fc.CP(command[1])
            elif "af" == command[0]:
                fc.AF(command[1],command[2])
            elif "df" == command[0]:
                fc.DF(command[1])
            elif "es" == command[0]:
                fc.ES(command[1],command[2],command[3])
            elif "ec" == command[0]:
                fc.EC(command[1])
            elif "lp" == command[0]:
                fc.LP()
            elif "lf" == command[0]:
                fc.LF()
            elif "ls" == command[0]:
                fc.LS()
            elif "lsa" == command[0]:
                fc.LSA(command[1])
            elif "lsaf" == command[0]:
                fc.LSAF(command[1])
            elif "as" == command[0]:
                if len(command) ==5:
                    fc.AS(command[1],command[2],command[3],command[4])
                else:
                    fc.AS(command[1],command[2],command[3])
            elif "ca" == command[0]:
                fc.CA(command[1],command[2])
            else:
                print("Instrução inválida.")
        except:
            print("Instrução inválida.")

def listToString(lista):
    str1 = " "
    return (str1.join(lista))