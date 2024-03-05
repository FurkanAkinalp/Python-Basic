boy = float(input("Boyunuzu giriniz :"))
kilo = float(input("Kilonuzu giriniz :"))


print("Beden Kitle İndeksi: Kilo/Boy(m)*Boy(m)")
print("{}/{}*{} = {}".format(kilo,boy,boy,float(kilo/(boy ** 2))))