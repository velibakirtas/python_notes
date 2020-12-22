def sayHello():
    print('Hello')
    
# sayHello adında bir fonksiyon oluşturduk
#bu fonksiyonun içinde barındıracağı kod bloğunu : dan sonra tanımladık

sayHello()

#fonksiyona parametre de girilebilir.
#bu parametrenin çalışması için kod bloğunda parametreye ilişkin kodun yazılı olması gerektir

def sayHello1(name = 'user'):
    print('Hello ' + name)

sayHello1('veli')

# fonksiyon oluşturuken parametreye istenilen parametrenin türünü belirtecek çağrışım yapan bir değişken yazılmalı
# burada parametreden gelen değerin aşağıdaki kod bloğunda amacı doğrultusunda kodlanır

sayHello1()
# kullanıcıdan bir parametre alınmadığında parametre istemine değer tanımlanmadıysa hata alınır
#ama fonksiyon oluştururken yapıldığı gibi bir tanımlama olursa parametre girilmediği zaman daha önce oluşturulurken tanımlanmış parametreyle çalışır


def sayHello2(name = 'user'):
    return 'Helo ' + name
#return ifadesi fonksiyonun işlemi bittikten sonra değeri çağrıldığı yere geri göndermek için kullanılır(sayHello2'ye gönderiliyor).

msg = sayHello2('veli')
print(msg)

def toplam(num1,num2):
    return num1 + num2
sonuc = toplam(5,6)
print(sonuc)

def emeklikalan(dy,isim):
    '''
    DOCSTRİNG: Dogum yiliniza gore emeklilik yasinizi hesaplar
    İnput: Dogum yili ve isim
    Output: emekliliginize kalan sure
    '''
    yas = 2020 - dy
    emeklilik = 65-yas
    
    if emeklilik > 0:
        print(f'emekli olmanıza {emeklilik} yıl kaldı')
    else:
        print(f'zaten emeklisiniz')        
        
emeklikalan(1999,'veli') 
print(help(emeklikalan))       

#oluşturulan fonksiyon içinde yorum bölümü olarak yazılan kısım fonksiyonun help(yardım) bilgilerini saklar
#buraya fonksiyonun neye yaradığını nasıl kullanılacağının bilgilerini ekleyebilrirz
#help komutu ile bu bilgilere ulaşabiliriz
