'''
DEKORATÖR FONKSİYONLAR
'''

# Bir fonksiyona özellik eklemek istediğimizde kullanılır
# bir özelliği birkaç farklı yerde kullanmak istiyorsak decorator fonksiyon oluşturup oluşan decorator fonksiyonu birçok fonksiyon ile ilişkilendirebiliriz

def my_decorator(func):
    def wrapper():
        print('fonksiyondan önceki işlemler')
        func()
        print('fonksiyondan sonraki işlemler')
    return wrapper

def sayHello():
    print('hello')
    
def greeting():
    print('greeting')        


sayHello = my_decorator(sayHello)
# sayHello foksiyonunu my_decorator fonksiyonu ile ilişkilendirdik/yapılandırdık
# yani sayHello fonksiyonunu my_decorator fonksiyonunun parametresine atarak oluşan çıktı tekrar sayHello fonksiyonu içine atıldı
sayHello()   
# sayHello fonksiyonunu tekrar kullandığımızda sayHello fonksiyonu my_decorator fonksiyonu ile yeniden yapılnadırılarak kullanıldı

# bu işlemi kısaltmak için kullanılan kw var
@my_decorator
def sayHello1():
    print("hello")
# @ operatörü ile @ ile belirtilen fonksiyonun içine oluşturacağımız yeni fonksiyonu gönderebiliriz
# yukarıda yapılan işlmein kısa halidir    
sayHello1()

@my_decorator
def sayHello2(name):
    print("hello",name)
# göndereceğimiz fonksiyonda parametre kullanabilmek için fonksiyonun bulunduğu fonksiyon localinde bu parametrelerin çağırılması gerektir
# bu kullanım hata döndürecektir
# sayHello2('veli')

# aşağıdaki şekilde bir kullanım dönecek hataya engel olur   
def my_decorator1(func):
    def wrapper(name):
        print('fonksiyondan önceki işlemler')
        func(name)
        print('fonksiyondan sonraki işlemler')
    return wrapper

@my_decorator
def sayHello3(name):
    print('hello', name)

sayHello3('veli')    

import math
import time


def usalma(a,b):
    start = time.time()
    time.sleep(1) # fonksiyonu 1 saniye uyuttuk
    print(math.pow(a,b))
    
    finish = time.time()
    print('fonksiyon'+ str(finish - start)+ 'saniye sürdü')


def faktoriyel(num):
    start = time.time()
    time.sleep(1) 
    print(math.factorial(num))    
    finish = time.time()
    print('fonksiyon'+ str(finish - start)+ 'saniye sürdü')
   
# oluşturulan fonksiyonların sadece ana görevlerini yapmasını istediğimizi varsayarsak:
# yani zaman hesaplamak için farklı fonksiyon tanımlamak istersek ve ana fonksiyonları bunun içinde kullanmak istersek:
def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print(func.__name__ +' fonksiyonu ' +  str(finish - start)+ ' saniye sürdü')
    return inner    

@ calculate_time        
def usalma(a,b):
   
    print(math.pow(a,b))
 

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))    
    
usalma(2,2)    
faktoriyel(5)