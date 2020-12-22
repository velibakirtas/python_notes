
#1
deger = int(input('sayı girin: '))
degerD = (deger > 0) and (deger <= 100)
print(degerD)
print(f'sayı 0 ile 100 arasında mı: {degerD}')

#2
sayi = float(input('sayı girin: '))
sayiD = (sayi > 0) and (sayi % 2 == 0)
print(f'girilen sayı pozitif çift sayı mı: {sayiD}')

#3
email = 'vb@gmail.com'
password = '12345'

mail = input('email: ')
sifre = input('sifre: ')
onay = (mail == email) and (sifre == password)
print(f'hesaba giriş yapılabildi mi: {onay}')

#4
x = input('sayı1: ')
y = input('sayı2: ')
z = input('sayı3: ')

buyukX = (x > y) and (x > z)
print(f'x en büyük sayıdır: {buyukX}')

buyuky = (y > x) and (y > z)
print(f'y en büyük sayıdır: {buyuky}')

buyukZ = (z > x) and (z > y)
print(f'z en büyük sayıdır: {buyukZ}')

#5
a = float(input('vize 1: '))
b = float(input('vize 2: '))
c = float(input('final 1: '))

vize40 = ((a + b) * 40) / 100
final60 = (c * 40) /100
ort = (vize40 + final60) / 2

d1 = (ort >= 50) and (c >= 50)
print(f'öğrenci dersi geçti mi: {d1}')
d2 = (ort >= 50) or (c >= 70)
print(f'öğrenci dersi geçti mi: {d2}')

#6
person = {}

nameB = input('isim baş harfi: ')
name = input('isim: ')
surname = input('soyisim: ')
weight = float(input('kilo: '))
length = float(input('boy: '))

person[nameB] = {
    'ad' : name,
    'soyisim' : surname,
    'kilo' : weight,
    'boy' : length
}
print(person)
kutleind = (person[nameB]['kilo']) / (person[nameB]['boy'] ** 2)

indz = (kutleind>=0) and (kutleind<=18.4)
print(f'kişi zayıftır: {indz}')

indN = (kutleind>=18.5) and (kutleind<=24.9)
print(f'kişi normal kiloludur: {indN}')

indF = (kutleind >= 25.0) and (kutleind <= 29.9)
print(f'kişi fazla kiloludur: {indF}')

indO = (kutleind >= 30.0) and (kutleind <= 34.9)
print(f'kişi obezdir: {indO}')