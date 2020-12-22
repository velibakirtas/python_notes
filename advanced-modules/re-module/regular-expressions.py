import re

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

'''
    []- Köşeli parantezler arasına yazılan bütün karakterler aranır

        [abc] söz konusu strde a,b,c karakterleri aranacaktır
            => a    : 1 match (a stringinde aram yapılırsa bir eşleşme sağlanır)
            => b    : 1 match (b stringinde arama yapılırsa bir eşleşme sağlanır)
            => Python   : No matches (Python stringinde arama yapılırsa eşleşme sağlanmaz)
        
        [a-e] aranılacak karakterleri tek tek yazmak yerine aralık belirterek de aranabilir
            [a-e] => [abcde] ile aynıdır
            [1-5] => [12345] ile aynıdır
            [0-39] => [01239] ile aynıdır
            
        [^abc] => abc dışındaki karakterleri arar
        [^0-9] => rakam olmayan karakterleri arar
'''

findall = re.findall("[abc]",str)  #a,b,c karakterlerini aradık                              
print(findall)

findall2 = re.findall("[sat]",str)  #s,a,t karakterlerini aradık        
print(findall2)

findall3 = re.findall("[a-e]",str) # a ile e arasındaki karakterlerin hepsini aradık
print(findall3)

findall4 = re.findall("[0-7]",str) #0 ile 7 arasındaki rakamların tamamını arar
print(findall4)

findall5 = re.findall("[1-4907]",str) # aralık belirten kısım sadece 1 ile 4 arasıdır
# bu aralığın dışında 9,0,7 rakamlarını da arar
print(findall5)

findall6 = re.findall("[^abc]",str) # ,b,c karakterleri dışındaki bütün karakterleri arar
print(findall6)

findall7 = re.findall("[^0-9]",str)
print(findall7)

'''
    . - herhangi bir haneli karakteri belirtir (sayı da olabilir kelime de...)

        .. -söz konusu strde herhangi iki haneli bir ifade arar
            => a    : No match (a stringinde iki haneli herhangi bir karakter yoktur)
            => ab   : 1 match (ab stringinde iki haneli bir karakter aranır)
            => abc  : 1 match (abc stringinde iki haneli bir karakter aranır)
            => abcd : 2 match (abcd stringinde iki haneli bir karakter aranır)
'''       
    
findall = re.findall("...",str) # objedeki ifadenin her 3 karakterini eleman olarak alıp liste haline getirir
print(findall)

findall2 = re.findall("Py..on",str) # ilk parametredeki noktaları değişken karakter olarak algılar
# str içinde bu tanımla eşleşebilecek elemanları alıp liste haline getirir 
print(findall2)

'''
    ^ - belirtilen karakterle başlıyor mu?

        ^a söz konusu strnin a karakteri ile başlayıp başlamadığını sorar
        
            =>a : 1 match (a stringi belirtilen karakterle başlıyor mu?)
            =>ab: 1 match (ab stringi belirtilen karakterle başlıyor mu?)
            =>bac: No match (bac stringi belirtilen karakterle başlıyor mu?)
'''

search = re.search("^P",str) #verdiğimiz str nin P karakteri ile başlayıp başlamadığını soruyoruz
# search metodundan alacağımız çıktı eğer öyle ise bir match objesinin oluşturulduğudur
print(search)            

search2 = re.search("^K",str)
# str ifade K karakteri ile başlamıyorsa bir obje oluşturulmaz
print(search2)
# şart söz konusu stringin en başındaki karakterin ne olduğu ile ilgilidir

search3 = re.findall("^R","Python Kursu: Python Programlama Rehberiniz | 40 saat") 
# 2. parametredeki ifade str değişkenine tanımlı ifade ile aynıdır
# bu ifadenin en başındaki karakter P olduğu için findall metodundan alınan çıktı boş bir listedir
print(search3)

'''

    $- belirtilen karakterle bitiyor mu?
    
        a$ söz konusu karakterin a karakteri ile bitip bitmediğini sorar
        
            => a    : 1 match (a stringi a karakteri ile bitiyor mu?)
            => lamba: 1 match (lamba stringi a karakteri ile bitiyor mu?)
            => Python: No match (python stringi a karakteri ile bitiyor mu?)
'''

findallend = re.findall("t$",str) # str t karakteri ile bitiyor mu?       
print(findallend)
# çıtkı olarak eğer şart sağlanıyorsa t'nin eleman olduğu bir liste oluşturulur

findallend2 = re.findall("saat$",str)     
print(findallend2)

findallend3 = re.findall("saatt$",str)
print(findallend3)
# şart sağlanmadığı için findall metodu boş bir liste döndürecektir

'''
    * - bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder
        sorgulanma şeklince bir dizilim varsa ama karakter yoksa bile eşleşme sağlanır
        
        ma*n  burada sorgu a karakteri üzerinedir
            =>mn    : 1 match (mn stringi şarttaki dizilimi sağlıyor( a karakteri olmasa bile eşleşme sağlanır))
            =>man   : 1 match (man stringi şarttaki dizilimi sağlıyor( a karakteri burada bulunuyor))
            =>main  :No match (main stringi şarttaki dizilimi sağlamıyor( yani a dan sonra i karakteri bulunduğu için eşleşme sağlanamıyor))
'''

