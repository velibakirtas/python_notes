'''
İDENTİTY OPERATOR: is
'''

x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)
print(x == z)
#Burada yapılan karşılaştırmalar adresin değil ona karşılık gelen verinin karşılaştırmasıdır.

print(x is y)
print(x is z)
# is operatörü ile listelerin referansları(adresleri) karşılaştırılır.

print(x is not y)


'''
MEMBERSHİP OPERATOR: in
'''
a = ['apple', 'banana']
print('banana' in a)
#'banana' elemanı a dizisinde var mıdır?

b = 'Veli'
print('l' in b)
# 'l' karakteri str ifade içinde var mı?
print('e' not in b)