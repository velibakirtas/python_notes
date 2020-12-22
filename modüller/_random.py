import random

'''
icerik = dir(random)
print(icerik)
'''

'''
yardim = help(random)
print(yardim)
'''

rs = random.random()
# 0.0 ile 1.0 arasında rastgele bir sayı üretilir

rsKat = random.random() * 100
#üretilecek sayıyı 100 ile çarptık

uni = random.uniform(1,10)
#parametreler arasında float bir sayı üretir

intUni = int(random.uniform(1,10))
#üretilen sayıyı int veriye çevirebiliriz

#int yardımcı metodunu kullanmak yerine randint metodunu kullanabiliriz
intS = random.randint(1,10)
#int bir sayı üretir

names = ['veli', 'mehmet', 'hülya', 'a']
rİsim = names[random.randint(0,len(names) - 1)]
#random modülü ile liste içinden eleman seçtirebiliriz

#listeden eleman seçmek için direkt bu iş için hazırlanmış choice metodunu kullanabiliriz
rChoice = random.choice(names)

greeting = 'Hello There'
rGreeting = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
#shufflee metodu ile bir listenin içeriği karıştırılabilir

liste2 = range(100)
listSample = random.sample(liste2,3)
# parametrede belirtilen liste içinden, parametrede belirtilen kadar eleman alır

#bu metot str verilerde de kullanılır
st = 'hello'
stSample = random.sample(st,2)

print(rs)
print(rsKat)
print(uni)
print(intUni)
print(intS)
print(rİsim)
print(rChoice)
print(rGreeting)
print(liste)
print(listSample)
print(stSample)