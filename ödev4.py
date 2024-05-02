import sqlite3
import time

def create_database():
    conn = sqlite3.connect('metinler.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS metinler
                 (id INTEGER PRIMARY KEY, metin TEXT)''')
    conn.commit()
    conn.close()

def metin_al(metin):
    conn = sqlite3.connect('metinler.db')
    c = conn.cursor()
    c.execute("INSERT INTO metinler (metin) VALUES (?)", (metin,))
    conn.commit()
    conn.close()
"""
def karsılastır(metin1, metin2):
    kelime_set1 = set(metin1.split())
    kelime_set2 = set(metin2.split())
    kesisim = len(kelime_set1.intersection(kelime_set2))
    hesap = len(kelime_set1) + len(kelime_set2) - kesisim
    return kesisim / hesap
"""
def karakter_benzerligi(metin1,metin2):
    sayac = 0
    len_metin1 =len(metin1)
    len_metin2 =len(metin2)
    if len_metin1>len_metin2:
        for i in range(len_metin2):
            if metin1[i] == metin2[i]:
                sayac +=1
        return sayac/len_metin2
    else:
        for i in range(len_metin1):
            if metin1[i] == metin2[i]:
                sayac +=1
        return sayac/len_metin1
    

def main():
    create_database()
    metin1 = input("İlk metni girin: ")
    metin2 = input("İkinci metni girin: ")
    metin_al(metin1)
    metin_al(metin2)
    print("Metinler veritabanına eklendi.")

    metin1 = "Örnek metin 1"
    metin2 = "Örnek metin 2"

    time.sleep(3) 
    print("Benzerlik hesaplanıyor")
    time.sleep(3)


    benzerlik = karakter_benzerligi(metin1, metin2)
    print("Benzerlik oranı:", benzerlik)

    with open("benzerlik_durumu.txt", "w") as file:
        file.write(f"Benzerlik oranı: {benzerlik}")

if __name__ == "__main__":
    main()
