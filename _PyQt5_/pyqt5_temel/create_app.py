import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon
def window():
    app = QApplication(sys.argv)
    # QApplication metodu ile porgramı çalıştırırken kulanılan parametreleri işleme sokuyoruz
    win = QMainWindow()
    #QMainWindow metodu il e bir pencere oluşturup win değişkenine atıyoruz(örneklem oluşturma)
    # penceredeki çarpı(x) işaretine tıklandığında programın bitmesi için sys modülünün exit metoduna parametre ile exec_ metodunu gönderiyoruz
    win.setWindowTitle("a")
    # oluşturulan win penceresinin ismini tanımlıyoruz
    win.setGeometry(200,200,700,700)
    # win penceresinin boyutunu tanımlıyoruz
    win.setWindowIcon(QIcon("AppIcons.png"))
    # penceremizin ikonunu belirliyoruz
    win.setToolTip("deneme tooltip")
    win.show()
    # daha sonra oluşturulan pencereyi fonksiyon çalıştığında show metodu ile gösteriyoruz
    sys.exit(app.exec_())
    
window()
    
 