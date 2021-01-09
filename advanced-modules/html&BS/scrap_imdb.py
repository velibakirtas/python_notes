import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
# web sitesine bir talep gönderdik
# talebin olumlu olmasından sonra sitenin kaynak kodlarına content ile ulaştık
##print(html)


soup = BeautifulSoup(html,"html.parser")

list = soup.find("tbody", {"class":"lister-list"}) 
# kaynaktaki liste-list classına sahip ilk tbody etiketine ulaştık
list2 = soup.find("tbody", {"class":"lister-list"}).find_all("tr",limit = 1) 
# find_all metoduna girilen limit parametresi etiket içeriğinden kaç tanesine ulaşılcağını belirtir
# yani bu kaynakta 250 tane tr etiketi varken biz ilk tr etiketine ulaşıyoruz

for tr in list2:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    print(title,year,rating)
    # list 2 değişkeninde limiti 1 olarak tanımladığımız için sadece ilk filmin ismini yazdırır
    
"""
1- imdbnin top rated movie sayfasının linkini aldık ve url değişkenine tanımladık
2- requests modülünün get metodu ile kaynak ulaşım talebi yollandı ve content metoduyla kaynak içeriğine ulaşıldı ve html değişknine atldı
3-  soup adında bir obje oluşturuldu ve parametrelerine html değişkeni ve html.parser yöntemi atandı
4- soup içinde find metodu ile classı lister list olan etikete gidildi sonra find_all ile tr etiketlerinin tamamına ulaşıldı ama sadece ilk tr etiketi ile ilgilendiğimiz için limit'e 1 tanımlandı
5- yukarıdaki işlemden gelen bilgi list2 değişkenine atıldı 
6- list2 üzerinde bir döngü başlatıldı
7(döngü)- find metodu ile classı titleColumn olan td etikeitine gidildi sonra yine find ile a etiketine gidildi ve text bilgisi alındı
8(döngü)- yukarıdaki işlemden gelen bilgi title değişkenine atıldı
9(döngü)- aynı işlem yıl bilgisi için yapıldı ama ikinci findda "span" etiketine gidildi ve year değişkenine atıldı
10(döngü)- reyting bilgisi için de gerekli işlemler yapıldı
11(döngü)- sonra print ile yazdırıldı

"""