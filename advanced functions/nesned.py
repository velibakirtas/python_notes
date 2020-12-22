'''
İÇ İÇE FONKSİYONLAR
'''

def greeting(name):
    print('hello', name)

greeting('veli')
# fonksiyonu çalıştırdık ve parametredeki veri ile fonksiyondan çıktı aldık

print(greeting)
# oluşsturduğumuz fonksiyonun bir nesne olarak ramde yer tuttuğunu görüntülemek için print ile gözlemledik

sayHello = greeting
# greeting fonksiyonunun sayHello değişkenine attık
print(sayHello)
# sayHello değişkeninin adresini görmek için print ile gözlemledik
print(greeting)
# greeting fonksiyonunun adresini tekrar görmek için print ile gözlemledik

# her iki objenin de aynı adrese sahip olduğu görülüyor.

# artık sayHelloyu da fonksiyon olarak kullanabiliriz. greeting fonksiyonu ile aynı işlemi gerçekleştirir

sayHello('mehmet')

del sayHello
# sayHello fonksiyonunun tutulduğu adresi değil tanımlamayı siler
# yani greeting fonksiyonu hala ramde bir yer tutar
print(greeting)


def outer(num1):
    print('outer')
    def inner_increment(num1):
        print('inner')
        return num1 + 1
    
    
outer(10)
# outer fonksiyonunu çağırdığımızda sadece outer fonksiyonu işlevini yapar.Yani inner_increment fonksiyonunu çalıştırmaz
# görüldüğü üzere çalıştırıldığında döndürülen veri 'outer' dır    

# ENCAPSULATİON
# inner_increment fonksiyonunu outer fonksiyonu içinde çalıştırabilmemiz için oluşturulan inner_increment fonksiyonunu outer fonksiyonu içinde çağırıyor olmamız gerekiyor
def outer1(num1):
    print('outer1')
    def inner_increment1(num1):
        print('inner1')
        return num1 + 1
    num2 = inner_increment1(num1)
    print(num1, num2)
outer1(10)    

#inner_increment(10)
# inner_increment fonksiyonu yalnız çağırmayı denersek hata döndürülecektir
# bunun sebebi sadece outer1 scopunda çalıştırılacak olan bir fonksiyon olmasıdır

def factorial(num):
    def inner_factorial(num):
        if num <=1:
            return num
        return num * inner_factorial(num-1)
    return inner_factorial(num)
print(factorial(5))