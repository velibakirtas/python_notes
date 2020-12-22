'''
name = 'Veli Bakirtas'

for harf in name:
    if harf == 'a':
        break
    print(harf)
# harf değişkeni a' ya eşit ise break komutuyla döngüyü durdurduk.    

for harf2 in name:
    if harf2 == 'a':
        continue
    print(harf2)
# harf2 değişkeninin 'a' ya eşit olduğu döngü turunu pas geçip döngüye devam et

'''
x = 0
'''
while x<5:    
    if x == 3:
        break
    print(x)
    x+=1
# 0 dan 5 e kadar yazdırdığımız sayının 3'e eşit olması halinde breakle karşılaşılır ve döngü sona erer.
'''
while x<5:
    if x == 2:    
        continue
    print(x)
    x+=1   
'''     
#bu döngüde x, 2'ye eşit olduğunda döngünün o turu atlanır
#tur atlandığı için değişken üzeride işlem yapılmaz
#haliyle değişken daima 2 ye eşit olarak kalır ve döngü sonsuz işlem görür.    
#bunun telafisi olarak değişken üzerinde yapılan işlem satırını şartlandırma başlamadan önce konumlandırabiliriz
while x<5:
    x += 1
    if x == 2:
        continue
    print(x)


#ÖRN:1'den 100'e kadar tek sayıların toplamı kaçtır

x = 0
toplam = 0

while x <= 100:
    x += 1
    if x % 2 == 1:
        continue
    toplam += x
print(toplam)
'''                   