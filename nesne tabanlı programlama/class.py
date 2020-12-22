#class

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
    #methods
        
#OBJECT(INSTANCE)
'''
p1 = Person()
'''
#person classından kopyalanmış bir objedir
#p1 objesi Person classının barındırdığı attributes ve metotları kullanabilir
'''
print(p1)
'''
#bir adrese tanımlı olduğuni ve tipinin person olduğunu belirten bir ifadeyle karşılaşırız   
'''
print(type(p1))
'''
#class olduğunu Person tipind olduğunu görebilriz

p2 = Person('veli',1999)
print(p2)
#Updating
p2.name = 'mehmet'#p2 objesinin parametrelerini cons yapılandırması ile ulaşarak güncelleyebiliriz
print(f'name: {p2.name} year: {p2.year} adress: {p2.adress}')
#init metodunda tanımladığımız üzere p2 selfi üzerinden tanımlanan name ve year bilgilerine ulaşabiliriz
