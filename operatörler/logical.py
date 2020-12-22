'''
MANTIKSAL OPERATÖRLER
'''

x = 7

sonucX = 5 < x <10
print(sonucX)
#x değeri 5'ten büyük 10' dan küçük müdür?(False)

'''
and
'''
sonucAnd = x > 5 and x < 10
print(sonucAnd)
#ifadenin iki tarafındaki sonuç örneğin True olursa True olarak yazdırır.
#İki tarafındaki sonuç False olursa False olarak yazdırır

hak = 1
devam = 'e'
sonucO = (hak > 0) and (devam == 'e')
print(sonucO)
#sadece sayısal veri tiplerinde değil str veri tipinde de kullanılır.

'''
OR
'''  
sonucOr = (x < 10) or (x % 2 == 0)
print(sonucOr)
#sorulardan herhangi birinin True değerinin alması sonucOr değişkeninin True değerine sahip olmasına yeterlidir.

'''
NOT
'''

sonucNot = not(x > 10)
print(sonucNot)
#sorudan alınması gereken değeri tersine çevirir.
#True False olur, False True olur.