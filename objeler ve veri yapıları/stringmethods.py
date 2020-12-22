message = "Hello There. My name is Veli Bakirtas"

print(message)

upperM = message.upper() 
print(upperM)
#upper metodu ile ifade edilen str dizesindeki bütün karakterleri büyük harfe çevirip istenen değişkene yazdırır.

lowerM = message.lower()
print(lowerM)
#lower metodu ile bütün karakterler küçük harfe çevrilir.

titleM = message.title()
print(titleM)
#Her kelimenin baş harfi büyük harfe çevrilir.

capM = message.capitalize()
print(capM)
#Verilen str ifadenin sadece ilk harfini büyük yazdırır

message2 = " Hello There. My name is Veli Bakirtas "
stripM = message.strip()
print(stripM)
#Verilen str ifadenin baş ve sondaki boşluk karakterlerini siler.
#sadece soldan silmek iöçin lstrip kullanılır
#sadece sağdan silmek için rstrip kullanılır

splitM = message.split()
print(splitM)
print(splitM[0])
#str ifade içindeki her boşluk sonrasını ayırır
splitM2 = message.split('.')
print(splitM2)
#split metoduna parametre girilmediği zaman boşluklardan ayırır.Metoda bölmke istediğimiz karakteri parametre olaark girebiliriz
#split metoduyla bir str ifadeyi parçalara ayırıp parçaları tek tek kullanabiliriz

joinM = '*'.join(splitM)
print(joinM)
#belirtilen str dizisinin elemanlarının tanıtılan ifadeyle birleşmesini sağlar(ifade = '*')

findM = message.find('Veli')
print(findM)
#verilen str ifade içindeki bir elemanı aratmak için kullanılır.
#aradığımız elemanın str ifade içindeki ilk elemanın index numarasını verir.
#rfind ile aramayı sağdan başlatabiliriz

isFound = message.startswith('H')
#message str ifadesi H ile mi başlıyor sorusunu sorduk.
print(isFound)

isFounde = message.endswith('s')
print(isFounde)
#message str ifadesi s ile mi bitiyor diye sorduk.

replaceM = message.replace('Veli','veli')
print(replaceM)
#ifade içindeki istenen elemanı bulup istenen ile değiştirir.

centerM = message.center(50)
print(centerM)
#oluşturulan 50 karakterlik konteynerı verilen str ifade ile yazdırır.
centerM2 = message.center(50,'*')
print(centerM2)

print(message.ljust(50,'*'))
#verilen ifadeyi sola yaslayarak konteyneri doldurur.

print(message.rjust(50,'*'))
#verilen ifadeyi sağa yaslayarak konteyneri doldurur.