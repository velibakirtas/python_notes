#1)Belirtilen bir kelimeyi belirtilen kadar ekranda yazdıran fonksiyonu yaz
def loopf(kl,lp):
    while lp > 0:
        print(kl)
        lp -= 1
loopf('v',3)        

#2)Kendisine gönderilen sınırsız sayıdaki parametreyi listeye çeviran fonksiyon
def lt(*params):
    liste = []
    
    for param in params:    
        liste.append(param)
    return liste
sonuc = lt(10,20,50,'veli')
print(sonuc)                      

#3)Gönderilen iki sayı arasındaki tüm asal sayıları bul

def asalc(x,y):
    asal = []
    for sayi in range(x,y+1):
        if sayi > 1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                asal.append(sayi)            
    return(asal)
deneme = asalc(2,10)     
print(deneme)   

#4)gönderilen sayının tam bölenlerinin bir listesini oluştur

def tamb(a):
    bölenler = []
    for bnn in range(2,a):
        if a % bnn == 0:
            bölenler.append(bnn)
    return bölenler
sonuc2 = tamb(15)        
print(sonuc2)