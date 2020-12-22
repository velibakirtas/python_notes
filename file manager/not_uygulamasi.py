def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ogrenciAdi = liste[0]
    notlar = liste[1]
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1 + not2 + not3)/3
    
    if ortalama > 90 and ortalama <= 100:
        harf = 'AA'
    elif ortalama >=85 and ortalama <=89:
        harf = 'BB'
    elif ortalama >=65:
        harf = 'CC'
    else:
        harf = 'FF'
    return ogrenciAdi  + ': ' + harf + '\nb'                               

def not_oku():
    with open('sinav_notlari.txt', 'r',encoding='utf-8') as file:
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input('Öğrenci Adı: ')
    soyad = input('Soyadı: ')
    not1 = input('not 1: ')
    not2 = input('not 2: ')
    not3 = input('not 3: ')
    with open('sinav_notlari.txt', 'a', encoding='utf-8') as file:
        file.write(ad +' '+ soyad +': ' + not1 +','+ not2 +','+not3 + '\n')
    
    
    
def not_kayit():
    pass

while True:
    islem = input('1- Notları Oku\n2- Notları Gir\n3- Notları Kaydet\n4- Çıkış: ')
    if islem == '1':
        not_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        not_kayit()
    elif islem == '4':
        pass
    else:
        break