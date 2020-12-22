name = 'Veli'
surname = 'Bakirtas'

#Format str ile FORMATLAMA
print('My name is {} {}'.format(name, surname))
#format komutuyla süslü parantezlere tanımlanan ifadeler name ve surname değişkenleridir.


print('My name is {0} {1}'.format(name, surname))
'''
Bu ifadede süslü parantezler 0. ve 1. index yerini alır. Yukarıdaki ifade aşağıdaki gibi de yazılabilir.
'''

print('My name is {1} {0}'.format(name, surname))
#süslü parantez içindeki index sayılarını değiştirerek yazılacak veride değişiklikler yapılabilir.

print('My name is {s} {a}'.format(a=name, s=surname))
#format kodu içerisinde ifadeler bir değişkene tanımlanarak süslü paranteze alınmak istenen sonucu verecek şekilde yerleştirilebilir.

result = 200 / 700
print('the result {}'.format(result))
#format işleminde süslü paranteze yazdırılacak veri tipi int veya str olsa da işlenir.

print('the result {r:1.5}'.format(r=result))
#süslü parantez içindeki 1 sayısı tam kısımdaki ifade dahil bırakılacak boşluk sayısını belirtir.
#süslü parantez içindeki 5 sayısı ondalıklı kısımdaki alınacak basamak sayısını 5 olarak göstrerşyor


# f str ile FORMATLAMA
print(f'My name is {name} {surname}')
#f formatlama tipi str ifadenin başına getirilerek süslü parantezler içine format verileri eklenir.

