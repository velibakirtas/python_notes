'''
FONKSİYONDAN FONKSİYON DÖNDÜRME
'''


def usalma(num):
    def inner(power):
        return num ** power
    return inner
a = usalma(2)
# usalma(2) yi a ya atarak local scopetaki inner fonksiyonunu a değişkenine tanımladık
# yani burada a objesi usalma fonksiyonu localindeki inner fonksiyonu haline geldi
print(a(3))

b = usalma(3)
# usalma fonksiyonuna gönderdiğimiz parametre ile tabanı belirledik
print(b(4))
# usalma fonksiyonunun localinde bulunan inner fonksiyonu(b) ile de kuvveti belirledik


def yetki_sorgula(page):
    def inner(role):
        if role == 'admin':
            return '{0} rolü {1} sayfasına ulaşabilir.'.format(role, page) 
        else:
            return '{0} rolü {1} sayfasına ulaşamaz.'.format(role, page)
    return inner        
    
admin_check = yetki_sorgula('yönetim')
print(admin_check('admin'))            
print(admin_check('user'))


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam +=i
        return toplam          
    
    def carpma(*args):
        carpım = 1
        for i in args:
            carpım *= i
        return carpım
    
    if islem_adi == 'toplama':
        return toplam
    else:
        return carpma

toplama = islem('toplama')
print(toplama(1,2,3,4,5))

carpma = islem('carpma')
print(carpma(1,2,3,4,5))      