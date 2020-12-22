x = 20
y = 20

if x > y:
    print("x y'den büyüktür")
else:
    print("y x'den büyüktür.")   
    
    
if x > y:
    print("x y'den büyüktür")
elif x==y:
    print("x y'ye eşittir.")
  
else:
    print("y x'den büyüktür.")
    
#Bir durumun sağlanması birden fazla koşula bağlanmışsa elif komutu kullanılır

num = float(input('sayı girin: '))

if num > 0:
    print('sayı pozitiftir')
elif num < 0:
    print('sayı negatiftir')    
else:
    print('sayı 0 dır')    
#num 0' dan büyükse sayı pozitiftir yazdır 
#Tekrar kontrol et sayı 0' dan küçükse sayı negatiftir yazdır
#her ikisi dışındayken sayı 0'dır yazdır.

