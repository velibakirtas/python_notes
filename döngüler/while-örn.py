sayilar = [1,5,7,9,12,19,21]

#ekleme: .append
#sıraya dizme: .sort

#1) sayılar listesindeki elemanları while ile ekrana yazdırın

c = 0
while (c < len(sayilar)):
    print(sayilar[c])
    c += 1
    
# bir değişkene 0 tanımladık
#while döngüsüne bağlı olarak c değişkenini sayilar dizisinin eleman sayısı kadar işleme soktuk
#her döngüde sayilar dizisindeki c'ye eşit sayıdaki indexteki elemanını yazdırdık
#her işlemden sonra c'yi bir arttırdık
#döngü sayilar dizisindeki eleman sayısı kadar devam etti    


#2) kullanıcıdan iki sayı alıp aradaki tüm tek sayıları yazdır

x = int(input('sayı giriniz: '))
y = int(input('sayı giriniz: '))

b = x
while b <= y:
    if (b%2 == 1):
        print(f'{b} tek sayıdır')
    b += 1        
    
#kulllanıcıdan iki tane sayı aldık
#aldığımız ilk sayıyı b değişkenine aktardım
#if bloğunda b değişkenindeki sayının tek sayı olması şartıyla işlemi devam ettirdim
#şarta uyması halinde sayıyı yazdırdım
#döngü her tamamlandığında b değişkenini 1 arttırdım
#döngüyü b, y'ye eşit olana kadar devam ettirdim   

#3) 1 ile 100 arasındaki sayıları azalan şekilde yazdırın

z = 100
while z > 0:
    print(z)
    z -= 1


#4) kullancıdan aldığınız 5 tane sayıyı  sıralı şekilde yazdır

numbers = []
t = 1
while t < 6 :
    n = int(input('sayı giriniz: '))
    numbers.append(n)
    t += 1    
    
numbers.sort()    
   
for num in numbers:
    print(num)    
                                #ya da 
                                
'''
i = 0
while (i < len(numbers)):
    print(numbers[i])
    i += 1
'''                        
#5)Kullanıcıdan alacağınız sınırsız sayıdaki ürün bilgisini ürünler listesinde saklayınız
#  ** ürün sayısını kulllanıcıdan al
#  ** dictionary liste yapısı şeklinde olsun 
#  ** ürün ekleme işlemi bittiğinde ürünü ekranda while ile yazdır  


urunler = []                               
adet = int(input('lütfen ürün miktarını giriniz: '))

i2 = 0
while (i2 < adet):
    name = input('ürün ismi: ' )
    price = input('ürün fiyatı: ')
    urunler.append({
        'name': name ,
        'price': price
    })
    i2 += 1
    
i3 = 0
while i3 < len(urunler):
    print(urunler[i3]['name'])
    i3 += 1
    