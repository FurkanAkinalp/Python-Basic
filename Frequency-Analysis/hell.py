sayacc = []
sayacc = [0] * 29 
harfler_tr = 'abcçdefgğhiıjklmnoöprsştuüvyz'
harfler_en = 'abcdefghijklmnopqrstuvwxyz'
article = ''
lang = ''
global sayac3

def say(article):
    global sayac3
    for char in article:
        if char.isalpha():
            sayac3 += 1
    return sayac3

def split(article, lang, sayac3):
    for char in article:
        if char.isalpha():
            if(lang=='tr'):
                control_tr(char,sayac3)  
            else:
                control_nontr(char,sayac3)
                
def alfabemi(char, lang):
    global harfler_tr, harfler_en
    if lang =='tr':
        for i in harfler_tr:
            if char==i:
                print("Alfabedendir")
                return char
        
        print("Alfabeden değildir")
        return 0
    else:
        for i in harfler_en:
            if char==i:
                print("Alfabedendir")
                return char
        print("Alfabeden değildir")
        return 0

    
def sayac(i,sayac3):
    sayacc[i] += 1
    global sayac2
    sayac2 += 1
    if 1000> sayac2 >= 100 and sayac2==sayac3:
        if lang=='tr':
            sonu_tr(sayac2)
        else:
            sonu_nontr(sayac2)
    elif 10000>sayac2>=1000 and sayac2==sayac3:
        if lang=='tr':
            sonu_tr(sayac2)
        else:
            sonu_nontr(sayac2)
    elif sayac2>=10000 and sayac2==sayac3:    
        if lang=='tr':
            sonu_tr(sayac2)
        else:
            sonu_nontr(sayac2)

def control_tr(char,sayac3):
    global harfler_tr
    index = harfler_tr.find(char)
    if index != -1:
        sayac(index,sayac3)
 
def control_nontr(char,sayac3):
    global harfler_en 
    index = harfler_en.find(char)
    if index != -1:
        sayac(index,sayac3)
 
def sonu_tr(i):
    global harfler_tr 
    print("İlk {} karaktere göre:".format(i))
    for j in range(len(harfler_tr)):
        print(harfler_tr[j],sayacc[j]," kullanılma oranı => {:.2f}".format(float(sayacc[j]/i*100)))

def sonu_nontr(i):
    global harfler_en
    print("İlk {} karaktere göre:".format(i))
    for j in range(len(harfler_en)):
        print(harfler_en[j],sayacc[j], " kullanılma oranı => {:.2f}".format(float(sayacc[j]/i*100)))



sayac2 = 0
sayac3 = 0

def kucult(article):
    print(article.lower())
    return article.lower()




print(say(article.lower()))
#Örnek input
"""
Türkiye,bazı tarihi nedenlerle uygarlık yarışına geç girmiş, büyük kültürel kopukluklar yaşamış bir ülke. Bu gecikmenin sancıları da çok uzun sürmüştür. Türk şair ve yazarları, bu büyük kopukluğun derin acılarını, izlerini yaşıyor hala. Bugün Türk edebiyatında haddinden fazla bireycilik ve son derece köksüz bir toplumculuk var. Sanki uzayda yaşıyor şair ve yazarlarımız. Halbuki bireycilik de toplumculuk gibi kültürel kökleri olması gereken bir olgudur.
"""




class kisi:
    def __init__(self,ad,soyad,numara,yıl,soz) -> None:
        self.ad ='Furkan'
        self.soyad = 'Akınalp'
        self.numara = 211220035
        self.yıl = 2003
        self.soz= "kill soceity"
        pass

def goster(deger):
    print("Created by Lehhguman\nAd = {}\nSoyad = {}\nNumara = {}\nYıl ={}\nSoz = {}".format(deger.ad,deger.soyad,deger.numara,deger.yıl,deger.soz))

Furkan = kisi("Furkan","Akınalp",211220035,2003,"kill soceity")
goster(Furkan)

