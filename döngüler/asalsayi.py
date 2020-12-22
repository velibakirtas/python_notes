'''
    Soru: Girilen bir sayının asal olup olmadığını bul
'''    

sayi= int(input('sayı giriniz: '))
asalmi = True

if sayi  == 1:
    asalmi = False
    
for i in range(2, sayi):
    if sayi % i == 0:
        asalmi = False
        break
if asalmi:
    print(f'{sayi} sayısı asaldır')        
else:
    print(f'{sayi} sayısı asal değildir')    
    
# kullanıcıdan bir sorgulanacak sayı bilgisi alıyoruz ve sayi değişkenine tanımlıyoruz(asal mı değil mi)    
# if bloklarını kontrol etmek için asalmi değişkenine True değerini tanımlıyoruz
# 1 sayısı istisna olduğu için ona ayrı bir if bloğu oluşturuyoruz
# eğer sayi 1'e eşitse asalmi değişkenini False'a çevirip en sondaki if bloğu doğrultusunda devam ediyoruz(sondaki if bloğu asıl sonuçları yazdıracak)
# 1 için inceleme bittikten sonra for döngüsü başlatıyoruz
# range metodu ile 1 ile girilen sayi arasındaki bütün elemanları i' ye atıyoruz
# for döngüsü altında bir if bloğu başlatıyoruz
# sayi değişkeninin i elemanlarıyla bölümünden kalan 0 ise :
# asalmi değişkenine False değerini atıyoruz 
# asalmi değişkeni daha sonra oluşturulacak bir başka if bloğunda çalıştırlacak
# break metodu ile for döngüsünü bitiriyoruz
# döngüden ayrı yeni bir if bloğu oluşturup asalmi değişkeninin aldığı değerleri burada değerlendiricez
# asalmi değişkenini if bloğunda inceliyoruz True değer alması halinde kullanıcıya sayının asal olduğunu yazdırıyoruz
# eğer asalmi değişkeni döngü altındaki şart bloklarından False değeri almış ise kullanıcıya sayi asal değildir yazdırıyoruz.
