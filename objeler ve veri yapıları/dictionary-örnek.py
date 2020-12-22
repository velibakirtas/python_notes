'''
ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02',
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 00 03'
    },
}

'''
#1) Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayın

#2) Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin


#1

students = {}

number = input('ogrenci no: ')
names = input('ogrenci adi: ')
surname = input('ogrenci soyadi: ')
phone = input('ogrenci tel: ')

students[number] = {
    'ad': names,
    'soyad:': surname,
    'phone': phone,
}
#students sözlük dizisinde ekledğimiz number value değerini anahtar olarak kullanıp bu anahtara yine anahtar value dizisinden oluşan bir value ekledik



number = input('ogrenci no: ')
names = input('ogrenci adi: ')
surname = input('ogrenci soyadi: ')
phone = input('ogrenci tel: ')

students[number] = {
    'ad': names,
    'soyad:': surname,
    'phone': phone,
}



number = input('ogrenci no: ')
names = input('ogrenci adi: ')
surname = input('ogrenci soyadi: ')
phone = input('ogrenci tel: ')

students[number] = {
    'ad': names,
    'soyad:': surname,
    'phone': phone,
}
# .update metodunu da kullanabilriiz
print(students)

#2
ogrNo = input('ogrenci Nu: ')
ogr = students[ogrNo]
print(ogr)