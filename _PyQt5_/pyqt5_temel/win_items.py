import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    
    win = QMainWindow()
    
   
    win.setWindowTitle("a")
    
    win.setGeometry(200,200,700,700)

    win.setWindowIcon(QIcon("AppIcons.png"))

    win.setToolTip("deneme tooltip")
    
    lbl_name = QtWidgets.QLabel(win)
    # win penceresi içinde Qtwidgets içindeki QLabel metodunu çalıştırdık
    # ve lbl_name'i bir obje haline getirdik
    lbl_name.setText("adınız: ")
    # obje üzerinden setText metodu ile pencereye adınız metnini ekledik
    lbl_name.move(50,30)
    # yazılan metni pencere içinde x ekseninde 50 birim, y ekseninde ise 30 birim sürükledik
    
    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("soyadınız: ")
    lbl_surname.move(50,70)
    
    txt_name = QtWidgets.QLineEdit(win)
    # win penceresi içinde QLineEdit metodu ile bir text kutusu objesi oluşturduk
    txt_name.move(100,30)
    # move metodu ile oluşturulan kutuyu sürükledik
    
    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(100,70)
    
    def clicked(self):
        print("butona tıklandı"+ " name: " + txt_name.text() + " surname: "+ txt_surname.text())
    # pencere içinde oluşturulan butona tıklandığında ne yapılacağını belirten özel bir fonksiyon oluşturuldu
    
    
    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Kaydet")
    btn_save.move(100,110)
    
    btn_save.clicked.connect(clicked)
    # butona işlev tanımlama için clicked.connect metodunu kullandık
    # bu metodda kullanılan parametreye bir fonksiyon atadık
    # bu fonksiyonun amacı kullanıcıya bir metin göstermek
    
    
    
    
    win.show()

    sys.exit(app.exec_())
    
window()
    
 