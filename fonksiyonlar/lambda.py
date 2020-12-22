def square(num): return num**2
#Fonksiyon ifadeleri tek satırda da yazılabilir.

numbers = [1,3,5,9]

for a in numbers:
    kare = square(a)
    print(kare)
#numbers elemanlarını for döngüsü ile teker teker  a'ya atıp square fonksiyonunda parametreye attık
#fonksiyonu kare değişkenine tanımladık ve yazdırdık

'''
Bunun için map metodunu da kullanabiliriz
'''
#MAP

karey = map(square, numbers)  

#map metodu belirtilen dizi elemanlarını içinde bulunduurduğu fonksiyonun içine tek tek göndermektir
#map metodu parametrelerine kullanacağımız fonksiyonu ve fonksiyonda kullanılacak listeyi atarız
#square fonksiyonunu metot içinde kullanılmaz sadece metota bildirmek için fonksiyon ismi yazılır
print(karey)
#çıkacak sonucu herhangi bir veriye çevirmezsek yazdırdığımızda oluşan çıktının adresine ulaşırız
#liste içinde istediğimiz için list metodunu kullanabiliriz
kareL = list(map(square, numbers))
print(kareL)

#eğer liste şeklinde bir çıktı istemiyorsak for metodu ile gerçekleştirebiliriz
for item in map(square, numbers):
    print(item)

#LAMBDA EXPRESSİONS

#daha önce tanımlanmamış bir fonksiyonu o anlık kullanmak için vardır

sonuc = list(map(lambda num: num**3 , numbers))
print(sonuc)
#daha önce eleman küpü alacak bir fonksiyon tanımlı değildi 
#lambda ile kalıcı olmayan spesifik kullanılan isimsiz bir fonksiyon oluşturuldu

#lambda ile fonksiyonu oluşturduk ve bunu map metodunun ilk parametresi olan fonksiyon parametresine, numbers dizisini de ikinci parametreye attık
#lambda ile oluşturulmuş isimsiz fonksiyonu bir değişkene tanımlayıp onu artık bir fonksiyon gibi kullanabiliriz

lambda3 = lambda num: num**4
#lambda ile lambda3 adında bir fonksiyon oluşturduk
sonuc2 = lambda3(3)
print(sonuc2)

#FİLTER

numbers2 = [1,3,5,9,10,4]

#map metodunun aksine bütün elemanları fonksiyonda kullanmak yerine fonksiyona gidecek elemanları filtrelemeye yarar
def check(num): return num % 2 == 0
#burada kullanılan bool ifade ile num parametresinin fonksiyon şartını sağlaması karşılığında fonksiyon True değerini alır

sonucF = list(filter(check, numbers2))
print(sonucF)
#numbers2 dizisinden gelen elemanları fonksiyonda kullanarak fonksiyondaki bool ifadeden True değer aldığımız elemanları yeni bir liste haline getirdik
#oluşturulan yeni listeyi sonucF değişkenine tanımladık

#check fonksiyonunu lambda ile de oluşturabiliriz
#oluşturulan isimsiz fonksiyonu bir değişkene tanımlayarak onu kalıcı bir fonksiyona çevirebiliriz
