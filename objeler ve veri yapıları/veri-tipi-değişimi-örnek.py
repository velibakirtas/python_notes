'''

Daire Alanı : π(r)**2
Daire Çevresi : 2πr

Alan ve çevresini hesapla (r: 3.14)
'''

pi = 3.14

'''
r = input('yarı çap: ') 
'''
#input sadece string türünde değer verebilir.Bu sebeple bu değerin int veya float değerinde yazılması gerekli

r = float(input('yarı çap: '))
DaireAlani = pi * (r**2)
DaireCevresi = 2 * pi * r



#Tek bir print komutuyla da yazdırabiliriz

'''
print('alan: ' + DaireAlani + 'cevre: ' + DaireCevresi) #Hesaplanan değeri kullanıcıya gösterirken string bir bilgiyr dönüşmesi gerekir
'''

print('alan: ' + str(DaireAlani) + 'cevre: ' + str(DaireCevresi))
 #print komutu içinde değişken tanımlama yapılırken değişken isminden sonra + konur ve değer yazılır
