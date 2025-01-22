v = 0 #initiator

for n in range(1, 501, 2):
    if n%3 == 0:
        print(n)
        v += n

print(f"O valor da soma total foi de {v}")
