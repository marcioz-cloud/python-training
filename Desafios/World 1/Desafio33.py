# Bigger or Smaller Than
a1 = int(input("Qual numero 1? "))
a2 = int(input("Qual numero 2? "))
a3 = int(input("Qual numero 3? "))

if a1>a2 and a1>a3 :
    print("a1 eh maior")
else:
    if a2>a1 and a2> a3:
        print("a2 eh maior")
    else:
        if a3>a1 and a3>a2:
            print("\033[31ma3 eh maior") #\033[ style; text; background + m
            #style : 0, 1, 4, 7.
            #text de 30 a 37
            #back de 40 a 47
