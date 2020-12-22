name = 'Veli'
surname = 'Bakirtas'
age = 21

'''
print('My name is ' + name + ' ' +  surname + ' and I am ' + age + ' years old') 
'''

#bu dizinde verşlen komut age değişkeninin int türünde olmasından dolayı işleme konamaz

#Bu sorunun giderilmesi için age değişkenini str tüürnde tanımlayabiliriz ya da print komutu içinde tip değişimi yapabiliriz.

print('My name is ' + name + ' ' + surname + ' and I am ' + str(age) + ' years old')

#(\n) ifadesi yeni bir satır oluşturur

print('My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old')

#Yazdırmak istediğimiz ifadeyi bir değişkene tanımlayarak yazdırma komutunun içine ekleyerk de bu işlem yapılabilir.

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old'

print(greeting)


#Str karakter dizisinin her bir elemanına ulaşmak için her elmana bir index numarası atanır.

print(greeting[0]) #greeting değişkeninde 0 numaralı indexe sahip karakteri yazdırdık
print(greeting[1])
print(greeting[2])
print(greeting[3])

# len komutu ile belirlenen str verinin kaç karakterli olduğunu öğrenebilriz

print(len(greeting))

print(greeting[len(greeting) - 1])

length = len(greeting)
print(greeting[length - 1]) #Karakter sayısı 47 olmasına rağmen index numaraları 0'dan başladığı iöin son karakter 46. index numarasına sahiptir.

#son karakteri karakter no ile değil index no ile sorgulatıyoruz.    sonKarakter = len - 1

'''
str dizisinin son karakteri sağdan sola giderken -1 ile indexlenir
'''
print(greeting[-1])

print(greeting[3:7])
#[x:y] ifadesi x ve y de dahil olmak üzere aradaki bütün karakterleri gösterir.

print(greeting[3:])
print(greeting[:12])
# Bu ifadede iki örnekte görüldüğü üzere başlangıç veya bitiş değerlerinden biri verilmeden karakterler istenebilir.

print(greeting[5:30:5]) 
#bu ifadeyle 5 den 30 a kdar olan indexli sayıları beşte bir şekiklde alır.
