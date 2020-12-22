fruits = {'orange','apple','banana'}

print(fruits)

'''
print(fruits[0])
'''
#set türündeki listelerde elemanlar indexlenemez.

for x in fruits:
    print(x)
    #for döngü komutu ile fruits içindeki bütün elemanları x'e yazdırabiliriiz.
    
## set türündeki listeler sıralanamaz.

fruits.add('cherry')
#.add metodu ile set listesine yeni bir eleman eklenebilir.
print(fruits)

fruits.update(['mango','grape'])
#.uptade metodu ile set listesine yeni liste göndererek birden fazla eleman ekleyebiliriz

##set liste türünde elemanlar tekrarlanamaz.Her elemandan sadece 1 tane bulunabilir.

myList = [1,2,5,4,1,3,2,3]
print(set(myList))
#print aşamasında liste türünü set constructorü ile set türüne çevirdik
#önceki listede tekrarlanan elemanlar set listesinde teke düşürülür

fruits.remove('mango')
print(fruits)
#remove metodu ile liste içinden belirtilen eleman silinebilir.
#ya da
fruits.discard('orange')
print(fruits)
#discard metodu ile de liste içinden eleman silinebilir.

fruits.clear()
print(fruits)
#clear metodu ile listedeki bütün elemanlar silinir.
