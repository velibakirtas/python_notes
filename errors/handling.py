# error
'''
print(a) => NameError
'''

'''
int(1a2) => ValueError
'''

'''
print(10/0) => ZeroDivisionError
'''

'''
print('denem'e) => SyntaxError
'''





# error handling(hata yönetimi)

try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except ZeroDivisionError as z: #alınacak hatanın paydanın 0 olmasından kaynaklı olacağını tanımladık
    #alınabilecek hata bir obje olarak değişkene tanımlanabilir  
    print('y sayısı 0 girilemez')
    print(z)
#hata olmasının öngördüğümüz işlemleri try ile başlatarak programın çalışmasını engelleyen faktörler düzeltilebilir

# except ile öngördüğümüz hata türünün ne olduğunu belirtiriz     
except ValueError: #alınacak hatanın x veya y'ye sayıdan farklı bir değer atamadan kaynaklanacağını tanımladık
    print('x ve y için sadece sayısal değer girmelisiniz') 
    
# alınabilecek hataların hepsini tek bir except satırında toplayabiliriz


try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except:
    print('hatalı bilgi girdiniz')
    
#exceptte herhangi bir hata türü belirtmeden de yapı kullanılabilir
#fakat alınacak hatanın ne olduğu saptanılamaz ve obje olarak kullanılamaz


try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except:
    print('hatalı bilgi girdiniz')
else:
    print('her şey yolunda')    
    
# Eğer trydan bir hata dönmezse else except'e bağlı olarak çalışır ve ifadeyi yazdırır.
 
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as cl:
        # Exception içinde hataların tümünü barındıran bir classtır
        #Dolayısıyla hata türlerini yazmak yerine ait olduğu classı tanımlayabiliriz
        print('hatalı bilgi girdiniz')
        print(cl)
    else:
        break
    finally:
        print('try except sonlandı')
        #finally ile döngü hangisiyle karşılaşırsa karşılaşsın belirtilen işlem yapılır
        
#while döngüsüne True değer vererek # x ve y'ye girilen değerler yanlış olduğu sürece sürekli dönecek sonsuz bir döngü oluşturduk
# Eğere girilen değerler doğru olursa belirtilen işlem yapılacak ve döngü sona erecek    
  
