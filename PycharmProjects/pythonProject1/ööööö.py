yazi =(input("bir metin gir"))
sesli = ["a","e","ı","i","o","ö","u","ü"]
sesli_toplam = 0
for harf in yazi:
    if harf in sesli:
        sesli_toplam +=1

print(sesli_toplam)