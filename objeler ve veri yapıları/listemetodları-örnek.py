names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years = [1998, 2000, 1998, 1987]

#1
names.append('Cenk')
print(names)
#ya da

#2
names.insert(0,'Sena')
print(names)

#3
'''
names.pop(3) #index no ile sildik
print(names) 
'''
#ya da 
names.remove('Deniz')
print(names)

#4
index = names.index('Ali')
print(index)

#5
aliIn = 'Ali' in names
print(aliIn)
#ya da
indexAli = names.index('Ali')
print(indexAli)

#6
names.reverse()
print(names)

years.reverse()
print(years)

#7
names.sort()
print(names)

#8
years.sort()
print(years)

#9
kd = 'Chevrolet, Dacia'
kdspl = kd.split(',')
print(kdspl)

#10
minY = min(years)
print(minY)

maxY = max(years)
print(maxY)

#11
countY = years.count(1998)
print(countY)

#12
clearY = years.clear()
print(clearY)

#13)kullanıcıdan aldığınız 3 tane marka bilgisini bir listede saklayınız
markalar = []

marka = input('marka: ')
markalar.append(marka)

marka = input('marka: ')
markalar.append(marka)

marka = input('marka: ')
markalar.append(marka)

print(markalar)