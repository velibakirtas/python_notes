numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
print(val)
#liste içindeki minimum değeri bulur
#letters üzerinden yaparsak alfabetik sırayı ele alır ve 'a' elemanını bulur

maxN = max(numbers)
print(maxN)
#liste içindeki maximum değeri bulur
#letters üzerinden yaparsak alfabetik sırayı ele alır ve 'y' elemanını bulur

splN = numbers[3:5]
print(splN)
#liste içinden istediğimiz elemanları alabiliriz

numbers[4] = 40
print(numbers)
#liste içinde istediğimiz indexteki elemnı değiştirebiliriz

numbers.append(12)
print(numbers)
#append metodu ile listeye belirttiğimiz elemanı ekler

numbers.insert(2,97)
print(numbers)
#insert metodu ile liste içinde istediğimiz konuma belirttiğimiz elemanı ekler

numbers.pop(2)
print(numbers)
#pop metodu ile listeden belirttiğimiz indexteki elemanı silebiliriz.
#metoda parametre atanmadığı zaman listenin en sonundaki elemanı siler.

numbers.remove(5)
print(numbers)
#remove metodu ile silmek istediğimiz elemanı belirterek silebiliriz

numbers.sort()
print(numbers)
#sayısal değerler üzerinden listeyi sıraya sokar

letters.sort()
print(letters)
#alfabetik sıra üzerinden listeyi sıraya sokar

numbers.reverse()
print(numbers)
#reverse metodu ile listeyi tersine çevirebiliriz

countN = numbers.count(10)
print(countN)
#count metodu ile istediğimiz elemanın liste içinde kaç tane olduğunu saydırabiliriz

inG = 'g' in letters
print(inG)
#in metodu ile istediğimiz elemanın liste içinde olup olmadığını sorgulatabiliriz
numbers.clear()
print(numbers)
#lite içindeki bütün elemanları siler.


