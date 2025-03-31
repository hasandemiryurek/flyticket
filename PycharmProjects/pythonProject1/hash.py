# Boş bir dictionary oluşturuyoruz
hash_table = {}

# Put fonksiyonu: Bir eleman ekler
def put(item):
    index = item % 11  # Hash fonksiyonu ile index hesaplanır
    original_index = index  # Başlangıç indeksini sakla
    while index in hash_table:  # Eğer index zaten kullanılıyorsa
        if hash_table[index] == item:  # Aynı item zaten varsa, eklemeyi durdur
            return
        index = (index + 1) % 11  # Linear probing ile bir sonraki index'e geç
        if index == original_index:  # Tüm tablo dolandıysa çık
            raise Exception("Hash tablosu dolu!")
    hash_table[index] = item  # Boş bulunan index'e item eklenir
    # Sıralı olacak şekilde tekrar düzenle
    sort_hash_table()

# Hash tablosunu sıralı artan düzene getirir
def sort_hash_table():
    global hash_table
    sorted_items = sorted(hash_table.values())  # Mevcut elemanları sıralar
    hash_table.clear()  # Hash tablosunu temizler
    for item in sorted_items:  # Sıralı elemanları yeniden ekler
        index = item % 11
        while index in hash_table:  # Boş index bulana kadar devam
            index = (index + 1) % 11
        hash_table[index] = item

# Contains fonksiyonu: Bir elemanın tablonun içinde olup olmadığını kontrol eder
def contains(item):
    index = item % 11
    original_index = index
    while index in hash_table:  # Eğer index'te bir şey varsa
        if hash_table[index] == item:  # Item bulunduysa
            return True
        index = (index + 1) % 11  # Linear probing ile bir sonraki index'e geç
        if index == original_index:  # Tüm tablo dolandıysa çık
            break
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