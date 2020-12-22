x, y, z = 2, 5, 107

numbers = 1, 5, 7, 10, 6

#1
a = int(input('sayı girin: '))
b = int(input('sayı girin: '))
sonuc = (a*b) - (x+y+z)
print(sonuc)

#2
result = y//x
print(result)

#3
toplamD = x+y+z
modD = toplamD % 3
print(modD)

#4
us = y**x
print(us)
#ya da
us2 = y*y
print(us2)

#5
x, *y, z = numbers
kupZ = z**3
print(kupZ)

#6
print(y)
toplamY = y[0] + y[1] + y[2]
print(toplamY)