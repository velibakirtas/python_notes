'''
x = input("1.sayı: ")  # "input" kodu kullancıdan veri alma komutudur.
y = input('2.sayı: ')

toplam = x + y

print(toplam)
# Bu işlemde x ve y string değer olarak görülür ve birleştirilir

# x ve y'nin "int" olarak algılanması için başına int getirilebilir.

print(type(x))
print(type(y))

toplam = int(x) + int(y)
print(toplam)
# bu şekilde yazdırılacak sonuç x ve y'nin int veri tipiyle algılanıp girilen verinin matematiksel toplamıdır.
'''



x = 7            #int
y = 3.5          #float
name = 'Veli'    #str
isOnline = True   #bool

'''
print(type(x))
print(type(y))
print(type(name))
print(type(isOnline))
'''
# Type Conversion(Tip Değişimleri)

# int to float

'''
x = float(x)
print(x)
print(type(x))
'''

# float to int
'''
y = int(y)
print(y)
print(type(y))
'''

# float to string
'''
result = x+y         # x ve y'nin toplamı float şeklindedir dolayısıyla result olarak tanımlanan 
print(result)          result değişkeni float tipindedir.
print(type(result))
'''

'''
result = str(x) + str(y)  # Burada ise float olan result değerini str tipine dönüştürdük.
print(result)
print(type(result))
'''

#bool to str

'''
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))
'''

#bool to int
'''
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))
'''

#int to bool
'''
print(x)
x = bool(x)
print(x)
print(type(x))
'''

#str to bool
'''
name = bool(name)
print(name)
print(type(name))
'''
