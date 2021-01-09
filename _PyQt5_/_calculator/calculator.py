import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        
        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,500,500)
        self.initUI()
        
    def initUI(self):
        self.lbl_no1 = QtWidgets.QLabel(self)
        self.lbl_no1.setText("Sayı 1: ")
        self.lbl_no1.move(50,30)
        
        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)
        
        self.lbl_no2 = QtWidgets.QLabel(self)
        self.lbl_no2.setText("Sayı 2: ")
        self.lbl_no2.move(50,80)
        
        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)    
        
        self.btn_topla = QtWidgets.QPushButton(self) 
        self.btn_topla.setText("Toplama")
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesapla)
        
        self.btn_cikar = QtWidgets.QPushButton(self) 
        self.btn_cikar.setText("Çıkarma")
        self.btn_cikar.move(150,160)
        self.btn_cikar.clicked.connect(self.hesapla)
        
        self.btn_carp = QtWidgets.QPushButton(self) 
        self.btn_carp.setText("Çarpma")
        self.btn_carp.move(150,190)
        self.btn_carp.clicked.connect(self.hesapla)
        
        self.btn_bol = QtWidgets.QPushButton(self) 
        self.btn_bol.setText("Bölme")
        self.btn_bol.move(150,220)
        self.btn_bol.clicked.connect(self.hesapla)
        
        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.setText("sonuç: ")
        self.lbl_sonuc.move(150,290)
    
    # def top_click(self):
    #     top_result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
    #     self.lbl_sonuc.setText("sonuç: " + str(top_result))
        
    # def cikar_click(self):
    #     cik_result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
    #     self.lbl_sonuc.setText("sonuç: " + str(cik_result))
        
    # def carp_click(self):
    #     carp_result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
    #     self.lbl_sonuc.setText("sonuç: " + str(carp_result))
        
    # def bol_click(self):
    #     bol_result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
    #     self.lbl_sonuc.setText("sonuç: " + str(bol_result))
    
    def hesapla(self):
        sender = self.sender().text()
        result = 0
        
        if sender == "Toplama":
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender == "Çıkarma":
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender == "Çarpma":
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender == "Bölme":
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
            
        self.lbl_sonuc.setText("sonuç: " + str(result))            
            

        
def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
    
app()    

    
                