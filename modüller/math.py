'''
import math
'''
#math modülünü dahil ettik

'''
value = dir(math)
'''
# math modülünün bütün bileşenlerini value değişkenine aktardık
'''
print(value)
'''
#math modülü içinde bulunan bütün fonksiyonları yazdırdık

'''
value2 = help(math)
'''
# math modülünün nasıl kullanılacağı bilgisine ulaşırız
'''
print(value2)
'''

'''
value3 = help(math.log10)
'''
#help ile fonksiyonları teker teker sorgulayabiliriz
'''
print(value3)
'''
'''
#ÖRNEK
deger = math.sqrt(49)
print(deger)
deger2 = math.factorial(5)
print(deger2)
deger3 = math.floor(5.9)
print(deger3)
'''
'''
import math as islem
'''
#math modülüne takma bir isim taktık
'''
a = islem.factorial(5)
print(a)
'''
'''
from math import *
'''
# ilgili modülden neleri çağıracağımı tek tek belirtebilirim
# yıldız ile hepsini çağırabilirim

'''
b = factorial(5)
'''
#bütün özellikleri import ettiğimiz için math modülünü belirtmeye gerek yok
'''
print(b)
'''
from math import factorial,sqrt
#ilgili modülden factorial ve sqrt fonksiyonlarını çağırdık
c = factorial(5)
print(c)

d = sqrt(49)
print(d)

def sqrt(x):
    print('x: ' + str(x))
# çağırılan modül altında modülün sahip olduğu bir fonksiyonla aynı isimde bir fonksiyon tanımlanırsa yeni fonksiyon modül fonksiyonunu ezer
# bu fonksiyon modül dışında tanımlanırsa ona verilen görevi yerine getirir ve modüldeki fonksiyon ile bağlantısı olmaz
    