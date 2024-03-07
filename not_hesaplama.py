vize = float(input("Vize puanı giriniz:"))
final = float(input("Final puanı giriniz:"))

topnot = (vize*0.4)+(final*0.6)

print("Geçme Notu: {}".format(topnot))
"""switch={
       topnot >= 90: print("AA"),
    90 > topnot >= 85: print("BA"),
    85 > topnot >= 80: print("BB"),
    80 > topnot >= 75: print("CB"),
    75 > topnot >= 70: print("CC"),
    70 > topnot >= 65: print("DC"),
    65 > topnot >= 60: print("DD"),
    60 > topnot >= 55: print("FD5"),
    topnot < 50: print("FF"),
}"""

if(topnot>=90):
    print("AA")
elif(topnot>=85):
    print("BA")
elif(topnot>=80):
    print("BB")
elif(topnot>=75):
    print("CB")
elif(topnot>=70):
    print("CC")
elif(topnot>=65):
    print("DC")
elif(topnot>=60):
    print("DD")
elif(topnot>=55):
    print("FD")
else:
    print("FF")