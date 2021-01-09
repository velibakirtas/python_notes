import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon



class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__() #yeni modül oluşturulduğunda modülün init metodu  miras alınan modülün init metodunu siler
        # miras alınan modülün init metodunun silinmemesi için super().__init__() metodu kullanılır
        
        self.setWindowTitle("a")
        self.setGeometry(100,300,200,200)
        self.setWindowIcon(QIcon("AppIcons.png"))
        self.setToolTip("deneme tooltip")
        self.initUI()
        # sınıf oluşturulduğunda pencere özellikleri tanımlandı ve aşağıdaki initUI içinde oluşturulan pencere elemanları class özelliği olarak çalıştırıldı
        
        
    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)

        self.lbl_name.setText("adınız: ")
        self.lbl_name.move(50,30)
    
        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("soyadınız: ")
        self.lbl_surname.move(50,70)
        
        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(100,130)
        # butona tıklandığında ilişkilendirebileceğimiz bir label oluşturduk
    
        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(100,30)
    
        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(100,70)
        
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(100,110)
        self.btn_save.clicked.connect(self.clicked)
    
    def clicked(self):
        self.lbl_result.setText("ad: " + self.txt_name.text() + "soyad: " + self.txt_surname.text())
# butona tıklandığında ilişkiendirdiğimiz clicked fonksiyonu çalışır ve class içindeki txt_name ve txt_surname özelliklerine ulaşıp setText metoduyla pencerede yazdırılır
        
def window():
    app = QApplication(sys.argv)
    win = MyWindow()        
    win.show()
    sys.exit(app.exec_())
window()    
    