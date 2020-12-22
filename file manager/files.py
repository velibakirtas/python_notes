# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# open(dosya_adi,dosya_erisme_modu)

#dosya_erisme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w" : (Write) yazma modu, dosyayı konumda oluşturur
#("w" tarafından yazılan bilgi daha önce yazılan bilgileri siler)
# (eğer ilgili dizinde yoksa oluşturur)

dosya = open("newfile.txt","w")
#oluşturduğumuz dosya bilgisinin referansını dosya değişkenine attık
# daha sonra bu referans ile dosya üzerinden belli işlemler yapacağız 
dosya.close()
#açtığımız dosyayı kapattık


ekFile = open("C:/users/Asus/desktop/newfile.txt","w",encoding='utf-8')
# oluşturacağımız dosyanın karakter kodlamasını belirledik
ekFile.write('Veli bakırtaş')
ekFile.close()
#oluşturacağımız dosyayı bulunduğumuz dizinden farklı bir dizinde oluşturabiliriz

# "a" : (appende) ekleme, dosya konumda yoksa oluşturur
#(dosyanın içinde daha önce olan bir verinin üzerine ekleme yapar)

ekFile = open("C:/users/Asus/desktop/newfile.txt","a",encoding='utf-8')
ekFile.write('\nMehmet Bakırtaş')
ekFile.close()


# "x" : (create) oluşturma, Dosya zaten varsa hata verir
# (yeni bir dosya oluşturur)

ekFile = open("C:/users/Asus/desktop/newfile2.txt","x",encoding='utf-8')


# "r" : (read) okuma, varsayılan dosya konumda yoksa hata verir

