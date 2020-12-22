import os

system = os.name
print(system)
# kullanılan işletim sistemini gösterir(nt windows işletim sistemine karşılık gelir)

'''
++++++++++++++++++++++++++++++++++  etkin dizin öğrenme   ++++++++++++++++++++++++++++++++++
'''
folder = os.getcwd()
print(folder)
# ilgili dosyanın hangi klasör içinde bulunduğu bilgisini verir(os-module.py)

#-----------------------------------------------------------------------------------------------

'''
***************  os.chdir() metodu  *******************
'''

# sözkonusu dizini değiştirmemizi sağlar
os.chdir('C:\\')
# yapılacak işlemlerin uygulanacağı dizini seçtik


print(os.getcwd())
# getcwd() modülü ile kontrol ettiğimizde C dizini içinde olduğumuzu görebiliriz

'''
+++++++++++++++++++++++++++++++  klasör oluşturma  ++++++++++++++++++++++++++++++++++++
'''

os.mkdir('new_directory')
# mkdir()metodu ile yeni bir klasör oluşturabiliriz
# klasörü C dizininde oluşturduk. bunun sebebi daha önce chdir() metodu ile ilgili klasörün değiştirilmesidir
#-----------------------------------------------------------------------------------------------------


'''
++++++++++++++++++++++++++++++  iç içe bulunan dizinde dolaşma  +++++++++++++++++++++++++++
'''

os.chdir('..') 
# bir üst dizine çıkmamızı sağlar
print(os.getcwd())

# birden fazla dizin geriye çıkacaksak;
os.chdir('../..') # şeklinde yapabiliriz
print(os.getcwd())
#-----------------------------------------------------------------------------------------

'''
******************************  makedirs() metodu *************************************
'''

# çoklu iç içe klasör oluşturmamızı sağlar
os.makedirs('new_directory/denemeklasörü')####
# ilgili dizinde new_directory adlı bir klasör, onun içine de deneme klasörü adlı bir klasör oluşturduk

# chdir metodu ile dizin değiştirerek istenilen dizine klasör eklenebilir
# ya da makedirs() metodu üzerinde de klasörün oluşturulacağı yol belirlenebilir
os.makedirs('C:\\deneme-klasör/deneme-içklasör')####
# -----------------------------------------------------------------------------------------


'''
+++++++++++++++++++++++++++++++++++++++++ klasörü yeniden isimlendirme ++++++++++++++++++++++++++++
'''

os.rename('deneme-klasör','değiştirildi')


'''
+++++++++++++++++++++++++++++++   klasörde listeleme  ++++++++++++++++++++++++++++++++
'''

print(os.listdir()) # ilgili dizin içindekileri listeler
# chdir metodu ile dizin değiştirilmişse o dizin üzerinde çalışır
listing = os.listdir('C:\\')
# parametrede belirtilen dizindeki klasörleri ve dosyaları listeler

# dosyalar arasında bir filtreleme yapmak istersek;
for dosya in os.listdir():
    if dosya.endswith('.py'): #endswith metodu ile .py ile biten dosyaları seçtik ve yazdırdık
        print(dosya)


'''
******************************   stat() metodu   *****************************************
'''

import datetime

att = os.stat('datetime-module.py')
print(att)
# parametrede verilen dosya hakkında bilgi edinmemizi sağlar

size = att.st_size/1024
# size dosyanın byte türünden büyüklüğünü verir
# biz bunu 1024'e bölerek mb haline getirdik
print(size)

ctime = att.st_ctime
print(ctime)
# oluşturulma tairihini saniye türünden gösterir
convertdt = datetime.datetime.fromtimestamp(ctime)
# saniye cinsinde olan veriyi datetime formatına çevirdik
print(convertdt)

datetime.datetime.fromtimestamp(att.st_atime) #saniye türünde gelen veiriyi metod ile çevirdik
# son erişilme tarihini gösterir

