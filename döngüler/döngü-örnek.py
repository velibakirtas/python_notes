'''
    1 ile 100 arasında rastgele bir sayıyı aşağı yukarı ifadeleriyle buldurmaya çalışın
    ** random modülü
    ** 100 üzerinden puanlama yapın her soru 20 puan
    ** Hak bilgisini kullanıcıdan al ve her soru belirtilen can sayısı üzerinden hesaplansın
'''
    
import random

sayi = random.randint(1,10)
can = int(input('kaç kere tahminde bulunmak istersiniz: '))
hak = can
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))
    
    if sayi == tahmin:
        print(f'Doğru tahmin {sayac}. defada bildiniz. Toplam puanınız {100 - (100/can) * (sayac -1)}')
        #sayacı 1 eksiltemizin sebebi her döngünün başında bir arttığı için kullanıcının doğru bildiği adımda da puan düşecek bunu engellemek için sayacın 1 eksiğini aldık.
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')        
    if hak == 0:
        print(f'hakkınız bitti, tutulan sayı: {sayi}')        
        
# random modülü çağırdık
# random modülü randint metoduyla 1 ile 10 arasından rastgele bir sayı seçtirdik 
# kullanıcıdan can değişkenine tanımladığımız bir tahmin miktarı istedik
# can değerini hak değişkenine attık
# sayac adında bir değişkene 0 değerini attık (sayac değişkenini döngünün dönme miktarını kayda alması için ekledik)       
# while ile döngüyü başlatıp hak > 0 için devam ettirdik
# döngü başında hak değişkenini 1 azalttık ve sayac değişkenini bir arttırdık
# (hak= kullanıcdan alınan tahmin etme hakkı, sayac= döngünün bulunduğu aşama sayısını kaydeden değişken)
# kullanıcıdan bir tahmin istedik 
# alınan veriyi if bloğunda bizim atadığımız sayi değişkeniyle karşılaştırdık (eşit mi değil mi)
# eşit ise sayac değişkeniyle bulunduğu adımı, doğru bildiğini ve puanını yazdırdık
# (puan hesabı: can değişkeninin 100'e bölümünü sayaç - 1 ile çarp ver 100'den çıkar)
# if şartı sağlanırsa yukarıdaki belirtilen yazdırma işlemini uygula
# ve break metodu ile döngüyü durdur
# bunun yanında bir şartı daha kontrol et:
# rastgele sayı tahminden büyükse 'yukarı' yazdır 
# bu şartlar sağlanmıyorsa else altında belirtildiği gibi 'aşağı' yazdır
# yeni bir if bloğuyla hak değişkeninin sıfıra eşit olmasıyla kullanıcıya hakkının bittiğini ve tutulan sayıyı söyle

