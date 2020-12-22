#1 Girilen sayının 0-100 arasında olup olmadığını kontrol et
'''
sayi = int(input('sayı: '))
sayiAr = (sayi > 0) and (sayi <= 100)
print(f'sayi 0 ile 100 arasında mı: {sayiAr}')
'''
 
sayi = int(input('sayı: '))
if (sayi > 0) and (sayi <= 100):
    print(f'sayı pozitif bir sayıdır')
elif sayi == 0:
    print(f'sayı 0 a eşittir.')
else:
    print('sayı negatiftir')


#2 Girilen sayı pozitif çift sayı mı
'''
sayi1 = int(input('sayı giriniz: '))
sayiC = (sayi1 > 0) and (sayi1 % 2 == 0)
print(f'sayı pozitif çift sayı mı: {sayiC}')
'''

sayi1 = int(input('sayı giriniz: '))

if (sayi1 > 0) and (sayi1 % 2 == 0):
    print(f'sayı pozitif çift sayıdır')
else:
    if (sayi1 < 0):
        print('sayı negatiftir')
    else:
        if (sayi1 % 2 != 0):
            print(f'sayı çift değildir')
        else:
            print(f'yeniden sayı giriniz')


#3 email ve parola bilgileri ile giriş kontrolü yap

email = 'mb@gmail.com'
password = '2004'

mail = input('email: ')
sifre = input('sifre: ')


'''
onay = (mail == email) and (sifre == password)
print(f'Giriş başarılı mı: {onay}')
'''

if (mail == email):
    if (sifre == password):
        print(f'giriş başarılı')
    else:
        print(f'şifre yanlış')
else:
    print(f'email yanlış')
    
   
#4 Girilen 3 sayıyı büyüklük açısından karşılaştır


a = int(input('sayi1: '))
b = int(input('sayi2: '))
c = int(input('sayi2: '))

if (a > b) and (a > c):
    print(f"en büyük sayı 'a: {a}' dır")
else:
    if (b > a) and (b > c):
        print(f"en büyük 'b: {b}' dir")
    else:
        if (c > a) and (c > b):
            print(f"en büyük sayı 'b: {c}'dir")
        else:
            print(f'yeniden hesaplatın.')


'''
buyukA = (a > b) and (a > c)
print(f'a en büyük sayıdır: {buyukA}')

buyukB = (b > a) and (b > c)
print(f'b en büyük sayıdır: {buyukB}')

buyukC = (c > a) and (c > b)
print(f'c en büyük sayıdır: {buyukC}')
'''

#5 2 vize notu(%40) ve final notu(%60)alıp  ortalama hesapla
#ortalama 50 ve üstüyse geçti altıysa kaldı yazdır
# final notu en az 50 olmalıdır
#final 70 işe ortalamanın önemi yok

v1 = int(input('vize1: '))
v2 = int(input('vize2: '))
f = int(input('final: '))

ort = ((v1 + v2) / 2) * 0.6  + (f * 0.4)
 
if ort >= 50:
    if f >= 50:
        print(f'not ortalamanız {ort}, dersi geçtiniz')
    else:
        print(f'final notunuz: {f} dersi geçmek için yetersiz ')
elif f >= 70:
    print(f'final notunuz: {f} dersi geçmek için yeterli')        
else :
    print(f'not ortalamanız {ort}, dersi geçmek için yetersiz')    


#6 Ad, kilo, ve boy bilgilerini alıp vke hesapla bulunduğu grubu belirleyip yazdır

name = input('isim: ')
weight = float(input('kilo: '))
length = float(input('boy: '))

vke = weight / (length ** 2)

if (vke >= 0) and (vke <= 18.4):
    print(f'Sayın {name} vücut kitle endeksiniz {vke}, kilo değerlendirmeniz zayıf')
elif (vke >= 18.5) and (vke <= 24.9):
    print(f'sayın {name} vücut kitle endeksiniz {vke}, kilo değerlendirmeniz normal')        
elif (vke > 24.9) and (vke <= 29.9)    :
    print(f'sayın {name} vücut kitle endeksiniz {vke}, kilo değerlendirmeniz fazla kilolu')
elif (vke >= 29.9 ) and (vke <= 34.9)    :
    print(f'sayın {name} vücut kitle endeksiniz {vke}, kilo değerlendirmeniz obez')
else:
    print('lütfen bilgilerinizi tekrar giriniz')    