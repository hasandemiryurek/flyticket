class HashTable:
    def __init__(self, size=11):
        """Basit bir hash tablosu başlangıç boyutuyla oluşturulur."""
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        """Basit bir modüler hash fonksiyonu."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Hash tablosuna bir anahtar-değer çifti ekler."""
        index = self.hash_function(key)
        i = 0

        while True:
            new_index = (index + i ** 2) % self.size
            if not self.table[new_index] or self.table[new_index][0] == key:
                self.table[new_index] = (key, value)
                return
            i += 1

    def search(self, key):
        """Anahtarı arar ve değerini döndürür."""
        index = self.hash_function(key)
        i = 0

        while True:
            new_index = (index + i ** 2) % self.size
            if not self.table[new_index]:
                return None
            if self.table[new_index][0] == key:
                return self.table[new_index][1]
            i += 1

    def delete(self, key):
        """Anahtarı hash tablosundan siler."""
        index = self.hash_function(key)
        i = 0

        while True:
            new_index = (index + i ** 2) % self.size
            if not self.table[new_index]:
                return False
            if self.table[new_index][0] == key:
                self.table[new_index] = None
                return True
            i += 1

    def __str__(self):
        """Hash tablosunu basitçe yazdırır."""
        return str(self.table)


# Örnek Kullanım
if __name__ == "__main__":
    ht = HashTable()
    ht.insert("elma", 10)
    ht.insert("armut", 20)
    ht.insert("çilek", 30)
    print("Başlangıç Tablosu:", ht)
    print("'armut' Ara:", ht.search("armut"))
    ht.delete("armut")
    print("'armut' Silindikten Sonra Tablo:", ht)
    ht.insert("muz", 40)
    print("'muz' Eklendikten Sonra Tablo:", ht)