datetime.datetime.fromtimestamp(att.st_mtime) # saniye türünde gelen veriyi metod ile çevirdik
# son değiştirilme tarihini gösterir
#----------------------------------------------------------------------------------------------------------

'''
******************************************** system() metodu **********************************************
'''

# system() metodu ile bilgisayarda istediğimiz bir programı çalıştırabiliriz
os.system('notepad.exe') 


'''
************************************ rmdir() metodu  *************************************
'''
# parametrede belirtilen klasörün silinmesini sağlar
os.rmdir('silinecek-klasör')

# parametredeki klasörün içinde başka bir klasör veya dosya varsa rmdir metodu ile klasör silinemez
#os.rmdir('new_directory')
# programı çalıştırdığımızda OSError alırız

'''
******************************* removedirs() metodu ***************************************
'''
# çoklu klasörleri veya içinde dosya olan klasörleri silmeyi sağlar
# silmek istediğimiz klasörleri içindeki klasörlerle ve dosyalarla parametreye girmemiz gerekir
os.removedirs('new_directory/denemeklasörü')
#----------------------------------------------------------------------------------------------------------



'''
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& PATH CLASSI &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
'''

# genellikle dosyaların uzantıları ile ilgili işlemleri path classı altındaki attributes ve metodlar ile yaparız

tamyol = os.path.abspath('os-module.py')
# parametredeki dosyanın tam yolunu verir
# dosya yolu belirtilirken katmanlar arasına ters slash('\') konur
print(tamyol)

dizin_ismi = os.path.dirname('C:/Users/Asus/Desktop/Python/Python_Temelleri/advanced-modules/os-module.py')
# dosya yolunun dizin kısmını verir
# dizin ismi dosya yolundan dosya isminin çıkarılmış halidir
# dizin sıralaması belirtilirken katmanlar arasına slash('/') konur
print(dizin_ismi)

# dirname metodunda parametre olarak abspath metodunu kullanabiliriz
# genellikle dosya tam yolu bilinmediğinde abspath metodu dirname metodu içinde kullanılır

ic = os.path.dirname(os.path.abspath('a.py'))
print(ic)



'''
++++++++++++++++++++++++++++++++++++++ klasör veya dosya varlığı sorgulama +++++++++++++++++++++++++++++
'''
# klasör, dosya, dizin sorgulamak için path.exists() metodunu kullanırız
print(os.path.exists('C:/Users/Asus/Desktop/Python/Python_Temelleri/advanced-modules/os-module.py'))
# exists metoduna parametre olarak dizin, klasör, dosya adı girilmelidir
# aradığımız dosya ilgili dizinde yokda parametreye dizin eklenmelidir

'''
**************************** path.isdir ve path.isfile metodu********************************
'''

print(os.path.isfile('C:/Users/Asus/Desktop/Python/Python_Temelleri/advanced-modules/os-module.py'))
# path.isfile() metodu parametredeki girdinin dosya olup olmasdığını sorgular
print(os.path.isfile('C:/Users/Asus/Desktop/Python/Python_Temelleri/advanced-modules')) # false

print(os.path.isdir('C:/Users/Asus/Desktop/Python/Python_Temelleri/advanced-modules/os-module.py')) # false
# parametredeki girdinin klasör olup olmadığını sorgular
print(os.path.isdir('C:/Users/Asus/Desktop/Python/Python_Temelleri/advanced-modules')) #true


'''
*************************************** diğer path metodları ******************************************************
'''
print(os.path.join("C:\\","deneme","deneme2"))
# path.join() metodu parametredeki dizinlerin birleştirilmesini sağlar

print(os.path.split("C:\\deneme"))
# dizinleri bölerek tuple şeklinde bir liste oluşturur

print(os.path.splitext('os-module.py'))
# dosya ismini ve uzantı türünü ayırarak tuple şeklinde bir liste oluşturur