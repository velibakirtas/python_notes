'''
FONKSİYONLARA PARAMETRE OLARAK FONKSİYON GÖNDERMEK
'''

def toplama(a,b):
    return a + b

def cikarma(a,b):
    return a - b

def carpma(a,b):
    return a * b

def bolme(a,b):
    return a / b

def islem(f1,f2,f3,f4,islem_adi):
    # f1, f2, f3, f4 parametreleri dışarıdan alıncak fonksiyyonları temsil ediyorlar(kullanımlarından bağımsız olarak)
    if islem_adi == 'toplama':
        print(f1(2,3))
    elif islem_adi == 'cikarma':
        print(f2(5,3))
    elif islem_adi == 'carpma':
        print(f3(3,2))        
    elif islem_adi == 'bolme':
        print(f4(4,2))        
    else:
        print('gecersiz islem')
        
islem(toplama,cikarma,carpma,bolme,'toplama')       
islem(toplama,cikarma,carpma,bolme,'cikarma') 
islem(toplama,cikarma,carpma,bolme,'carpma') 
islem(toplama,cikarma,carpma,bolme,'bolme')  
# fonksiyonu çalıştırabilmek için islem fonksiyonuna parametre olarak 
# daha önce tanımlanmış olan (toplama,cikarma,carpma,bolme) fonksiyonları kullandık
