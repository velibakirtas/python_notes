#araba listesi oluştur
carlist = ['bmw','mercedes','opel','mazda']

#listenin eleman sayısını bul
print(len(carlist))

#listedeki ilk elemanı bul
print(carlist[0])

#listedeki son elemanı bul
print(carlist[3])

#mazdayı toyota ile değiştir
carlist[-1] = 'toyota'
print(carlist) #listelerde index numarası verilerek elemanlarda değişiklik yapılabilir.

#mercedes listenin elemanı mıdır
inM = 'mercedes' in carlist
#listelerde in operatörü ile istenen elemanın liste içinde olup olmadığını sorgulayabiliriz.
print(inM)

car2 = carlist[-2]
print(car2)

#listenin ilk üç elemanını al
i3 = carlist[0:3]
print(i3)

#listenin son 2 elemanı yerine toyota ve renault değerlerini ekleyin
carlist[-2:] = ['toyota','renault']
print(carlist)

#listeye audi ve nissan değerlerini ekle
carlist2 = ['audi','nissan']
carall = carlist + carlist2
print(carall)
#aşağıdaki şekilde de yapılabilir
carlistek = carlist + ['audi','nissan']
print(carlistek)

#listenin son elemanını silin
del carlist[-1] # del komutu ile liste içinden belirtilen elemanı silebilirz
print(carlist)

#listenin elemanlarını tersten yazdır
tcar = carlist[::-1]
print(tcar)

#verilen elemanları bir liste içinde sakla
      # ogrenciA = Veli Bakirtas 1999 (90,85,67)
      # ogrenciB = Mehmet Bakirtas 2004 (100,84,79)
      # ogrenciC = Hulya Bakirtas 1977 (56,87,34)
      
ogrenciA = ['Veli','Bakirtas',1999,[90,85,67]]
ogrenciB = ['Mehmet','Bakirtas',2004,[100,54,79]]
ogrenciC = ['Hulya','Bakirtas',1977,[56,87,34]]

print(ogrenciA)
print(ogrenciB)
print(ogrenciC)

print(ogrenciA[3][2])
print(ogrenciB[0])
print(ogrenciC[2])

#velinin adını soyadını yaşını ve not ortalamasını str ile yazdır
'''
f'Veli Bakirtas 21 yaşında ve not ortalaması 80'
'''
strden = f'{ogrenciA[0]} {ogrenciA[1]} {2020 - ogrenciA[2]} yaşında ve not ortalaması {(ogrenciA[3][0] + ogrenciA[3][1] + ogrenciA[3][2]) / 3}'
print(strden)