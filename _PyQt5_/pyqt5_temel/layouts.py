import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        # fonu otomatik doldur fonksiyonunu True olarak tanımladık
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)
        
        layout = QtWidgets.QVBoxLayout()
        # dikey bir layout(düzen) oluşturmak için bir obje yarattık
        ##layout = QtWidgets.QHBoxLayout()
        # QHBoxLayout metodu ile yatay widgetlardan oluşan bir layout oluşturabiliriz
        
        layout.addWidget(Color("red"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("green"))
        # addWidget metodu ile layoutların widgetlerini ekledik
        #parametresindeki Color keywordü ile fon renklerini belirledik
        layout.setSpacing(50)
        # layoutun her bir elemanı için arada parametredeki birim kadar boşluk bırakır
        
        """
        hlayout1 = QtWidgets.QHBoxLayout()
        hlayout1.addWidget(Color("red"))
        hlayout1.addWidget(Color("blue"))
        hlayout1.addWidget(Color("green"))
        # yatay bir layout oluşturduk ve 3 tane widget ekledik
        
        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(Color("red"))
        hlayout2.addWidget(Color("green"))
        # ikinci bir grup layout oluşturduk ve 2 widget ekledik
        
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addWidget(Color("red"))
        vlayout.addWidget(Color("green"))
        # 2 widgetten oluşan dikey bir layout oluşturduk
        
        widget = QWidget()
        # layoutları pencereye eklemek için QWidget classının bir objesini oluşturduk
        widget.setLayout(vlayout)
        # setLayout metodu ile layoutları pencereye ekledik
        # parametreye atadığımız vlayoutu widget merkezi olarak aldık
        """
        #-----------------------------------------------------------------------------------------
        """
        # grid oluşturma
        layout = QtWidgets.QGridLayout()
        
        layout.addWidget(Color("red"),0,0)
        layout.addWidget(Color("blue"),0,1)
        layout.addWidget(Color("green"),1,0)
        layout.addWidget(Color("yellow"),1,1)
        # 4 tane widgettan oluşan bir grid layout oluşturduk
        """
        
        
       
        widget = QWidget()
        # oluşturduğumuz layoutu pencere ile ilişkilendirmek için QtWidgetin bir objesini oluşturduk
        widget.setLayout(layout)
        # oluşturulan obje üzerinden setLayout metodunu kullanarak parametresine oluşturulan layoutu verdik
        
        self.setCentralWidget(widget)
        
def app():
    app = QApplication(sys.argv)        
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    
app()    
