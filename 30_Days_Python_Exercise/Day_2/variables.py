#Day 2: 30 Days of python programming
first_name = "Furkan"
last_name = "Akınalp"
full_name = first_name + last_name
country = "Turkiye"
city = "Ankara"
age = 45
year = 2024
is_married = False
skills = ['HTML', 'CSS', 'Js', 'React', 'Python']

person_info = {
    'firstname':'Furkan', 
    'lastname':'Akınalp', 
    'country':'Turkiye',
    'city':'Ankara'
    }

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(skills))
print(type(person_info))

print(len(first_name))
print(len(last_name))
print(len(full_name))


num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("sayı bir: {}\nsayı iki: {}\ntoplam: {}\nfark: {}\nçarpım: {}\nbölüm: {:.2}\nmod: {}\nüssü: {}\nköke alma: {}".format(num_one,num_two,total,diff,product,division,remainder,exp,floor_division))

radius = 30
pi = 3.14
area_of_circle = pi*(radius**2)
circum_of_circle = 2*pi*radius
print("Yarıçap:", radius)
print("Alan:", area_of_circle)
print("Çevre: ", circum_of_circle)

radius=int(input("Lütfen yarıçapı giriniz:"))
area_of_circle = pi*(radius**2)
circum_of_circle = 2*pi*radius
print("Yarıçap:", radius)
print("Alan:", area_of_circle)
print("Çevre: ", circum_of_circle)

first_name = input("Adınız: ")
last_name = input("Soyadınız: ")
country = input("Ülkeniz: ")
age = int(input("Yaşınız "))
print("Yazdırılıyor")
print("Adınız:",first_name)
print("Soyadınız: ", last_name)
print("Ülkeniz: ", country)
print("Yasşınız: ",age)
