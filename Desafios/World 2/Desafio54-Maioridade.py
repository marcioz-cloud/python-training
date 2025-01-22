v = 0 #initiator
adults = 0
kids = 0

# a1 = int(input("Qual seu ano de nascimento? "))
# a2 = int(input("Qual seu ano de nascimento? "))
# a3 = int(input("Qual seu ano de nascimento? "))
# a4 = int(input("Qual seu ano de nascimento? "))
# a5 = int(input("Qual seu ano de nascimento? "))
# a6 = int(input("Qual seu ano de nascimento? "))
# a7 = int(input("Qual seu ano de nascimento? "))

list = [int(input("Qual seu ano de nascimento a1? ")),
        int(input("Qual seu ano de nascimento a2? ")),
        int(input("Qual seu ano de nascimento a3? ")),
        int(input("Qual seu ano de nascimento a4? ")),
        int(input("Qual seu ano de nascimento a5? ")),
        int(input("Qual seu ano de nascimento a6? ")),
        int(input("Qual seu ano de nascimento a7? "))]

for v in range(0, len(list)):
    if list[v] >= 18 :
        adults += 1
    else:
        kids += 1

print(f"In the end, we have {adults} adults and {kids} kids present tonight.")