liste = ['1', '2', '5a', '10b', 'abc', '10', '50']

'''
SON SORUYU MATH MODÜLÜNÜ KULLANARK YARIN TEKRAR YAP
'''

#1) liste elemanları içindeki sayısal değerleri bulunuz 

'''
convertible = []
notConvertible = []
for sayi in liste:
    try:
        a = int(sayi)
        convertible.append(sayi)
        #print(a)
    except Exception as numeric:
        continue           
print(convertible)    


#2) Kullanıcı 'q' değerini girmedikçe aldığınız her değerin sayı olduğundan emin olun aksi halde hata mesajı yazın

while True:
    sayi = input('deger giriniz: ')
    if sayi == 'q':
        break

    try:
        b = int(sayi)
    except Exception as veriHata:
        print('lütfen bir sayı giriniz') 
        continue
    
#3) girilen parola içinde türkçe karakter hatası
    
def sifre_kontrol(sifre):
    import re
    if re.search('[ıüğşöç]',sifre):
        raise Exception('parolanız Türkçe karakter içeremez')
    else:
        print('giriş başarılı')                     
sifreGir = input('şifre giriniz: ')
try:
    sifre_kontrol(sifreGir)
except Exception as turkish:
    print(turkish)
'''
#4) Kullanıcıdan alınan sayıların faktoriyelini alırken gereken hataları ver

def check_num(sayi):
    int(sayi)
    if not int(sayi):
        raise Exception('Girdiğiniz değer sadece sayılardan oluşmalıdır')
      
    if sayi < 0:
        raise Exception('Pozitif bir sayı giriniz')     
    else:        
        import math
        int(sayi)
        math.factorial(sayi)
    
no = input('faktoriyeli alınacak bir sayı giriniz: ')    
try:
    check_num(no)    
except Exception as fac:
    print(fac)    