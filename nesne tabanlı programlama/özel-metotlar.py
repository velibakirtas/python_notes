
myList = [1,2,3]
'''
myString = 'my string'

print(len(myList))
print(len(myString))
#yukarıdaki objelerin classları len metoduna sahiptir.
'''
#kendimiz bir class oluşturalım
class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('obje oluşturuldu')
        
    def __str__(self):
        return f'{self.title} by {self.director}'    
    
    def __len__(self):
        return self.duration    

m = Movie('interstellar', 'Nolan', 180)


'''
print(len(m))
'''
#Bu kullanımda hata alırız bunun sebebi oluşturduğumuz Movie classında len metodunun bulunnmamasıdır

#classa len metodunu ekledik
print(len(m))

print(myList)
print(m)

print(str(myList))
print(str(m))
#biz bir veriyi yazdırdığımızda bunu bulunduğu classın içinde bulunduğu __str__ metodu ile yapar
#class içinde bir __str__ metodu tanımlı değilken yazdırdığımızda objenin adresini verirken __str__ metodunu ekleyince parametreler doğrultsunuda bir str ifade yazdırır.

del m
print(m)
#del ile m objesini sildik
#m objesini yazdırmak istediğimizde, del ile sildiğimiz için m objesine ulaşamayız 