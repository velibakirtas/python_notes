'''
METHOD
'''

#metotlarla birlikte class kavramı ortaya çıkıyor
#class = bünyesinde birçok metot barındıran yapı(şimdilik)

list= [1,2,3]
print(type(list))

list.append(4)
print(list)

list.pop()
print(list)

#list liste türüyle birlikte metotlarını içinde barındıran bir list classı sözkonusudur

myString = 'Hello'
print(type(myString))
#string veri tipiyle birlikte metotlarını içinde bulunduran bir str classı sözkonusudur
print(myString.upper())

#Not: Şu an için classları biz tanımlamıyoruz py kütüphanesinden bize geleln classları kullanıyoruz


'''
FONKSİYON
'''

# fonksiyonlar class içinde tanımlanmaz     
#bu fonksiyonlara ulaşırken bir class ismi gerekmez
    