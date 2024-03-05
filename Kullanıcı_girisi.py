
i=3

while (i!=0):
    kullanıcı = input("Kullanıcı Adınız:")
    parola = input("Parola:")

    if(kullanıcı=="root" and parola == "admin"):
        print("Giris basarılı!!")
        exit()
    else:
        i -= 1
        if(i!=0):
            print("Kalan Hakkınız {}".format(i))


print("Hakkınız kalmadı :(")