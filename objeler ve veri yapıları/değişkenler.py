#print(5000 - (5000 * 0.27))
#print(7000 - (7000 * 0.27))


maasAli = 5000
maasVeli = 7000
vergi = 0.27

print (maasAli - (maasAli * vergi))
print(maasVeli - (maasVeli * vergi))

#Değişken Tanımlama Kuralları

# rakam ile başlayayamaz

# 1number = 10 olamaz

number1 = 10

# değikenler boş bırakılamaz
# number =     olamaz


# Aynı değişken ismine birden fazla değer tanımlanamaz

#örn
number1 = 10
print(number1)
number1 = 20  # en son tanımlanan değer 20 olduğu için 20 üzerinden işlem görür
print(number1) #en son atanan değer 20 olduğu için print komutuyla 20 yazılır

number1 += 40 #önceki number değerine 40 ekler
print(number1)

# Değişken tanımlamalarında büyük küçük harf duyarlılığı vardır

age = 15
AGE = 35

print(age)
print(AGE)

x = 1                #integer
y = 2.3              #float
isStudent = True     #bool
name = "Veli"        #string
# Buradaki isStudent = True örneğinde öğrenci mi sorusuna 'Evet' cevabını veriyoruz

x, y, isStudent, name = (1, 2.3, True, "Veli") # Tek bir satırda birden fazla değişken tanımlanabilir.


a = 10
b = 20 
print(a+b) # 30 yazdırılacaktır

a = "10"
b = "20"
print(a+b) # 1020 olarak yazdırılacaktır
# Burada string değerler birleşir

firstname = "Veli"
lastname = " Bakırtas"
print(firstname+lastname)
# Değişken isimleri arasında boşluk olamaz.