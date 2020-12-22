website = "http://www.velibakirtas.com"
course = "Python Kursu: Baştan Sona Python Programlama (40 saat)"

#1
greeting = ' Hello world '
stripGreeting = greeting.strip()
print(stripGreeting)

#2
webS = website.lstrip('htp:/')
print(webS)

#3
lowerC = course.lower()
print(lowerC)

#4
websiteA = website.count('a')
print(websiteA)

#5
isStart = website.startswith('www')
print(isStart)

isFinish = website.endswith("com")
print(isFinish)

#6
findWeb = website.find('.com')
isFind = findWeb
print(isFind)

#7
alfabet = course.isalpha() #course ifadesindeki bütün karakterler alfabetik mi?
print(alfabet)

digit = course.isdigit() #course ifadesindeki bütün karakterler sayı mı
print(digit)

#8
text = 'contents'
c1 = text.center(50,'*')
print(c1)

#9
replaceC = course.replace(" ","-")
print(replaceC)

#10
stripGreeting2 = stripGreeting.replace("world","There")
print(stripGreeting2)

#11
courseS = course.split()
print(courseS)