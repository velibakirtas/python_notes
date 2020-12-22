# INHERİTANCE(KALITIM)

#Classların birbirinden miras alması ile ilgili bir durumdur
'''
Person => name, lastname, age, eat(), run()
'''
#bunlar Person classının attributesi ve metotlarıdır.

#yeni oluşturacağımız bir classta bunların bulunmasını istiyoruz varsayalım
#yeni classta bunları yenidne tanımlamak yerine Person classından miras olarak alabiliriz
'''
Student(Person), Teacher(Person)
'''
#Person için tanımlanan bütün attributes ve metotlar Student ve Teacher classlarınında bir parçası olacak
#Bunların yanında ekstadan yeni attributes ve metotlarda eklenebilir
#bunlardan birine eklenen yeni attribute ve metot Person classını ilgilendirmez

class Person():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        print('person created')
        
    def benkimim(self):
        print('ben senim')        
        
class Student(Person)        :
    #Person classının sahip olduğu bütün niteliklere Student classı da sahiptir.Student classına person classının haricinde yeni nitelikler eklenebilir
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.stnumber = number
        print('student created')
    #Student classında kullanılan init metodu, içine eklediğimiz Person classının init metodunu ezer.     
    #Student classında Person classını çalıştırabilmek için Student classının init metodunda Person classını çalıştırmamız gerekir   

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        #super() metodu ile Person classını Teacher classına miras verebiliriz
        self.branch = branch

p1 = Person('veli','bakirtas')
s1 = Student('memo','bakirtas',4604)    

print(f"adım {p1.fname}, soyadım {p1.lname}")
print(f"kardeşimin adı {s1.fname}, soyadı {s1.lname}, okul numarası {s1.stnumber}")

p1.benkimim()
s1.benkimim()
# benkimim metodunu Person classında oluşturmama rağmen Student classının objesi olan s1de de çalışır
#bunu sebebi Student classının, Person classının niteliklerine sahip olmasıdır


