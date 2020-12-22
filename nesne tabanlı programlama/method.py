class Person:
    pass #pass kw ile boş olan class ifadeden hata almamk için pass yer tutucusunu kullanabilriz
    #ATTRİBUTES(ÖZELLİK)
    #A)Class Attributes
    adress = 'no information'
    #bir özelliği constructor içinde tanımlamak yerine direkt class attribute olarak tanımlayabiliriz
    #genelde her zaman kullanılmayacak özellikler burada tanımlanır
    
    #cunstructor(yapıcı metot)
    def __init__(self,name,year):  #Self = Classtan türetilen herhangi bir obje
        #selften sonra gelen parametreler self üzerine eklediğimiz attributeslerdir(tanımmlanacak olan objeler üzerine ekleyeceğimiz özelliklerdir)
        self.name = name
        self.year = year
        print('init metodu çalıştı')
        
    #methods(instance)
    def intro(self):
        print('Hello There I am ' + self.name)
    #Person classına intro isminde bir metot ekledik   
    #metot parametresi boş kalırsa hata alrız
    #metotun çalışması için instance metot olması gerekir
    #bunun için constructorda tanımladığımız obje referansının(self) girilmesi gerekir 
    
    def calculateAge(self):
        return (2020 - self.year)    
    
#OBJECT(INSTANCE)
p1 = Person('mehmet',2004)
p2 = Person('veli',1999)

p1.intro()
p2.intro()

print(f"adım : {p1.name}, yaşım : {p1.calculateAge()}")
print(f"adım : {p2.name}, yaşım : {p2.calculateAge()}")


class Circle:
    #Class object attribute
    pi = 3.14
    
    #constructor
    def __init__(self,yaricap = 1):
        self.yaricap = yaricap
    
    #methods
    def cevreHesapla(self):
        return (2*self.pi*self.yaricap)
    
    def alanHesap(self):
        return self.pi * self.yaricap**2
c1 = Circle()

cev = c1.cevreHesapla()
al = c1.alanHesap()
print(cev)
print(al)     

c2 = Circle(7)

cev2 = c2.cevreHesapla()
al2 = c2.alanHesap()
print(cev2)
print(al2)