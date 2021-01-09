import sys
from PyQt5 import QtWidgets
from check_hobby import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        
        self.ui = Ui_MainWindow()
        
        # | obje üzerinden pencere tasarımının taşınması|
        self.ui.setupUi(self) 
        
        # |check_box amaç bağlantısı|
        self.ui.cinema_check.stateChanged.connect(self.show_state)
        # cinema check boxunu stateChanged metodu ile oluşturduğumuz show_state fonksiyonu ile ilişkilendirdik
        self.ui.book_check.stateChanged.connect(self.show_state)
        self.ui.sport_check.stateChanged.connect(self.show_state)
        
        # | Seçilenleri Al butonu amaç bağlantısı|
        self.ui.btn_secilenleriAl.clicked.connect(self.getAllChecked)
        
    # |btn_secilenleriAl ilişkilendirmesi |    
    def getAllChecked(self):
        result = ""
        # işaretlenen boxları yazdırmak için bir result strsi tanımladık
        items = self.ui.centralwidget.findChildren(QtWidgets.QCheckBox)
        # belirtilen dizin altındaki tüm ögelere ulaşmamızı sağlar
        # centralwidget alrındaki tüm ögelere ulaştık ve bu ögelerden QtWidgets ögesinin de altındaki tüm QCheckBox ögelerine ulaştık
        # ulaştığımız ögeler findChildren metodu gereği liste halinde tutulur
        # bu da döngü kullanmamızı müsait hale getirir
        for i in items:
            # findChildren metodundan gelen liste üzerinde döngü başlattık
            if i.isChecked():
                # boxun işaretli olması şartını koyduk
                result += i.text() + "\n"
            self.ui.lbl_result.setText(result)    
            # işaertli boxın texti resulta atıldı ve pencere içindeki label alanına setText metoduyla yazdırıldı
                
        
        
        

    #|check_box ilişkilendirmesi|    
    def show_state(self,value):        
        cb = self.sender()
        ##print(cb.text())
        # her halükarda söz konusu boxun text içeriğini döndürür
        ##print(cb.isChecked())
        # boxun işaretlenip işaretlenmediğini gösterir
        # işaretlenmişse True, işaret kaldırılmışsa False değerini gönderir
        ##print(value)
        # eğer işaretliyse 2 işaret kaldırılmışsa 0 değerini gönderir        
        
def app():
    app = QtWidgets.QApplication(sys.argv)        
    win = myApp()
    win.show()
    sys.exit(app.exec_())
    
app()    