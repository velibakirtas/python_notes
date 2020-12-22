#BANKAMATİK UYGULAMASI

veliHesap = {
    'ad': 'Veli Bakirtas',
    'hesapNo': '12536',
    'bakiye': 3000,
    'ekHesap': 2000,
}

mehmetHesap = {
    'ad': 'Mehmet Bakirtas',
    'hesapNo': '19489',
    'bakiye': 2000,
    'ekHesap': 1000,
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print('paranızı alabilirsiniz')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']      
        
        if toplam >= miktar:
            ekHesapKullanimi = input('ek hesap kullanılsın mı: (e/h) ')
            
            if ekHesapKullanimi == 'e':
                ehkm = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ehkm
                print('paranızı alabilirsiniz')  
            else:
                print(f"{hesap['hesapNo']} no'lu hesabınızda ana bakiye olarak {hesap['bakiye']} TL bulunmaktadır")
        else:
            print('üzgünüz, bakiye yetersiz')                


paraCek(mehmetHesap,7000)    