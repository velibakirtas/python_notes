#1

isim = input('isim: ')
yas = int(input('yas: '))
egitim = input('eğitim düzeyi: ')

'''
if (yas >= 18) and (egitim == 'lise' or egitim == 'uni'):
    print(f'{isim} ehliyet alabilirsin')
else:
    print(f'{isim} ehliyet almaya uygun değilsin')
    
    '''
                        #ya da

if yas>=18:
    if (egitim == 'lise' or egitim == 'uni'):
        print(f'{isim} ehliyet alabilir')
    else:
        print(f'{isim} ehliyet alamazsın, egitim durumun yetersiz')                            
else:
    print(f'{isim} ehliyet alamazsın, yaşın küçük')     
    
    
#2

y1 = int(input('yazılı1: '))    
y2 = int(input('yazılı2: '))
s = int(input('sözlü: '))

ort = (y1 + y2 + s) / 3

if (ort >= 0) and (ort <= 24):
    print('0')
elif (ort >= 25) and (ort <= 44):
    print('1')
elif (ort >= 45) and (ort <= 54):
    print('2')
elif (ort >= 55) and (ort <= 69):
    print('3')    
elif (ort >= 70) and (ort <= 84):    
    print('4')
elif (ort >= 85) and (ort <= 100): 
    print('5')
else:
    print('yanlış bigi girdiniz')  
    
    
#3

days = int(input('aracın trafikte bulunduğu gün sayısı: '))

if days <= 365:
    print('1. servis aralığı')
elif days > 365 and days <= 365*2 :
    print('2. servis aralığı')    
elif days >365*2 and days < 365*3 :
    print('3. servis aralığı')
else:
    print('Girdiğiniz bilgileri yenileyin')



#DATETİME MODÜLÜ
import datetime
tarih = input('aracın trafiğe çıkış tarihi (2018.04.19): ')
tarih = tarih.split('.')
print(tarih)
#kullanıcıdan alınacak bilgiyi . bulunan yerlerden bölüp gün ay yıl verilerini ayrı elde ettik.

trafigeCikis = datetime.datetime (int(tarih[0]), int(tarih[1]), int(tarih[2]))
#datetime.datetime metodu ile elimizdeki veriyi datetime modülüne uygun hale getirdik.

simdi = datetime.datetime.now()
#datetime.datetime.now() metodu ile bir değişkene şimdiki tarihin değerlerini datetime modulüne uygun şekilde atadık.

fark = simdi - trafigeCikis
days = fark.days
#.days metodu ile, önce oluşturulmuş datetime(burada iki datetime arasındaki fark ölçüldüğü için tipi deltatime) verisinden sadece gün bilgisini ayıklayabiliriz

if days <= 365:
    print('1. servis aralığı')
elif days > 365 and days <= 365*2 :
    print('2. servis aralığı')    
elif days >365*2 and days < 365*3 :
    print('3. servis aralığı')
else:
    print('Girdiğiniz bilgileri yenileyin')