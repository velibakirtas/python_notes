#VALUE TYPES => str ve number dahildir
x = 5
y = 25

x = y
#y değişkenindeki 25 i x'e kopyaladık
print(x,y)

y = 10
print(x,y)

#value types'de y de yaptığımız sonraki değişiklik x'i etkilemez farklı alanlarda tanımlanan değişkenlerden oluşur

#REFERENCE TYPES => list ve class dahildir
a = ['apple','banana']
b = ['apple','banana']

a = b
print(a)

b[0] = 'grape'

print(a,b)
#oluşturulan liste içinde bir adres bilgisi taşır
#bu adres bilgisinin karşılığı olan value bilgiler belleğin farklı bir alanında tutulur.
#listeler adres ile ilişkilendirilir

#iki liste birbirine eşitlendiği zaman adresler birbiriyle ilişkilendirilir.
#daha sonra listelerden birinde yapılan değişiklik aynı adres üzerindeki veriyle ilgilidir



### Value typlerda verinin kendisiyle, reference typlerde listenin adresiyle ilgileniriz