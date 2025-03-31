vize = int(input("vize notu:"))
final = int(input("final notu:"))

ortalama = vize*0.40 + final*0.60

if ortalama >= 50:
    print("geçti")
else:
    print("kaldı")

