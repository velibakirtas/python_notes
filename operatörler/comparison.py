'''
KARŞILAŞTIRMA OPERATÖRLERİ
'''
#Yazdığımız uygulamanın belli koşullar altında farklı yollara gitmesini sağlamak için kullanılır.

#username, password => database

#'velibakirtas, '123456'

a, b, c, d = 5, 5, 10, 4

username = 'velibakirtas'
password = '12345'

sonucA = 'velbkrts' == username
print(sonucA)

bol = a == b

print(bol)
# == ile soru sorma işlemi gerçekleitirilir.
#sorulan soru a b'ye eşit midir?
# Bu sorunun cevabı True ya da False olarak alınır.

negA = a != b
print(negA)
# != ile de soru sorma işlemi gerçekleştirilir
# yukarıdaki yapıda a b'ye eşit değil mi şeklinde bir soru sorulur

essiz = a > b
print(essiz)
# a b'den büyük mü sorusunu sorduk.
#tersi için de bu durum geçerlidir

dbl = a <= b
print(dbl)
# a b'den küçük müdür ya da a b' ye eşit midir sorusunu sorduk.