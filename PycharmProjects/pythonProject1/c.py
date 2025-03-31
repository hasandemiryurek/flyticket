def s(x):
    uzunluk = len(x)
    a=""
    for i in range (uzunluk-1,-1,-1):
        a += x[i]
    return a
print(s("evet"))