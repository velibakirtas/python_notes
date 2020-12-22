'''
import datetime
'''
# datetime modülünün bütün claslarını, modüllerini, fonksiyonlarını ve özelliklerini çağırdık

# bunun yerine istediğimiz modülün istediğimiz classını, modülünü, fonksiyonunu veya özelliğini çağırabiliriz
'''
from datetime import date
from datetime import time
'''
from datetime import datetime
# datetime modülünün datetime classını çağırdık
# sadece datetime classını import ettiğimiz için modülden obje olarak çağırmak yerine classı direkt kullanabiliriz
att = dir(datetime)
#print(att)
# datetime modülü içindeki datetime classının özelliklerini, fonksiyonlarını vb. yazdırdık

'''
**************datetime.now() metodu*****************
'''
data = datetime.now()
# datetime classının now() metod ile şimdinin tarih ve saat bilgisine ulaşırız
# now() metodu çıktısı içinden istediğimiz bölümü alabiliriz
print(datetime.now().month)
print(data.year)
print(data.day)
print(data.hour)
print(data.minute)
print(data.second)

#***** datetime classının today() metodu da now() metodu ile aynı işi yapar. özelliklerine de aynı şekilde ulaşılır

'''
**************************datetime.ctime() modülü***********************
'''
# bizden parametre olarak bir datetime bilgisi istiyor
print(datetime.ctime(data))
# daha önce datetime'dan bir obje alarak data'ya tanımlamıştık. bunu ctime metoduna parametre olarak yolladık
# ctime() metodu datetimedan alınan bilginin daha açık ifade edilmesini sağlar

'''
****************************datetime.strftime() modülü***************************
'''
print(datetime.strftime(data,'%Y')) # data objesinden sadece yıl bilgisini almamızı sağlar
# bu modül bizden ilk parametrede bir datetime objesi bekler
# ikinci parametrede ise str içinde strftime için özel kullanılan bazı komutları ister
print(datetime.strftime(data,'%X')) # data objesinden sadece saat bilgisini almamızı sağlar
print(datetime.strftime(data,'%d')) # data objesinden sadece gün(sayı ile) bilgisini almamızı sağlar
print(datetime.strftime(data,'%A')) # data objesinden sadece gün(yazı ile) bilgisini almamızı sağlar
print(datetime.strftime(data,'%B')) # data objesinden sadece ay(yazı ile) bilgisini almamızı sağlar
# strftime modülü içinde ctime modülü çıktılarını da barındırır ikinci parametreye verilen komut ile hangi türde çıktıyı alacağımızı belirleriz
# strftime modülü ile birden fazla komutu kullanarak istediğimiz çıktıyı bir arada alabiliriz
print(datetime.strftime(data,'%X %d %B %Y'))
print('strftime parametre kodlarını görmek için linke tıkla https://www.w3schools.com/python/python_datetime.asp ')

'''
**********************************strptime() modülü******************************
'''
t = '13 Aralık 2020'
# kendi oluşturduğumuz tarihin gün, ay gibi niteliklerini python bilemez
gun, ay, yil = t.split()
# split metodu ile str bilgiyi bölüp değişkenlere atabiliriz
print(gun)
print(ay)
print(yil)

t2 = "15 December 2020 hour 14:15:55"
# kendimiz str şekilde detaylı bir tarih bilgisi ekledik
# bu strdeki veriyi gün, ay, yıl gibi bilgilere bölmek istersek strptime modülü kullanılır
dt = datetime.strptime(t2, '%d %B %Y hour %H:%M:%S') 
# içindeki bilgileri atayacağımız string veriyi(t2) ilk paramaetreye tanımladık
# ikinci parametredeki komutlarla strnin her bir elemanının(kelime, sayı, takımsayı vb.) tanımlanmasını sağladık
# 15 sayısı gün olarak, December ay olarak, 2020 yıl olarak, 14:15:55 ise saat olarak tanımlandı
# hour bilgisine herhangi bir nitelik atamak istemediğimiz için hour bilgisi hour olarak atandı
print(dt)

# strftime modülü ile ulaşmak istediğimizde artık istediğimiz niteliğe ulaşabiliriz
print(datetime.strftime(dt,'%B')) # dt objesinden bulunan ay niteliğini yazdırdım

# datetime attribute ulaşma metodları ile de ulaşılabilir
print(dt.year)
print(dt.month)
print(dt.day)

'''
-------datetime classına ait obje oluşturma----------
'''
birthday = datetime(1999,10,27,15,47,16)
# ilk parametreye yıl, 2.ye ay, 3.ye gün, 4.ye saat, 5.ye dakika, 6.ya saniye değerlri atılır
print(birthday)

'''
**************************timestamp ve fromtimestemp modülü********************************
'''
sn = datetime.timestamp(birthday) # verilen tarihi saniye cinsinden verir
print(sn)

toDt = datetime.fromtimestamp(sn) # saniye cinsinde olan tarihi açık tarih(datetime) şekline dönüştürür
print(toDt)

milat = datetime.fromtimestamp(0)
print(milat) # 1970-01-01 03:00:00  
# milat verinin çıktısı bilgisayarlar için kullanılan milattır
# timestamp modülünden alınan çıktı bu tarih referans alınarak oluşturulur
# fromtimestamp modülünden alınan bilgi de bu tarih referans alınarak oluşturulur

'''
--------- iki tarih arasındaki süreyi bulma---------------
'''
delta = data - birthday # verilen çıktı timedelta fonksiyonu kullanılarak da elde edilebilir
# zaten ortaya çıkan bilgi de bir timedelta objesidir
print(delta)

days = delta.days
second = delta.seconds
ms = delta.microseconds
print(days)
print(second)
print(ms)

from datetime import timedelta
# kullanmak için timedelta classını da import ettik
plusDay = data + timedelta(days = 10)
# daha önce oluşturulan data datetime objesi üzerine timedelta metodu ile 10 gün ekledik
print(plusDay)

plusDayAndMin = data + timedelta(days = 630, minutes = 20)
print(plusDayAndMin)

# aynı işlemi çıkarmak için de kullanabiliriz(sadece operatörü değiştirmeliyiz)