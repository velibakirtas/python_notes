# generator bellekte yer işgal etmeyen iterator üretir

# def cube():
#     result = []
    
#     for i in range(5):
#         result.append(i**3)
#     return result     
# print(cube())
# # fonksiyonun oluşturduğu liste bellek üzerinde bir yer tutar
# # kullanılacak eleman sayısı çoğaldıkça objeler bellek üzerinde daha fazla yer işgal edecektir   
# # bunu önlemek için generator yapı kullanabiliriz

def cube1():
    for i in range(5):
        yield i ** 3
        # yield keywordu ile üretilen değerlerin bellekte yer tutmasını önler
        # fonksiyonun ürettiği çıktılara bir daha ulaşılamaz
# yield ile döndürülen fonksiyon iterable obje ortaya çıkarır        

generator = cube1()
'''
iterator = iter(generator) 
'''
# iter fonksiyonu ile yield çıktısı olarak gelen iterable objeyi iterator objeye dönüştürdük
# generator iterable olan objeyi kendi içinde iteratore çevirir
# yani aslında iter fonksiyonunu kullanmaya da ihtiyaç yoktur

print(next(generator))  
print(next(generator))  
print(next(generator))  
print(next(generator))
# iterableların sahip olduğu next() metoduyla objelere ulaşıp yazdırdık

# artık iteratore çevrildiği için döngü ile de yazdırabiliriz
for i in generator:
    print(i)  

# Bu yapının en basit haliyle kullanımı aşağıdaki gibidir
def cube2():
    for i in range(5):
        yield i ** 3    

for i in cube2():
    print(i)        
    
# ne zaman generator üzerindeki bir bilgiyi istersek o anda yield çalışarak çıktı üretir

liste = [i**3 for i in range(5)]    
# comprehension bellekte yer tutan bir list oluşturur
# bunu generator şekilde tanımlamak istersek ;
liste2 = (i**3 for i in range(5))
print(liste2)
# comprehensive'in generator obje olmasının sağladık
# print ile yazdırdığımızda genreator bir obje olduğu bilgisini alırız
# haliyle bunu çalıştırmak için iteratorlerin next fonksiyo kullanmalıyız
# for döngüsü de next fonksiyonunu kendinde default olarak tanımlı tutar. yani for ile liste2 objelerine ulaşabiliriz
for i in liste2:
    print(i)