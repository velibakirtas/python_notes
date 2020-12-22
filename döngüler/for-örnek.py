
sayilar = [1,3,5,7,9,12,19,21]

#1)sayilar listesindeki hangi sayılar 3'ün katıdır

for sayi in sayilar:
    if(sayi%3 == 0):
        print(sayi)
#sayılar dizisindeki bütün elemanlar sayi değişkenine atılıyor sonraki adımda if koşul ifadesiyle parametrede bulunan şarta uyan elemanlar yazdırılıyor

#2)sayılar listesindeki sayıların toplamı kaçtır

toplam = 0
for sayi in sayilar:
    toplam = toplam + sayi #(toplam += sayi olarak da yaılabilir)
print(toplam)         

#3) sayılar listesindeki tek sayıların toplamını yazdır

toplam2 = 0
for sayi in sayilar:
    if (sayi % 2 != 0):
        print(sayi ** 2)        


sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
         
#4) şehirlerden hangileri en fazla 5 karakterlidir

for sehir in sehirler:
    if (len(sehir) <= 5):
        print(sehir)


urunler = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'}
]        

#5) ürünlerin fiyatları toplamı nedir
toplam3 = 0
for urun in urunler:
    fiyat = int(urun['price'])
    toplam3 += fiyat
print(toplam3)    

#6)ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz

for urun in urunler:
    if int(urun['price']) <= 5000:
        print(urun['name'])
      