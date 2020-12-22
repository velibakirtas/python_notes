'''
ATAMA OPERATÖRLERİ
'''

x, y, z = 5, 10, 20

'''
x, y = y, x
'''
#değişkenlerin sahip olduğu değer değişimleri bu şekilde yapılabilir

'''
x = x + 5
'''
#x değişkeninn sahip olduğu değeri 5 arttırdık.Bu işlem bir farklı bir operatör ile yapılabilir.
x += 5

'''
x -=5
'''
#Bu işlem -= operatörü için de geçerlidir.
#değişkenin sahip olduğu değerden 5 çıkararak değişkene yeni değer tanımlanır
'''
x *= 5 
'''
#değişkenin sahip olduğu değeri 5 ile çarparak değişkene yeni değeri tanımlar

#Bu operatörler diğer matematiksel operatörlerin de hepsinde kullanılır.

values = 1, 2, 3
print(values)
print(type(values))

x, y, z = values
#values listesindeki elemanları x, y, z değişkenlerine attık
'''
x = 1
y = 2
z = 3 halini aldı'''

'''
x, y = values
'''
#Bu şekilde bir tanımlama hata ile sonuçlanır. 
#Değişken sayısı ve dizideki eleman sayısından az olduğundan tanımlama gerçekleşemez.

'''
values = 1, 2, 3, 4, 5
x, y, z = values'''
#Bu tanımlama da hata ile sonuçlanır
#Tanımlanacak liste elemanı değişkenden fazla olduğu için liste içinden çıkarılamaz.

valuesT = 1, 2, 3, 4, 5
x, y, *z = valuesT
print(x, y, z)
# *a operatörü ile listedeki fazla olan elemanı son değişkene dizi şeklinde tanımlar
print(x, y, z[0])

