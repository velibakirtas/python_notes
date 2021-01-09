from PyQt5 import QtWidgets
import sys
from mainwindow import Ui_MainWindow # py dosyasına dönüştürülen mainwindow dosyasının modül olarak kullanıp Ui_MainWindow classını import ediyoruz


class myApp(QtWidgets.QMainWindow):
    # app classında QMainWindow classını miras olarak aldık
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()

        # nesne üzerinden ui ı mainwindow modülünün Ui_MainWindow classının objesi haline getirdik
        # yani myApp veya QMainWindow classının objeleri .ui ile Ui_MainWindow classının da objesi haline getirdik
        self.ui.setupUi(self)
        # Ui_MainWindow classının setupUi metodunu çalıştırarak form dış görünüşünü düzenledik
        self.ui.btn_toplama.clicked.connect(self.hesapla)
        self.ui.btn_cikarma.clicked.connect(self.hesapla)
        self.ui.btn_carpma.clicked.connect(self.hesapla)
        self.ui.btn_bolme.clicked.connect(self.hesapla)
        
    def hesapla(self):
        sender = self.sender().text()
        result = 0
        
        if sender == "Toplama":
            result = int(self.ui.txt_line.text()) + int(self.ui.txt_line2.text())
        elif sender == "Çıkarma":
            result = int(self.ui.txt_line.text()) - int(self.ui.txt_line2.text())
        elif sender == "Çarpma":
            result = int(self.ui.txt_line.text()) * int(self.ui.txt_line2.text())
        elif sender == "Bölme":
            result = int(self.ui.txt_line.text()) / int(self.ui.txt_line2.text())
            
        self.ui.lbl_sonuc.setText("sonuç: " + str(result))    
        
def app():
    app = QtWidgets.QApplication(sys.argv)      
    win = myApp()
    # wini myApp sınıfının objesi haline getirdik
    win.show()
    # win objesini kullanarak show metoduyla myApp classında oluşturulan pencereyi çalıştırdık
    sys.exit(app.exec_())
    
app()    