'''
ITEREAIBLE(TEKRARLANABİLİR)
'''

liste = [1, 2, 3, 4, 5]
# yukarıda oluşturulan liste objesi iterable(tekrarlanabilir) objedir
'''
for i in liste:
    print(i)
'''    
# liste objesini for döngüsünde kullanabilmemizin sebebi iterable obje olmasıdır

'''
ITERATOR OBJE OLUŞTURMA
'''

iterators =iter(liste)
# iter() fonksiyonu ile liste iterable objesinden iterator obje oluşturduk    
print(next(iterators))
# iterable objeden oluştutulan iteator objelere ulaştık ve yazdırdık
# her çapırma işleminde diğer bir iterator obje yazdırılır
print(next(iterators))
print(next(iterators))
print(next(iterators))
# ıterable objedeki elemandan fazla ıterator obje çağırmaya kalkarsak program hata döndürecektir

# daha önce bu işlemi farkında olmadan dngülerle yapıyorduk
for i in liste:
    print(i)
    
liste = [1, 2, 3, 4, 5]
    
# for döngüsünün arkasındaki mantığı inceleyelim:

liste = [1, 2, 3, 4, 5]
iterators =iter(liste)
while True:
    try:
        element = next(iterators)
        print(element)
    
    except StopIteration:
        break

class myNumber:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
list = myNumber(5,10)
# list'i myNumber classının bir objesi haline getirdik
# __iter__ fonksiyonu ile myNumber classının objeleri iterable
print(list)

for x in list:
    print(x)      
# for döngüsü her iterasyonda iterator objesinin __next__() fonksiyonunu metodunu çağırır
# iterator objesi her çağırıldığında bir sonraki elemanı geriye döndürür                  
    