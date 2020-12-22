
with open('newfile.txt', 'r+', encoding='utf-8') as file:
    # 'r+' modu açılan dosya içinde hem okumayı hem de yazmayı sağlayan bir moddur
    print(file.read())

with open('newfile.txt', 'r+', encoding='utf-8') as file:
    file.write('deneme') 
   
    # cursoru dosyanın başından başlatarak istediğimiz ifadeyi dosyaya ekler
    # o sırada dosya içinde o indexlerde bulunan ifadelerin yerine geçer 
    # 'w' modu ile açıp ekleme yaptığımızda halihazırda bulunan bütün içerikleri silip belirtilen ifadeyi ekler
    # print(file.read())           


with open('newfile.txt', 'r+', encoding='utf-8') as file:
    file.seek(61)
    file.write('deneme')    
    # burada cursoru dosyanın istedğimiz bir yerine getirip yazılacakları buradan itibarn yazmasını istedik
    print(file.read())    


# dosyanın en sonuna bir şey eklemek istediğimizde 'a' modunu kullanabiliriz

with open('newfile.txt', 'a', encoding='utf-8') as file1:
    file1.write('\nDeneme İsim')

with open('newfile.txt', 'r', encoding='utf-8')as file:
    print(file.read())    

# ******** dosya başına ekleme************

with open('newfile.txt', 'r+', encoding='utf-8') as file:
    content = file.read()
    content = 'bakirtas mehmet\n' + content
    file.seek(0)
    file.write(content)
    # dosya içeriğini content içine attık
    # conten içinde + operatörü ile ekleme yaptık
    # cursoru seek() fonksiyonu ile dosya başına taşıdık
    # en son elde edilen content bilgisini write() fonksiyonu ile dosya için yazdık
    
with open('newfile.txt', 'r', encoding='utf-8') as files:
    print(files.read())    


# **************dosya ortasına ekleme*********    

with open('newfile.txt', 'r+', encoding='utf-8') as file:
    list = file.readlines()
    print(list)
    # readlines() fonksiyonu ile dosya içeriğini liste haline getirdik
    list.insert(1,'bakirtas veli\n')
    # insert metodu parametrede belirtilen indexe belirtilen ifadeyi ekler sonrakileri bir yana kaydırır
    # elimizdeki listede 1. indexe 'bakirtas veli' stringini ekledik
    print(list)
    file.seek(0)
    # dosyaya ifade yazmadan önde cursoru en başa getirdik

    for i in list:
        file.write(i)
      
    #liste elemanlarına döngü ile ulaşıp write() metodu ile belirtilen dosyaya yazdırdık 
    # listeyi döngü ile dolaşmak yerine writelines() metodu ile aynı işlemi yapabiliriz
    file.writelines(list)
           
    

with open('newfile.txt', 'r', encoding='utf-8') as files:
    print(files.read())        