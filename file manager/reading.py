# 'r' modu ile açılan dosyanın belirtilen dizinde bulunması gerekir. Aksi halde dosya okuma hatası fırlatılır
try:
    file = open('newfile.txt')
    #ikinci parametreye bir mod atanmadığında otomatik 'r' olarak algılanır
except FileNotFoundError:
    print('Dosya okuma hatası')
finally:
    print('dosya okundu')    
    file.close()
    # finally bloğu ile hata yaşansa da yaşanmasa da dosya kapanır ve dosya okundu mesajı verilir    


file2 = open("C:/users/Asus/desktop/newfile_örn/newfile.txt",'r',encoding='utf-8')    

# FOR DÖNGÜSÜ ile okuma

for i in file2:
    print(i, end='')
    #dosya okurken print fonksiyonu bittiği yerde bir boş satır(\n) bırakır
    # bunu eklemek istemiyorsak end kw'sini kullanabiliriz
file2.close()    


# read() fonksiyonu ile okuma

content1 = file2.read()
# read fonksiyonu ile dosya içeriğine ulaşırız
print('içerik 1')
print(content1)
# dosya içeriğine ulaşıp print fonksiyonu ile yazdırdık

content2 = file2.read()
print('içerik 2')
print(content2)

# aynı dosyayı tekrar yazdırdığımızda bir içerik bulamadı
#bunun sebebi read fonksiyonu ile okumayı başlattığımızda içerik bitince cursor en sona gelir sonraki okuma komutunda içerik bulamaz
# open fonksiyonu ile tekrar açarak bunu engelleyebiliriz

file2.close()
    

content1 = file2.read()
print('içerik 1')
print(content1)


file2 = open("C:/users/Asus/desktop/newfile_örn/newfile.txt",'r',encoding='utf-8')    

content2 = file2.read()
print('içerik 2')
print(content2)

file2.close()


# read fonksiyonunda istenilen size parametresine girdiğimiz sayı kadar karakteri döndürür
content2 = file2.read(4)
# read fonksiyonuna girdiğimiz parametrede belirttiğimiz kadar karakterin içeriğine ulaştık ve değişkene attık
print(content2)

content3 = file2.read(2)
# dosya üzerinden okumaya devam eder yani cursorun en son kaldığı yerden sonraki 2 karakterin içeriğine ulaşırız
print(content3)
file2.close()


# readline() fonksiyonu ile okuma

contentT = file2.readline()
# readline fonksiyonu her seferinde birer satır okur
print(contentT,end='')
print(file2.readline(),end='')
print(file2.readline(),end='')
print(file2.readline(),end='')
print(file2.readline(),end='')
print(file2.readline(),end='')
print(file2.readline(),end='')
print(file2.readline(),end='')
print(file2.readline())
print(file2.readline())
file2.close()
#readline fonksiyonunun koyduğu otomatik boşlukları engellediğimiz için içinde olduğu içerik kadarını yazdırır
# eğer bunu end ile bunun önlemezsek eklemediğimiz her print fonksiyonu için boşluk bırakarak okur


# readlines() ile okuma

satırBilgi = file2.readlines()
# her bir satır bilgiyi bir listeye eleman olarak ekler
print(satırBilgi)
# her yeni satırı '\n' temsil ettiği için liste içinde elemanlara bağlı bu ifadede bulunur
file2.close()