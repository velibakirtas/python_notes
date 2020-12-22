#RANGE METODU
       
for item in range(10)    :
    print(item)
#range metodu ile ortada bir liste yokken belli bir aralığı işleme sokabiliriz
#parametre içine girilen bir değer döngünün biteceği elemanı belirtir(0'dan 10'a kadar)

for item in range(3,12):
    print(item)
#parametre içine girilmiş iki tane değer varsa ilki sayıların başlangıç ikincisi bitiş değeridir.

for item in range(50,100,10):
    print(item)
#burada parametreye girilen üçüncü eleman ise artış miktarının belirtir.

arit = list(range(50,100,10))
#list metodu ile range metodundan gelecek değerleri liste haline getirdik
#50 den 100 e kadar olan sayıları 10 ar 10 ar al liste haline getir ve arit değişkenine at
print(arit)


#ENUMERATE METODU

greeting = 'Hello There'
index = 0

for letter in greeting:
    print(f'index: {index}, letter: {letter}')
    index+=1
# str ifadenin harflerini index numaralarını belirterek yazdırdık
#bunun için index adında bir değişkene 0 değerini attık
#index değişkenini döngüde yazdırdık döngü her devam ettiğinde indexe bir ekledik

# bu işlemi enumerate metodu ile kolaylaştırabiliriz

for item in enumerate(greeting):
    print(item)
# item değişkenine attığımızda eleman ve index ikililerini liste halinde ayırır


for index, item in enumerate(greeting):
    
    print(f'index: {index}, item: {item}')
#bu şekilde greetingten çıkarılacak ikiliyi teker teker farklı değişkenlere tanımlayabiliriz    


#ZİP METODU

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

general = list(zip(list1,list2))
print(general)
#zip metodu ile işleme sokulan listelerdeki elemanlar index numaraları referans alınarak birleştirilir
#söz konusu elemanlar dizi içinde tuple listesi halinde bulunur halinde bulunur.

for y,z in zip(list1, list2):
    print(y)