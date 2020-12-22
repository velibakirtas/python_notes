'''
if 3>2:
    print('Hoşgeldin')
'''    
#if ile koyduğumuz şartı karşılıyorsa bir sonraki yolu takip edip Hoşgeldin yazdırır.

'''
if 3<3:
    print('Hoşgeldin')
'''    
#şart karşılanmadığı için bir sonraki aşamaya geçip ifadeyi yazdırmaz.

'''
if True:
    print('Hoşgeldin')       
'''         
#ifin bağlı olduğu şart direkt True olduğu için sonraki aşamaya geçip ifadeyi yazdırır.
#False içinse ifade direkt False değerini alacağı için sonraki aşamaya geçmez

'''
isLoggedin = True

if isLoggedin:
    print('Hoşgeldin')   
'''    
#Daha önce isLoggedin değişkenine True değerini tanımladığımız için sonraki aşamaya geçip ifadeyi yazdırır.

'''
if isLoggedin == True:
    print('Hosgeldin')
'''    
#bağlanan şart isLoggedin değişkeninin True değerine eşit olmasıdır.
#Daha önce değişkene True tanımlandığı için şart yerine getirilmiştir. Ve ifade yazdırılır



username = 'velibakirtas'
password = '12345'

islogedİn = (username == 'velibakirtas') and (password == '12345')

if islogedİn:
    print('hosgeldin')
    
#islogedİn değişkenine karşılaştırmalar atadık ve bunu ife bağlayarak True değerini almasıyla ifadeyi yazdırdık.
#Karşılaştırma operatörlerinin kullanıldığı bool ifadeyi direkt if yanına da yazabiliriz


islogedİnA = (username == 'velibakirtas') and (password == '12346')
if islogedİnA:
    print('Hosgeldiniz')       
else:
    print('Kullanıcı adı veya parola yanlış')    
#if ifadesinden alınan sonuç False ise eğer varsa else ifadesine gelip o yolu izler.   


if (username == 'velibakirtas'):
    
    if (password == '12345'):
        print('hosgeldiniz')
    else:
        print('şifre yanlış')
else:
    print('kullanıcı adı yanlış')        

# kullanıcı adı 'velibakirtas' ise password doğrula
#password '12345' ise 'hoşgeldiniz' yazdır.
#password '12345 değil ise 'şifre yanlış' yazdır
#kullanıcı adı 'velibakirtas' değil ise 'kullanıcı adı yanlış' yazdır.
