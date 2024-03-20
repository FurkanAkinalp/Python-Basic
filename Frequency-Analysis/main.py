import hell
lang = input("Lütfen metninizin dilini giriniz(Eğer diliniz Türkçe ise 'tr' giriniz değilse enter tuşuna basınız): ")
x = input("Lütfen bir karakter giriniz:")

#verilen karakterin hangi dilde ise o dilin alfabesinede var mı yok mu kontrol ediyor
hell.alfabemi(x,lang) 





article = input("Lütfen metninizi giriniz(Maksimum 10000 karakter girebilirsiniz.): ")


#harfleri küçülten modül

y = hell.kucult(article) 
z=hell.say(y)

print(z,"Adet harf var")
#yüzdelik oranı bulmamızı sağlıyor

hell.split(y,lang,z) 



#Örnek input
"""
Türkiye,bazı tarihi nedenlerle uygarlık yarışına geç girmiş, büyük kültürel kopukluklar yaşamış bir ülke. Bu gecikmenin sancıları da çok uzun sürmüştür. Türk şair ve yazarları, bu büyük kopukluğun derin acılarını, izlerini yaşıyor hala. Bugün Türk edebiyatında haddinden fazla bireycilik ve son derece köksüz bir toplumculuk var. Sanki uzayda yaşıyor şair ve yazarlarımız. Halbuki bireycilik de toplumculuk gibi kültürel kökleri olması gereken bir olgudur.
"""

