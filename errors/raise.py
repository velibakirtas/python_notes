# HATA NESNESİ OLUŞTURMA

x = 10

if x > 5:
    raise Exception("x 5'den büyük değer alamaz")
# raise => hata fırlatma komutu
# Exception => temel exception classı



def check_password(psw):
    import re
    # regular expression modülünü ekledik
    if len(psw) < 8:
        raise Exception('parola en az 7 karakterli olmalıdır')
    elif not re.search('[a-z]',psw):
        raise Exception('parola küçük harf içermelidir')
    elif not re.search('[A-Z]',psw):
        raise Exception('parola büyük harf içermelidir')
    elif not re.search('[0-9]',psw):
        raise Exception('parola rakam içermelidir')
    elif not re.search('[_@$]',psw):
        raise Exception('parola alpha numeric ifade içermelidir')         
    elif re.search("\s",psw): #\s re'de boşluk karakterini ifade eder
        raise Exception('parolada boşluk kullanmazsınız')
    else:
        print('geçerli parola')

password = '1_2A3456a7'
    
try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print('geçerli parola')        
    

class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            print('isim alanı fazla karakter içeriyor')
        else:
            self.name = name
            
p = Person('veliiiiiiiiiiiiiiiiii',1999)                
