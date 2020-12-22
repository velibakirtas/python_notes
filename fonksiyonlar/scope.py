#Tanımladığımız değişkenlerin Local ve Global olarak nasıl tanımlanacağını inceleyeceğiz

#global scope
x = 'global x'

def function():
    #local scope
    x = 'local x'
    print(x)
function()    
print(x)
#fonksiyon içinde değişkene farklı bir değer atadık
#fonksiyonu çağırdık sonra x'i yine yazdırdık fakat x'de bir değişiklik olmadı

#Bunun sebebi fonksiyonların yeni bir tanımlama alanı kullanmasıdır
# fonksiyon için yeni bir tanımlama alaın hazırlanır
# çalışma alanı farklı olduğu için fonksiyondaki değişkenler dışarıdaki değişkenlerini etkilemez
# fonksiyon içinde(local scope) kullanılan yazdırma işleminde fonksiyonda yapılan değişiklik uygulanmıştır
# fakat fonksiyonun dışına(global scope) çıkıldığında yazdırdığımız x değişkeni dışardaki tanımlı olduğu değeri yazdırır

def function2():
    print(x)
function2()    
#burada local scope'da herhengi bir tanımlama olmadığı için fonksiyon için de global olan dışarıda(global scope) tanımlanan değeri alır
#fonksiyonda değişkene yeni bir değer tanımlandığında globaldeki değer yerine localdeki yeni değeri kullanır

########################

#global scope
name = 'veli'

def isimd(isim):
    #local scope
    name = isim
    print(name)
isimd('mehmet')    
print(name)

#####################

name2 = 'global string'

def greeting():
    name2 = 'veli'
    
    def hello():
        print('hello '+ name2)
    hello()        
    
#name2 değişkenine 'global string değerini attık
#greeting adında bir fonksiyon oluşturup name2 değişkeninin değerini değiştirdik
# fonksiyon içinde hello adında bir fonksiyon daha oluşturduk
#bu fonksiyonda print ile hello + name2(greeting fonksiyonunda yeniden tanımlanmıştı)     
#oluşturduğumuz bu hello fonksiyonunu birn önceki greeting fonksiyonu sonuna ekledik
greeting()    
print(name2)
#fonksiyonu çalıştırdığımızda 'hello veli' diye bir sonuç alacağız
#name2 değişkenini dışarıda çalıştırdığımızda ise 'global string' sonucunu alırız
#greeting fonksiyonunun global scopeu fonksiyon dışıdır
#hello fonksiyonunun global scopeu içinde bulunduğu greeting fonksiyonudur.
#yani name2 değişkeni greeting fonksiyonu içinde değiştirilmeden kullanılsaydı dışardaki değerini tutmaya devam ederdi
#greeting fonksiyonunda name2 değeri değiştirildiği için ve hello fonksiyonu da greeting fonksiyonunu global scope olarak aldığı için name2 değişkeni helloda da 'veli' değerini aldı

######################

x = 50
def test(x):
    print(f'x: {x}')
    
    x =100
    print(f'changed x to {x}')
test(x)    

########

x = 50
def test2():
    global x
    print(f'x: {x}')
    
    x =100
    print(f'changed x to {x}')
test2()    
print(x)
#global scopetaki değişkeni fonksiyon içinde kullanabilmek için global keywordunu kullanmamız gerekir
#global kw ile fonksiyon içinde yapılan bütün işlemler artık dışarıdaki değişken üzerinde çalışır