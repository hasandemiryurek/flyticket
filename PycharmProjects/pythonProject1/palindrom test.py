# Boş bir dictionary oluşturuyoruz
hash_table = {}

# Put fonksiyonu: Bir eleman ekler
def put(item):
    index = item % 11  # Hash fonksiyonu ile index hesaplanır
    while index in hash_table:  # Eğer index zaten kullanılıyorsa
        if hash_table[index] == item:  # Aynı item zaten varsa, eklemeyi durdur
            return
        index = (index + 1) % 11  # Linear probing ile bir sonraki index'e geç
    hash_table[index] = item  # Boş bulunan index'e item eklenir

# Contains fonksiyonu: Bir elemanın tablonun içinde olup olmadığını kontrol eder
def contains(item):
    index = item % 11
    while index in hash_table:  # Eğer index'te bir şey varsa
        if hash_table[index] == item:  # Item bulunduysa
            return True
        index = (index + 1) % 11  # Linear probing ile bir sonraki index'e geç
    return False  # Item bulunamadıysa

# Elemanları ekleyelim
put(54)
put(26)
put(93)
put(17)
put(77)
put(31)

# Hash tablosunu yazdıralım
print(hash_table)

# 22'nin tabloda olup olmadığını kontrol edelim
print("contains(22): ", contains(22))

# 17'nin tabloda olup olmadığını kontrol edelim
print("contains(17): ", contains(17))