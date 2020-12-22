
def changeName(n):
    n = 'veli'
    
name = 'mehmet'    
changeName(name)
print(name)
#fonksiyona gönderdiğimiz değer fonksiyon tarafından değiştirilemez
#değişkeni print ile yazdırdığımızda değişkenin hala ilk tanımlandığı değere sahip olduğunu görürüz
# n değişkeni için bir adres tanımlanıp içinde 'veli' bilgisi tutuluyor
# name değişkeni için de bir adres tanımlanıp içinde 'mehmet' bilgisi tutuluyor 
#fonksiyonda gerçekleştirdiğimiz kopyalama sadece değer kopyalamasıdır referanslar(adresler) kopyalanmaz
#value tipindeki değişken kopyalamalırnda adresler kopyalanmaz sadece değerler kopyalanır

def change(n):
    n[0] = 'istanbul'
    
sehirler = ['ankara', 'izmir']    
change(sehirler)
print(sehirler)
#fonksiyondaki n parametresine tanımlamış olduğumuz sehirler dizisinin adresi gönderiliyor
#bu adresteki bilginin ilk indexindeki değeri 'istanbul' yapıyoruz
#listeyi parmetreye gönderdiğimiz zaman listenin kopyası çıkartılmıyor
#orijinal listedeki adresi gönderip adresteki bilgiyi güncelliyoruz

m = sehirler[:] #parçalama işlemi
m[0] = 'kocaeli'
print(sehirler)
print(m)
#burada ise sehirler dizisin parçalayıp m dizisi içine attık
#m dizisi sehirler dizisinin elemanlarının ayrılıp m dizisine atılmasıyla oluşur
#bundan dolayı sehirler dizisinin adresiyle bir ilgisi yoktu
#iki dizinin de adresleri farklıdır.


def add(a,b):
    return sum((a,b)) #sum fonksiyonu py kütüphanesinden gömülü olarak gelir

print(add(10,20))
# sum fonksiyonu parametresinde dizi oluşturularak kullanılır

def add1(x, y, z = 0):
    return sum((x,y,z))
print(add1(10,20))
#bu örnekte olduğu gibi parametreye istenenden az değer girilirse girilmeyen değer(z) yerine default olarak 0 değerini gönderdik
#bu sebeple add fonksiyonunda da add1 fonksiyonunda da aynı sonuç çıkacaktır

print(add1(10,20,10))

def add2(*p):
    return sum(p)
print(add2(12,5,6,43,8,64,28))
#çok sayıda parametre girişi olduğunda teker teker belirtmek yerine * ile istediğimiz kadar parametre atabiliriz.Tuple veri tipinde bir liste oluşturur


def displayUser(**params): #gelecek olan liste türünün dictionary olduğunu bildirmek için ** kullanılır
    for key, value in params.items():
        print('{} is {}'.format(key,value))
        
displayUser(name = 'Veli', age = 21, city = 'istanbul')
displayUser(name = 'Mehmet', age = 17, city = 'konya', phone = '123')
displayUser(name = 'Hulya', age = 43, city = 'sivas', phone = '456', mail = 'h@m.com')

def myFonk(a, b, *parameter, **kw):
    print(a)
    print(b)
    print(parameter)
    print(kw)
    
myFonk(1, 100, 10, 200,, 3 'veli',key1 = 'value2', key2 = 98 )
#oluşturulan fonksiyona gönderilen parametreler tek bir veri tipi ya da liste türünden oluşmak zorunda değildir
#örnekte olduğu gibi parametrede a ve b'ye int, parameter'a tuple ve kw'ye dict attık
    
