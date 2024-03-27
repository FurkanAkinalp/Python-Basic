print("""-------------------------------\n|  Created by Furkan Akınalp  |\n-------------------------------""")

class Personel:
    def __init__(self, id, ad, soyad, departman, calisma_yili, maas):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.departman = departman
        self.calisma_yili = calisma_yili
        self.maas = maas
        pass

class Firma(Personel):
    
    def __init__(self, personel_liste):
        self.personel_liste = []

    def personel_ekle(self,personel):
        for p in self.personel_liste:
            if p.id == personel.id:
                print("{} id numaralı bir personel var".format(personel.id))
                return 
        self.personel_liste.append(personel)

        
    
    def personel_listele(self):
        print("Personel Listeleme:\n===================\n")
        for personel in self.personel_liste:
            print("""| Id                : {}\n
| Adı               : {}\n
| Soyadı            : {}\n
| Departmanı        : {}\n
| Çalışma yılı      : {}\n
| Maaş              : {}\n===================\n""".format(personel.id, personel.ad, personel.soyad, personel.departman, personel.calisma_yili, personel.maas))
                   

            
    def maas_zammi (self, personel_id , zam_orani):
        for personel in self.personel_liste:
            if personel.id == personel_id:
                personel.maas += personel.maas*(zam_orani/100)
                print("{} id numaralı ve {} adlı personelin maaşı {}% oranında arttırıldı. Yeni maaş: {}".format(personel.id, personel.ad, zam_orani, personel.maas))
                return
        print("{personel_id} id numaralı personel bulunamadı:")

    def personel_cikart (self, personel_id):
        for personel in self.personel_liste:
             if personel.id == personel_id:
                personel_ad = personel.ad
                self.personel_liste.remove(personel)
                print("{} id numaralı ve {} adlı personel silindi. ".format(personel_id, personel_ad))
                return
        print("{personel_id} id numaralı personel bulunamadı:")
    pass


def bilgi_al():
    id = int(input("Personel idsini giriniz:\n>$ "))
    ad = input("Personel adını giriniz:\n>$ ")
    soyad = input("Personel soyadını giriniz:\n>$ ")
    departman = input("Personel departmanını giriniz:\n>$ ")
    calisma_yili = int(input("Personel çalışma yılını giriniz:\n>$ "))
    maas = int(input("Personel maaşını giriniz:\n>$ "))
    return Personel(id, ad, soyad, departman, calisma_yili, maas)
    
     
if __name__ == "__main__":
    A_firmasi = Firma([])
    while True:
        secim=input("""Lütfen yapmak istediğiniz işlemi seçin:
-> e: Personel ekleme
-> l: Personel listeleme
-> z: Maaş zammı uygulama
-> s: Personel silme
-> q: Çıkış\n>$ """)
        if secim == 'e':
            A_firmasi.personel_ekle(bilgi_al())
        elif secim == 'l':
            A_firmasi.personel_listele()
        elif secim == 'z':
            id = int(input("Zam yapılacak personel idsini giriniz:\n>$ "))
            zam_orani = float(input("Lütfen zam oranı giriniz:\n>$ "))
            A_firmasi.maas_zammi(id, zam_orani)
        elif secim == 's':
            id = int(input("Silinecek personel idsini giriniz:\n>$ "))
            A_firmasi.personel_cikart(id)
        elif secim == 'q':
            print("Programdan çıkılıyor...")
            quit()
        else:
            print("Hatalı deger")









