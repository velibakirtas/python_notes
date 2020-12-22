'''
REGULAR EXPRESSİON MODÜLÜ
'''

import re


str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

'''
***************************************** re.findall() metodu **********************************************
'''

# string obje içersinde arama yapılmasını sağlar
findall = re.findall('Python',str) # str objesinde 'Python' ifadesini aradık
# findall metodu ilk parametreye ya bir regular expression ifadesi ya da bir string ister
# ikinci parametrede ise aramnın yapılacağı obje istenir
print(findall)
# çıktısı obje içindeki ilk parametrede verilen ifadeleri liste şeklinde döndürür
# eğer objede parametredeki veri yoksa boş bir küme döndürülecektir

# len fonksiyonu ile de kaç tane olduğunu öğrenebiliriz
print(len(findall))
#-------------------------------------------------------------------------------------------------------------

'''
**************************************** re.split() metodu***************************************************
'''

# verilen str veriyi bölmeye yarar
split = re.split(' ',str)
# ilk parametreye veri içinde bölünecek kısımlar tanımlanır (burada bunu boşluk olarak tanımladık)
# ikinci parametreye ise böleceğimiz veriyi tanımladık
# yani str ifadesindeki her boşluktan elemanları böl ve liste içine eleman olarak at
print(split)
# dönecek çıktı liste içinde verilir

#split metodu da bir nevi arama işine hizmet edebilir(nasıl kullanmak istediğimize bağlı olarak)
#-------------------------------------------------------------------------------------------------------------

'''
******************************************* re.sub() metodu ************************************************
'''

# str içinde değiştirme işine yarar
sub = re.sub(" ","-",str) # boşluk yerine ('\s') de kullanılabilir. re de boşluk karakteri olarak tanımlıdır
# ilk parametreye değiştirmke istediğimiz karakter
# ikinci parametreye değiştirmek istediğimiz karakterin yerine konulacak karakter
# üçüncü parametreye ise hangi veri üzerinde değişiklik yapacağımızı belirtiriz
print(sub)
# veri üzerinde kalcıı bir değişiklik yaptırmaz metod özelinde istediğimiz çıktıyı döndürür
#-------------------------------------------------------------------------------------------------------------

'''
***************************************** re.search() metodu *********************************************
'''

# bu da istediğimiz karakteri, ifadeyi bulmamızı sağlar
search = re.search("Python",str)
# ilk parametreye aradığımız ifadeyi yazarız
# ikinci parmetreye ise ifadeyi aradığımız objeyi tanımlarız
print(search)
# çıktı olarak bize bir re modülünün Match classının bir objesi dönecektir
# bu obje span bilgisinde ifadenin veride bulunduğu index aralığını verir
# aranılan ifade yoksa bir obje üretilmez (hata da döndürülmez)

# obje üzerinden span metodu kullanılabilir
span = search.span()
print(span)

print(search.start()) # aranılan ifadenin kaçıncı indexte başladığı bilgisini verir
print(search.end()) # aranılan ifadenin kaçıncı indexte bittiği bilgisini verir
print(search.group()) # hangi ifadeyi aradığımızı geri gönderir
print(search.string) # üzerinde arama yapılan veriyi döndürür
#-------------------------------------------------------------------------------------------------------------
