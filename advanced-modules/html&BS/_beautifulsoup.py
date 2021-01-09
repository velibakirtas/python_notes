html_docs = """
<!DOCTYPE html>
<html lang="en" lang="en">
<head>
    
<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Python</title>
</head>    
<body>
    <h1 id="header">
        programlama

        </h1>
    <div class="grup1">
        <h2>
            Python programlama

        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
            <li>Menü 4</li>
        </ul>
    </div>
    <div class="grup2">
        <h2>
            Python modüller

        </h2>

        <ul>
            <li>os module</li>
            <li>requests module</li>
            <li>random module</li>
            <li>Beatifoul Soup module</li>
        </ul>
    </div>
        <div class="grup2">
        <h2>
            Python modüller

        </h2>

        <ul>
            <li>os module</li>
            <li>requests module</li>
            <li>random module</li>
            <li>Beatifoul Soup module</li>
        </ul>
    </div>
     </div>
        <div class="grup3">
        <h2>
            Python modüller

        </h2>

        <ul>
            <li>os module</li>
            <li>requests module</li>
            <li>random module</li>
            <li>Beatifoul Soup module</li>
        </ul>
    </div>
</body>    
"""        



from bs4 import BeautifulSoup

soup = BeautifulSoup(html_docs, "html.parser")
# soup adında bir örneklem oluşturduk
# bs bizden ilk parametrede kullanılacak sitenin html iskeletini ya da kaynağını ister ister
    # html iskeletini yukarıda html_docs değişkenine attık
#2. parametrede ise denetleme mekanizmasının nasıl olacağını tanımlarız burada yöntemi html.parser olarak tanımladık

pre = soup.prettify()
# ilk parametrede bulunan html_docs kaynak bilgilerini prettify() metoduyla düzenlenmiş hale getirdik

# kaynak içinden title etiketini almak istersek:
title = soup.title
print(title) 

print(title.name)
# name att ile etiket ismine ulaşabiliriz
print(title.string)
# string ile etiket içeriğine ulaşabiliriz

# ya da head etiketi için deneyelim:
head = soup.head
print(head)

# bu şeklide diğer etiketlere de ulaşabiliriz
print(soup.h1)
print(soup.h2)
# h2 etiketinden birden fazla bulunuyor fakat biz etiketi çağırmak istediğimizde ilk karşılaşılan etiket çağırılır
print(soup.h2.string)
# h2 etiketindeki str bilgisini yazdırdık

all = soup.find_all("h2")
# parametrede bulunan etiket ismine sahip bütün etiketlere ulaşmamızı sağlar
# buradan 2 tane h2 etiketine sahip elemanlar gelecektir

print(all[0])
# find_all ile ulaşılan h2 etiketine sahip bilgilerin 0. indeksindeki bilgileri yazdırdık

print(all[0])

div = soup.div
print(div)

print(soup.find_all("div")[1])
print(soup.find_all("div")[1].ul)
print(soup.find_all("div")[1].ul.find_all("li")) # bunun çıktısı bize dizi şeklinde gelecektir
# dizi şeklinde dönen bir çıktı üzerinde döngü kurulmasına müsaittir

all_div = soup.div.findChildren()
#div etiketi altındaki tüm elemanları liste halinde getirir
print(all_div)


# şu an ilk div etiketinin bulunduğu bölgedeyiz hatta bunu div adlı etikete attık
# ama bir sonraki dive ulaşmak istiyorsak findNextSibling() metodunu kullanabiliriz
other_div = soup.div.findNextSibling()
print(other_div)

other_div2 = soup.div.findNextSibling().findNextSibling()
# metodu bir kere daha kullanarak etiketin bir sonraki öğesine yani 3. öğesine ulaşabiliriz
print(other_div2)

other_div3 = soup.div.findNextSibling().findNextSibling().findNextSibling()
# şu anda div etiketinin 3. elemanındayız
# eğer geride kalan elemanlara(1 veya 2) dönmek istersek:
previous = soup.div.findNextSibling().findNextSibling().findNextSibling().findPreviousSibling()
print(previous)