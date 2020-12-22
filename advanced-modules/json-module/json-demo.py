import os
os.chdir("C:/Users/Asus/Desktop/Python/Python_Temelleri/advanced-modules/json-module")






import json
class User:
    def __init__(self, username, password,email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False # kullanıcının daha önce login olma durumunu default olarak False yapıyoruz
        self.currentUser = {} # login olan kullanıcının bilgilerinin saklanacağı ortam olarak boş bir dict tanımlıyoruz
        # login olan kullanıcının verileri currentUser objesi içinde saklanacaktır
        
        #load users .json file
        # json dosyasındaki bilgileri uygulama içerisindeki users objesine aktarmak için bir metod kullanıcaz
        self.loadUsers() #userRepository oluştuğu anda loadUser metodunu çağırdık
        
    def loadUsers(self):
        if os.path.exists("users.json"): #exists metodu ile dosyanın varlığını kontrol ettik ve bunu if bloğuna bağladık
            # eğer dosya varsa dosyayı "r" formatında açtık ve file referansına tanımladık
            with open("users.json", "r",encoding="utf-8") as file: 
                users = json.load(file) # file içine attığımız dosya içeriğini load metodu ile çalışma alanımıza çektik
                #print(users)
                # görüldüğü üzere gelen veri hala json string bilgisi şeklindedir
                for user in users:
                    user = json.loads(user)
                    # loads metodu bir str json bilgisini standart veri tipine dönüştürmeyi sağlar
                    # artık json dosyasından çektiğimiz verinin üzerinde işlem yapabilir, istediğimiz elemanına ulaşabiliriz
                    newUser = User(username = user["username"], password = user["password"], email = user["email"])
                    self.users.append(newUser)
                    print(self.users)
        
    def register(self,user: User): # user bilgisinin User classı niteliği olmasını sağladık
        #kullanıcı kayıt
        self.users.append(user) # geken kullanıcı bilgisini users listesine ekledik
        self.savetoFile()
        print("Account Created")


    
    def login(self, username, password): #giriş
        # kullanıcıdan giriş için username ve password parametresi istedik
        for i in self.users: # userRepository classındaki users listesindeki verileri sırayla i referansına attım
            if username == i.username and password == i.password: # listedeki bilgilerle kullancıı bilgilerinin aynı olup olmadığını sordum
                self.isLoggedIn = True # eğer doğruysa isLoggedIn özelliğini True olarak değiştirdim
                self.currentUser = i # kullancının istediği bir zaman kullanabilmesi için bilgilerini iöinde barındıran bir özellik tanımladım
                print("Logged in")
                break
            
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print("Logged out")        
        
    def identity(self):
        if self.isLoggedIn:
            print(f"username: {self.currentUser.username}")
        else:
            print("Could not login")                            
    
    def savetoFile(self): #json dosyasına kayıt
        # json dosyasına veri göndermeden önce elimizdeki verinin json dosyasına girmeye uygun olması gerekir
        # UserRepository classının user özelliğindeki listeyi atmak istersek:
        # json dosyası class özelliklerini barındıramadığı için hata döndürülecektir
        # bunun için elimizdeki verinin json dosyasına eklenmeye uygun hale getirmemiz gerekir
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
            # __dict__ metoduyal UserRepository classı özelliği içeriğinin dict veri yapısına çevirdik
            # ve json dosyasına kayıt etmek için bu dicti string json haline getirdik(dumps metodu ile)
            # dumps metoduna parametre olarak user.__dict__ metodunu attık(classı dict veri yapısına çevirdik)
        with open("users.json","w") as file:
            json.dump(list, file)
        # dosyayı "w" formatında açtık
        # dump metoduyla, oluşturulan list listesini json dosyasına kayıt ettik              

repository = UserRepository() #repositoryi UserRepository classının bir objesi haline getirdik
    
while True:
    print(" Menu ".center(40,"*"))    
    choice = input("1- Register\n2- Login\n3- Logout\n4- Identity\n5- Exit\nYour choice: ")
# identity = kimlik bilgisi öğrenme     
    if choice == "5":
        break
    else:
        if choice == "1":
            #register
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            
            user = User(username = username, password = password, email = email) #herhangi bir hata almamak için attribute garantiye aldık
            #userı User classının bir objesi haline getirdik
            repository.register(user)
# repositoryi yukarıda UserRepository classının bir objesi olarak tanımladık 
# #classın register metoduna user parametresini göndererek  hesap oluşturan kullanıcı bilgilerini users listesine ekledik           
        
        elif choice == "2":
            #Login
            if repository.isLoggedIn:
                print("Already logged in")
            else:    
                username = input("username: ")
                password = input("password: ")
                repository.login(username, password)
        elif choice == "3":
            #logout
            repository.logout()
        elif choice == "4":
            #identity
            repository.identity()
        else:
            print("False choice")
            

# ilk önce menü iskeletini

# User classındaki özellikleri belirle metodunu oluştur

# UserRepository classı metotlarını ve özelliklerini belirle

# UserRepository classın oluştuğunda loadUsers metodunu çalıştır(sonradan oluşturulacak)

# UserRepository classındaki register olan kullanıcının verilerinin tutulacağı veri tipini belirle

# yine UserRepository classındaki kullanıcı giriş durumunu belirleyen değişkeni belirle(default False)

# UserRepository classında, kullaıcı istediğinde bilgilerini görüntülemek için bilgilerini barındıran bir dict tanımla
# register metodunu oluştur


# register metodu çalıştığında UserRepository classındaki register olan kullnaıcının verilerinin tutulduğu alana yeni register yapan kullancının  veirlerini ekle

# yine register metodunda savetoFile adında bir metot çalıştır

# savetoFile metodunu oluştur

# savetoFile görev: bu metotta boş bir list listesi oluştur

# savetoFile görev2: UserRepository classındaki users listesi için for döngüsünü başlat

# savetoFile görev3: döngüden gelecek elemanları dumps metoduyla -dict veri haline getirdğimiz veriyi-  json dosyasına kayıt edilmeye müsait hale getirip oluşturduğumuz boş list listesine ekle

# savetoFile görev4: sonra user.json dosyasını "w" formatında açarak içi doldurulan list listesini user.json dosyasına kaydet

# UserRepository classının repository adında bir örneklemesini oluştur

# loadUsers adında bir fonksiyon oluştur ve görevini belirle

# loadUsers görev: eğer sistemde user.json adlı bir dosya varsa dosya okunsun

# loadUsers görev2: okunan dosya içeriği load metoduyla çalışma alanına çekilsin ve içerik users adlı bir değişkene atılsın

# loadUsers görev3: for döngüsü ile users elemanları alınıp user adlı bir referanslama yapılsın

# loadUsers görev4: her user bilgisini loads metodu ile standart veri tipine dönüştür

# loadUsers görev5:newUser adında User classının bir örneklemesini oluştur paramaetre olarak da görev 4 deki user verisinden username, password ve email bilgilerini al

# newUser örneklemesini append metoduyla UserRepository örenkelemesinin users listesine ekle

# daha önce de söylendiği üzere loadUsers metodunu UserRepository oluştuğunda çalıştır

# kullanıcı girişi gerçekleştirmek için login metodu oluştur

# login metodu parametre olarak username ve password adında 2 tane parametre alsın

# login görev: for döngüsünde UserRepository classındaki elemanlar alınıp i referansına atılsın

# login görev2: i referansından username ve password bilgisi alınsın ve if bloğuyla dışarıdan gelecek olan username ve password parametresi ile karşılaştırılsın

# login görev3: eğer eşleşme sağlanırsa UserRepository classındaki isLoggedIn özelliği True değerine eşitlensin

# login görev4: yine UserRepository classındaki currentUser bilgisine döngüden gelen i referansı atılsın

# kullanıcı istediğinde bilgilerini görebilmek için identity adında bir metot oluşturulsun

# identity görev: if bloğunda UserRepository classındaki isLoggedIn özelliği sorgulansın. Eğer True değerine sahipse;
# identity görev2: kullanıcıya göstermek için UserRepository classındaki currentUser dictinden gerekli bilgi alınsın

# identity görev3: eğer isLoggedIn False değerine sahipse -giriş yapılmamış demektir- kullanıcıya giriş yapılmalı uyarısı verilsin

# hesaptan çıkış işlemini gerçekleştirmek için logout metodu oluşturulsun

# logout görev: metot çağırıldığında UserRepository classındaki isLoggedIn özelliğine False değeri atılsın ve currenUser dicti yeniden boş hale gelsin

# logout görev2: kullanıcıya çıkış yapıldı bilgisini versin

# daha önce oluşturulan menü iskeleti doldurulmaya başlansın

# while ile sonsuz bir döngü başlatılsın

# menü döngüsü görevi: yapmak istenilen işlemin belirlenmesi için kullanıcıdan 1 ile 5 arasında bir değer istensin(1 ve 5 dahil)

# bu işlemler sırasıyla "register", "login", "logout", "identity","çıkış"           

# menü döngüsü görevi: kullanıcıdan gelen girdi "5" ise döngü sonladırılsın

# menü döngüsü görevi(register): kullanıcıdan gelen görev "1"(register) ise kullanıcıdan username, password ve email bilgisi istensin

# menü döngüsü görevi(register1): user isminde User classının bir örneklemesi oluşturulsun ve parametre olarak kullanıcıdan alınan bilgiler class parametreleriyle eşitlensin

# menü döngüsü görevi(register2):daha önce UserRepository classının bir örneklemesi oalarak oluşturulan repository üzerinden register metodu çağırılsın ve parametre olarak User örneklemesi olan user gönderilsin

# menü döngüsü görevi(login): eğer kullanıcıdan alınan girdi "2"(login) ise if bloğu ile repository örneklemesi üzerinden isLoggedIn çağırılarak kontrol edilsin

# menü döngüsü görevi(login1): eğer isLoggedIn True değerine sahipse kullanıcıya zaten giriş yapıldı uyarısı verilsin

# menü döngüsü görevi(login2): eğer isLoggedIn False değerine sahipse kullanıcıdan username ve password bilgisi alınsın

# menü döngüsü görevi(login3): repository örneklemesi üzerinden login fonksiyonu çağırılarak parametrelerine kullanıcıdan alınan username ve password bilgisi atılsın

# menü döngüsü görevi(logout): kullanıcıdan gelen girdi "3"(logout) ise repository örneklemesi üzerinden logout metodunu çalıştırılsın

# menü döngüsü görevi(identity): kullanıcıdan gelen girdi "4"(identity) ise repository örneklemesi üzerinden identity metodunu çalıştırılsın

# menü döngüsü görevi: eğer menüde belirtilen verilerden başka bir veri girilirse yanlış seçim uyarısı gönderilsin            
