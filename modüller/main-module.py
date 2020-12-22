import makemodule

num = makemodule.number
nums = makemodule.numbers
per = makemodule.person
choosePer = makemodule.person['age']

makemodule.func(15)

p = makemodule.Person()
# p'yi Person classının bir objesi olarak tanımladık
p.speak()


print(num)
print(nums)
print(per)
print(choosePer)





'''
python kontrol istemcisinde sys classını import ederek python içindeki içeriklere(modül,kütüphane,fonksiyon,class) ulaşılabilir
sys.builtin_module_names fonksiyonu ile python içindeki bütün hazır gelen modül isimlerini görüntüleyebiliriz
sys.path fonksiyonu ile python'ın kurulu olduğu dizini ve python'ın alt dizinlerini görüntüleyebiliriz
'''