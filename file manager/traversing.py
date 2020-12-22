'''
DOSYA OKUMA FONKSİYONLARI
'''

with open('newfile.txt', 'r', encoding='utf-8') as file:
    # açılan dosya objesinden gelen bilgiyi file değişkenine attık
    # bunun sebebi obje üzerinden çıktı sağlayabilmek için kullanmaya müsait hale getirmek
    content = file.read()
    print(content)
    # with bloğunun sonuna gelindiğinde dosya otamatik olarak kapanır
    print(file.tell())
    # tell() fonksiyonu dosya okunma sırasında bulunulan cursor konumunu verir
    file.seek(0)
    # seek() fonksiyonu ile cursoru istediğimiz konuma gönderebiliriz
    print(file.tell())
    # seek() fonksiyonu ile cursoru dosyanın başına gönderdik ve gözlemlemek için tekrar tell() fonksiyonunu çalıştırdık
    
