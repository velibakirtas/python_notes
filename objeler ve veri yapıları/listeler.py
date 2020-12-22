#str ifade bie karakter dizisidir.
#str içindeki her bir karakter listenin bir öğesini temsil eder

my_list = [1,2,3]
print(my_list)

mylist = ['bir',2,True,5.6]
print(mylist)

list1 = ['one','two','three']
list2 = ['four','five','six']
allList = list1 + list2
print(allList)
#+ operatörü verilen listeleri tek bir liste haline getirir.

print(len(allList))

print(allList[0])

userA = ['veli',21]
userB = ['mehmet',16]
users = [userA,userB] # bu şekilde dizi içerisinde dizi oluşturulabilir.
print(users)
print(users[1])

a = users[0]
print(a[0])

print(users[0][0]) #yukarıdaki işlem bu şekilde de yapılabilir.

