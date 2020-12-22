#DİZİLERDE FOR

number = [1,2,3,4,5]

print(number[0])
print(number[1])
print(number[2])
print(number[3])
print(number[4])

#daha fazla sayıdaki eleman için bunu yapmak mümkün olmayacaktır
#bunun için for döngüsünü kullanabiliriz.

for num in number:
    print(num)
#burada yapılan işlem:
#liste içerisinden elemanları tek tek al num değişkeni içerisine at for döngüsü her döndüğünde gelen num bilgisini yazdır.    
#burada yapılan temel mantık elemanları yazdırmak değil listenin eleman sayısı kadar for döngüsünün dönüyor olmasıdır.

for num2 in number:
    print('hello')
#listede 5 eleman bulunuyor listedeki eleman sayısı kadar print parametresindeki ifadeyi yazdırdık

names = ['veli', 'mehmet', 'hülya']

for isim in names:
    print(f'my name is {isim}')
    
#STRİNG İFADELERDE FOR
name = 'veli bakirtas'    

for n in name:
    print(n) 
#string ifadelerde her karakter indexlendiği için for döngüsünde ifadeyi yazdırmak istediğimizde her karakteri teker teker yazdırır.        

#TUPLE LİSTELERİNDE FOR
tuple = (1,2,3,4,5)

for t in tuple:
    print(t)
#bu liste türü içinde geçerlidir.

tuple2 = [(1,2), (1,3), (2,1), (3,4)]    

for t2 in tuple2:
    print(t2)
#dizi içerisinde tuple halde bulunan listeleri yazdırır

#tuple listeleri içindeki elemanları da teker teker yazdırabilirz
for a,b in tuple2:
    print(a)
#her bir tuple listesinin ilk elemanını yazdırdık

for a,b in tuple2:
    print(a,b)    
#tuple listesindeki elemanları listeden çıkarılmış şekilde yan yana yazar

#DİCTİONARY LİSTELERİNDE FOR


d = {'k1': 1, 'k2': 2, 'k3': 3}

for kl in d:
    print(kl)
#dictionary listelerinde bu şekilde bir kullanım sadece key bilgilerini ulaşmamızı sağlar


for kli in d.items():
    print(kli)
#.items metodu ile dictionary listesindeki eleman gruplarına tek tek ulaşırız(key ve value değerlerinin tek tek listelenmiş hali

for key,value in d.items():
    print(key, value)
#bu şekilde listedeki key ve value elemanlarını listeden çıkartarak tek tek yazdırabiliriz

for key,value in d.items():
    print(value)
#bu şekilde de sadece value değerlerini elde edebiliriz

