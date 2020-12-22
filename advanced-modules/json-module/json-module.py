import os
os.chdir("C:/Users/Asus/Desktop/Python/Python_Temelleri/advanced-modules/json-module")
# dosya işlemlerinde sorun çıkmaması için söz konusu dizini çalışma dosyamızın bulunduğu dizin olarak tanımladık


import json

person = {"name":"Veli","languages":["Python","C#"]}
# person isminde bir dict yapısı tanımladık

person_json = '{"name":"Veli","languages":["Python","C#"]}'

# dict veri yapısını string içine alarak bir json yapısı oluşturduk
# elemanlarına ulaşmak istediğimizde dict veri yapısında olduğu gibi bir yöntem izleyemeyiz

# json bilgiyi dict veri yapısına çevirdiğimizde dict veri yapısının uygun olduğu işlemleri ve metodları kullanabilirim
# bunu gerçekleştirmek için json modülünü kullanırız

'''
******************************************** json.loads() metodu ******************************************
'''

# bir string json bilgisini dict veri tipine dönüştürmeyi sağlar
toDict = json.loads(person_json)
# parametre olarak elimizdeki bir string json bilgisini gönderip dict veri tipine dönüştürebiliriz
print(toDict)

# artık dict veri tipine uygun yöntemlerle json bilgisi içindeki elemanlara ulaşabilirim(çünkü artık dict veri yapısına çevrildi)
print(toDict["name"]) # çıktısı "Veli" stringi olacaktır


'''
*************************************** json.load() metodu ************************************************
'''

# daha önce oluşturulmuş bir json uzantılı person.json dosyamız var
with open("person.json") as f: # dosya okuma sonucu alınan bilgi f değişkenine tanımlanmıştır
# open ile daha önce oluşturulmuş person.json dosyasını oluşturduk
#open fonksiyonuna format bilgisi girilmediğinde format default olarak "r" formatına tanımlıdır
    data = json.load(f)
    # load metoduyla okuduğumuz bilgiyi çalışma alanımıza yüklüyoruz
    print(data) # artık bu json bilgisinden istediğimiz elemana ulaşabilririz
    print(data["name"])
    print(["languages"][0])

'''
**************************************** json.dumps() metodu *********************************************
'''
# dict veriyi string json halin getirir
person_dict = {"name":"mehmet","languages":["java","C++"]}

# örneğin bu objesi json bilgi kaydeden bir ortama göndermek istiyoruz;
# dict veriyi göndermeden önce json bilgi haline getirmeliyiz. Bunu .dumps() metodu ile gerçekleştiriyoruz

toJson = json.dumps(person_dict)
# person_dict dict objesini str veri tipine dönüştürdük
# diğer bir deyişle json bilgisi haline getirdik

'''
************************************** json.dump() metodu *********************************************
'''

# bir json uzantılı dosyaya bilgi atmak istediğimizde .dump() metodunu kullanırız
#eklemeyi yapmak için öncelikle open fonksiyonuyla dosyayı "w" formatında açmamız gerekir
with open("person2.json","w") as f:
    json.dump(person_dict,f) # yukarıda bulunan dict veri tipindeki bilgiyi bir json dosyasına atmak istiyoruz
    # bunun için dosyayı "w" formatında açıp dump metoduyla açıp parametreye bilgiyi ya da bilginin tanımlı olduğu değişkeni atmalıyız
    # ikinci parametreye ise open fonksiyonu ile tanımladığımız geçici dosya içeriği değerini atmalıyız
    # person2.json dosyasına baktığımızda person_dict objesinin kaydedildiğini görebilriz

person_dict2 = json.loads(person_json)
# string json bilgisini dict veri tipine çevirdik

arrangement = json.dumps(person_dict2,indent=4,sort_keys=True)
# dict tipinde olan person_dict2 objesini string json haline çevirirken düzenlemeler yapmak adına bazı parametreler kullandık
print(arrangement)
print(person_dict2)
# çıktıda da görüldüğü üzere person_dict2 verisi tek bir satırda yazılıyken arrangement verisinde girintiler ve satırlar bulunur

