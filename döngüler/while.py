#1'DEN 100'E KADAR YAZDIR
x = 0

while True:
    print(x)

#bu döngüde ifade daima True değeriyle karşılaşacağı için x'i sonsuz kere yazdırır.

while x < 100:
    print(x)

# while döngüsü bu şekilde de x ' i yazdırır.
#çünkü x daima 0'a eşit olur ve 100'e ulaşmaz    

while x < 100:
    print(x)
    x += 1
print( 'bitti')

#bu şekilde bir kullanımda x her döndüğünde x'1 eklenir ve x 100'e en yakın olduğu yerde döngü biterek 'bitti' yazdırır

#NOT: while koşul ifadesi algoritmada True ya da False değer üretir.True değer ürettiği sürece döngü devam eder.

while x <= 100:
    if x%2 == 0:
        print(x)
    x += 1        
    
#döngüyü bir şart bloğuna bağlayabiliriz.
#1-100 arasındaki bütün çift sayıları yazdırana kadar döngü devam eder.Döngü her yenilendiğinde x'e bir eklenir.
#x 100'e ulaştığında döngü sona erer.

while x <= 100:
    if x%2 == 0:
        print(f'{x} çift sayıdır')    
    else:
        print(f'{x} tek sayıdır')    
    x += 1           


name = '' #boş bir string ifade False değerine karşılık geliyor.
#döngü içinde tek başına kullanıldığında döngüyü çalıştırmaz


while not name: #not name diyerek daima False değer alacak veriyi True değerine çevirdik.
    name = input('isminizi giriniz: ')
print(f'merhaba {name}')   
      
#kullanıcı name str ifadesine bir değer girmediği sürece not metodundan dolayı döngü sürekli tekrar edecektir.
#kullanıcıdan bir bilgi alındığında döngü sona erer ve işlem gerçekleşir.

while not name.strip():
    name = input('isminizi giriniz: ')
print(f'merhaba {name}')
#kullanıcı bu noktada boşluk karakteri girebilir bunun önlemek için .strip metodu ile boşlukları sielbiliriz