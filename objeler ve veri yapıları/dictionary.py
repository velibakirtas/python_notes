#dictionary liste yöntemi key(anahtar) - value(değer) şeklşinde çalışır

#örneğin
'''
34 => istanbul    41 => kocaeli
'''

#dictionary liste türünü kullanmadan plakalar ve şehirleri eşleştirelim

plakalar = [34, 41]
sehirler = ['istanbul', 'kocaeli']

print(plakalar[sehirler.index('istanbul')])
print(plakalar[sehirler.index('kocaeli')])

#dictionary listesi aşağıdaki şekilde oluşturulur.
dictionary = {'key' : 'value'}

plakalarD = {'kocaeli': 41, 'istanbul': 34}
print(plakalarD['kocaeli'])
print(plakalarD['istanbul'])
#key değeri olarak şehir ismini value olarak da plaka numaralarını tanımladık.

plakalarD['ankara'] = 6
print(plakalarD)
#dictionary dizi içine 'ankara'= key, 6= value olarak ekledik

plakalarD['kocaeli'] = 'new value'
print(plakalarD)
#dictionary dizi içinde bulunan bir elemana yeni bir value atadık

users = {
    'velibakirtas': {
        'age': 21,
        'roles': ['admin','user'],
        'email': 'veli@gmail.com',
        'adress': 'istanbul',
        'phone': 124533,
    },
    'mehmetbakirtas': {
        'age': 16,
        'roles': ['user'],
        'email': 'mehmet@hotmail.com',
        'adress': 'karaman',
        'phone': 448348,
    }
}

print(users['velibakirtas'])
print(users['mehmetbakirtas']['email'])
print(users['velibakirtas']['roles'][0])