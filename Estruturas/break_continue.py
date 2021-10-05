#O break é usado para parar laços e o continue para pular um iteração
for x in range(1, 15):
    print(x)
    x = x + 1

    if(x == 7):
        continue
    if(x == 13):
        break