liste = [1, 2, 3]

tupleL = (1, 'iki', 3)

print(type(liste))
print(type(tupleL))

print(tupleL[2])

print(len(tupleL))

liste = ['7', 11]
tupleL = ('dokuz', '0', 'dokuz')
print(liste)
print(tupleL)
#listelerin içeriklerini silip listeye farklı içerikler koyduk

liste[0] = 'ahmet'
#listenin 0 ıncı indexindeki elemanı 'ahmet' elemanı ile değiştidik

'''
tupleL[0] = 10
'''
#tuple liste türünde herhangi bir indexe bir atama yapılamaz
#tuple liste türü oluşturulduktan sonra liste içindeki içeriğin tamamı dışında herhangi bir değişiklik yapılamaz

countT = tupleL.count('dokuz')
print(countT)
#tuple içerisinde belirttiğimiz elemandan kaç tane olduğunu gösterir

indexT = tupleL.index('dokuz')
print(indexT)
#tuple içinde sorduğumuz elemanın ilk var olduğu index numarasını verir

names = ('veli', 'mehmet', 'hülya')
allT = names +tupleL
print(allT)
#ya da
allT2 = ('veli', 'mehmet', 'hülya') + tupleL
print(allT2)
#tuple listeler + operatörü ile birleştirilerek tek bir tuple haline getirilebilir
