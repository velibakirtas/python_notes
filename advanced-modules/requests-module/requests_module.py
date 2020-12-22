import requests as rq

talep = rq.get("https://jsonplaceholder.typicode.com/todos")
# parametrede belirtilen adrese bir get metodu ile bir talep yolladık

print(talep)
# adresten Respone[200] şeklinde bir cevap geldi
# bu talebin olumlu karşılandığını gösterir

# talebi gönderdiğimiz adreste json bilgiler bulunuyor  v ben bu bilgileri almak istiyorum
jsn = talep.text
#print(jsn)
# text özelliği ile adresteki json bilgiyi alabiliriz
print(type(jsn))

# adresten gelen veriler json str tipinde olduğu için çalışma alanımızda kullanabilmek için standart veri tiplerine dönüştürmeliyiz
# bunun için json modülünü import ediyoruz

import json

convert  = json.loads(talep.text)
#print(convert)
# loads metoduyla gelen veriyi standart bir veri yapısına çevirdik
# artık veri içinde istediğimiz bir bilgiyi alıp kullanabiliriz
print(convert[0])

# gelen liste verisini for dmngüsü içinde düzenli bir şekilde gözlemleyebiliriz
for i in convert:
    print(i)