a= re.findall("sa*t",str) # strdeki saat elemanı içinde iki tane a karakteri olduğu için bir liste oluşturur
print(a)            

b = re.findall("ram*ing","programming")
print(b)
# findall metodu eğer sağlanıyorsa sadece sorgulanan kısmı liste elemanı yapar

c = re.findall("hb*r",str) # strde ilk parametredeki formatı sağlayan bir unsur olmadığı için boş liste dönecektir
# eğer r yerine e yazsaydık rehber elemanından dolayı listede 'hbe' diye bir eleman olacaktı
print(c)


'''

    + - bir karakterin bir yada daha fazla olmasını kontrol eder
        * daki gibi 0 olması önemsiz değildir
        yani karakterin diziliş uygunluğu içerisinde varlığını sorgular
        
        ma+n sorgu yine a karakteri üzerinedir
            =>mn    : No match (dizilişe uygun fakat a karakteri bulunmuyor)
            =>man   : 1 match (hem dizilişe uygun hem de a karakterini barındırıyor)
            =>main  :No match (a karakteri bulunuyor fakat dizilişe uygun değil)
                              (a dan sonra i karakteri bulunduğu için eşleşme sağlanmaz)
'''

x = re.findall("sa+t",str)
print(x)                       

y = re.findall("ku+su",str)
print(y)                   
# str içinde belirtilen şekilde eleman bulunmadığı için boş bir liste döndürülür

z = re.search("sa+tt",str)
print(z)
# sondaki t str içindeki saat elemanında bulunmadığı için obje oluşmaz

print(re.search("r+su",str)) # str içindeki kursu elemanı ilk parametredeki ifadeyi barındırıyor
# çıktı olarak eğer sağlanıyorsa sorgulanan ifade obje olarak oluşturulur


'''

    ? -bir karakterin sıfır ya da bir kez olmasını kontrol eder
       * ve + dan farkı en fazla bir tane bulunmasıdır
       
       ma?n
            =>man   :1 match 
            =>maan  :No match(1 den fazla bulunduğu için eşleşme sağlanamıyor)
            =>mn    :1 match (a nın olmaması da şartı sağlar dizilim belirtildiği gibi olduğu sürece)
            =>main  :No match (a 1 tane bulunuyor fakat i karakteri şartta bulunmadığı için eşleşme sağlanamıyor)
'''

print(re.findall("sa?t",str)) # str içinde saat elemanında iki tane a karakteri olduğu için boş liste çıkar
print(re.findall("Reh*b",str)) # şartı sağlayan eleman vardır


'''
    {} -karakter sayısını kontrol eder

        al{2}   : a karakterinin arkasında l karakterinin 2 kere tekrarlanması şartıyla arar
        al{2,4} :a karakterinin arkasında l karakterinin en az 2 en fazla 4 kere tekrarlanması şartıyla arar
        [0-9]{2,4}  :en az 2 en fazla 4 basamaklı sayı şartıyla arar
'''

print(re.findall("a{2}",str)) # str içinde a karakterinin 2 kere tekrarlandığı kısmı sorar
# findall metodu sebebiyle bununla bir liste oluşturur

print(re.findall("[0-9]{2}",str)) # str içinde rakamların 2 kere yan yana sıralandığı kısmı sorar        

'''
    | -alternatif seçeneklerden birinin gerçekleşmesi gerekir

        a|b =>a ya da b

            =>cde   :no match
            =>ade   :1 match
            =>acdbea    :3 match
'''
print(re.findall("R|r",str))        

'''
    () -gruplamak için kullanılır(or | ifadesi kullanılır)
    
        (a|b|c)xz =>a veya b veya z karakterlerinin arksaında xz olmalıdır
'''
print(re.findall("(R|r)eh",str))    
        
'''  
    \ -özel karakterleri aramamızı sağlar
        \$a => $a karakterini arar.yani slashdan dolayı $ karakteri regular exp. tarafından yorumlanmaz
    
    \A -belirtilen karakter stringin başında mı?
        \Athe => 'the' stringin başında mı
        
    \Z -belirtilen karakter stringin sonunda mı?
        the\Z => 'the' stringin sonunda mı                          

    \b -belirtilen karakter kelimenin başında ya da sonunda mı?
        \bthe => "the" kelimenin başında mı
        the\b => "the" kelimenin sonunda mı  
        
    \B -belirtilen karakter kelimenin başında ya da sonunda değil mi
        \Bthe => "the" kelimenin başında değil mi
        the\B => "the" kelimenin sonunda değil mi

    \d -[0-9] ile aynı anlama gelir
        \d => 12abc34
        
    \D -[^0-9] ile aynı anlama gelir     
    
    \s -boşluk karakterini arar
    
    \S -boşluk karakteri dışındakileri arar
    
    \w -alfabetik karakterler, rakamlar ve alt çizgi karakterinin tümünü arar
    
    \W -\w nin tam tersi işlem yapar    
'''                                     