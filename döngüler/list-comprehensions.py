
for x in range(10):
    print(x)
    
number = [x for x in range(10)]    
# range metodu ile 0'dan 10' a kadar bütün elemanları for ile alıp tekrar ilk x ile işleme sokuyoruz
#x liste elemanı olduğu için rangeden gelecek her eleman dizi içine giriyor.
print(number)

numbers = []
for x in range(10):
    numbers.append(x)
#0'dan 10'a kadar elemanları x'e tanımla
#her x elemanını numbers klasörüne ekle    

#NOT: Yukarıdaki her iki işlem de aynı işi yapıyorlar

for x in range(10):
    print(x**2)
# range metodundan gelen elemanları x'e atadık
# döngü her döndüğünde x'in karesini yazdırdık    
    
num = [x**2 for x in range(10)]    
print(num)
#range metodundan gelen elemanları x'e atadık
#atanan elemanların karesini alıp num dizisine ekledik
'''
'''
#bu yapıda if bloğu kullanılabilir.
num1 = [x**2 for x in range(10) if x%3 == 0]
print(num1)
# yapı içerisine koyduğumuz if bloğuyla sadece 3'ün katı olan elemanları listeye ekledik


myString = 'Hello'
myList = []

for el in myString:
    myList.append(el)
print(myList)    
# bu işlemi aşağıda uygulayacağımız yolla da yapabiliriz

myList = [elm for elm in myString]
print(myList)


years = [1999,2004,1977,1967]
age = [2020 - y for y in years]
print(age)


sonuclar = [x if x%2==0 else f'Tek: {x}' for x in range(1,10)]
#x in liste içine dahil olabilmesi için if bloğundaki şartı yerine getirmesi gerekir
print(sonuclar)
#NOT: yapı sonunda if kullanılırsa işleme alınacak olan elemanın o şartı yerine getirmesi halinde değişkene alınıp işleme konup listeye eklenmesini sağlar         
#NOT2: işlemi görülmüş değişken ifadesinden sonra kullanılırsa işlemi bitmiş değişkeni listeye sokmak için kontrol edici görev görür.

sonuc = []
for k in range(3):
    for l in range(3):
        sonuc.append((k,l))
#for döngüsü altında kullanılan yeni for döngüsü kendi döngüsü tamamlanana kadar ana döngüye geçmez.        
#ana döngünün devam etmesi alttaki döngünün tamamlanmasına bağlıdır
#yani x'e atılması gereken değerlerin tamamının atılabilmesi için y'ye her adımda bütün değerleri atmak gerekir
print(sonuc)
#bu işlemi comprehensions ile gerçekkleştirebiliriz

sonucC = [(e,f) for e in range(3) for f in range(3)]
print(sonucC)
# comprehension içinde kullanılan 2. for döngüsü birincisinin altında bulunur şekilde varsayılır.