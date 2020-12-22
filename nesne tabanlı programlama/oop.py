#OBJECT ORİENTED PROGRAMİNG(OOP) (NESNE TABANLI PROGRAMLAMA)

#Class
#Instance(obje)

lst = [1,2,5]
print(type(lst))

#lst listesi list classından üretilmiş olan bir instancedir.
#Class = Daha önceden kütüphane içerisinde oluşturulmuş belli nitelikleri ve bell, metotları içinde bulunduran yapı

lst2 = [1,4,5,6]
#oluşturduğum her yeni liste list classının özelliklerini barındıran bir kopyadır

#Classlar kendince metotlara sahiptir.
#classtan türeyen her instance classın barındırdığı metotları kullanabilir
lst.append(9)

#Geliştiriciler kendi classlarını da oluşturabilir
'''
class => person(name, yearOfBirth, job, calculateAge())
'''
#örnek olarak person isimli bir class oluşturduğumuzu düşünelim
#class içinde bulundurduğu her metotu her instancei için kullanılır kılar
'''
veli(veli, 1999, student)
'''
#oluşturduğumuz bu ifade person classının bir kopyası olan veli instancedir
#person classında bulunan calculateAge metodu person classının veli instancei için de tanımlanır ve kullanılabilir(veli.calculateAge)

#objeye bağlı olmayan kod bloklarına fonksiyon denir