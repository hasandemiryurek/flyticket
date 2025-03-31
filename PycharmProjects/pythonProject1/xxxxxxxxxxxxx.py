
n=int(input("Tek sayıları toplanacak sayıyı girin: "))
toplam=0
for i in range (1,n,2):
    toplam = toplam + i
print("1 den n ye kadar olan sayıların toplamı ", toplam)