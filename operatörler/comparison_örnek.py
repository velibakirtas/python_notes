#1
a = int(input('1.sayı: '))
b = int(input('2.sayı: '))
buyuk = a > b 
print(f'a: {a}, b: {b} den büyüktür: {buyuk}')

#2
x = int(input('vize1: '))
x2 = int(input('vize2: '))
y = int(input('final: '))

xP = ((x + x2) *40) /100
yP = (y*40) / 100
ort = (xP + yP) / 3
ortez = ort >= 50 
print(f'not ortalamanız: {ort}, durumunuz: {ortez}')

k = int(input('sayı girin: '))
nit = k % 2 == 0
print(f'girilen sayının çift olma durumu: {nit}')