website = 'http://www.velibakirtas.com'
course = 'Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)'
 
print(len(course)) #1

print(website[7:10]) #2

print(website[24:27]) #3

uzunlukC = len(course)
print(uzunlukC)
print(course[:15])
print(course[50:65]) #4



course[::] #köşeli parantez içindeki '::' str ifadenin tamamını temsil eder.
print(course[::-1]) #-1 ifadesi ile yazdırmayı tersten başlatabiliriz

print(course[:-66:-1])


#Hello world str ifadesindeki w yi W yap
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]
print(s)

s.replace('w', 'W') # .replace komutu ile str ifade içindeki belirtilen karakteri istenen karakterle değiştirebiliriz.