import controller.function_controller as ct


arq = "game.json"
if not ct.VerifArq(arq):
    ct.CriarArq(arq)
ct.Data()
while True:
    command = input("").lower().split()
    try:
        if "rj" == command[0] and len(command) == 2:
            ct.RJ(command[1])
        elif "ej" == command[0] and len(command) == 2:
            ct.EJ(command[1])
        elif "lj" == command[0] and len(command) == 1:
            ct.LJ()
        elif "ij" == command[0] and len(command) == 3:
            values = input("")
            values = values.split()
            values2 = input("")
            values2 = values2.split()
            ct.IJ(command[1], command[2], int(values[0]), int(values[1]), int(values[2]), [int(tamanho) for tamanho in values2])
        elif "dj" == command[0] and len(command) == 1:
            ct.DJ()
        elif "d" == command[0] and len(command) in range(2, 4):
            ct.D(command[1:])
        elif "cp" == command[0] and len(command) in range(4, 6):
            ct.CP(command[1], command[2], command[3], command[4] if len(command) == 5 else None)
        elif "v" == command[0] and len(command) == 1:
            ct.V()
        elif "g" == command[0] and len(command) == 2:
            ct.Gravar(command[1])
        elif "l" == command[0] and len(command) == 2:
            ct.L(command[1])
        else:
            print("Instrução inválida.")
    except:
        print("Instrução inválida.")