from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from _msgboxForm import Ui_MainWindow
import sys

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        """
        self.ui.btn_exit.clicked.connect(self.showDialog)
        """
    """        
    def showDialog(self):
        # aşağıda açıklamasıyla bulunan işlemleri daha kısa halde gerçekleştirebiliriz
        result = QMessageBox.question(self, "Close Application","Are you sure ?",QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Cancel)
        # question metodu aynı zamanda mesaj penceresinde tıklanan butonun bilgisini döndürür
        if result == QMessageBox.Ok:
            QtWidgets.qApp.quit()
        # result değeri Ok butonunun değerini döndürürse uygulama kapatılacak            
    """
       
# QMessageBox sınıfının question metoduyla aşağıdaki yapılan işlerin bir kısmını daha kısa şekilde yapabiliriz
#question metodunun ilk parametresi objeyi alır,
# >>> 2. parametresi mesaj penceresinin ismini alır, 
# >>> 3. parametresi kullanıcıya gösterilecek mesaj içeriğini alır, 
# >>> 4. parametresi mesaj kutusunda bulunacak butonları alır,
# >>> 5. parametresi default seçilen buton bilgisini alır         
        
        
    """
        msg = QMessageBox()
        # üzeinde metotları kullanabilmek için QMessageBoxın bir objesini oluşturduk
        
        msg.setWindowTitle("Close Application")        
        # setWindowTitle metoduyla bir mesaj penceresi oluşturduk ve pencereye Close Application ismini verdik
        
        msg.setText("Are you sure? ")
        # setText metoduyla pencerede kullanıcıya gönderilecek mesajı yazdık
        
        msg.setIcon(QMessageBox.Warning)
        # setIcon metoduyla kullanıcıya gönderilecek mesaj kutusunun ikonunu belirledik
        # alternatif birçok ikon kullanılabilir
        
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore) 
        # mesaj penceresine kullanıcının dönüt verebilmesi için 3 tane buton ekledik
        
        msg.setDefaultButton(QMessageBox.Cancel)
        # Cancel butonunu default olarak seçilmiş gönderdik ama kullanıcı hala seçimde özgür
        
        msg.setDetailedText("details...............")
        # gönderilen mesajla ilgili kullanıcıya daha detaylı bilgi vermek için setDetailText metodunu kullanabiliriz
        # parametreye girilen str ifade detay bilgisi olarak sunulur
        
        msg.buttonClicked.connect(self.popup_button)
        # mesaj penceresinde tıklanılan butonların işlevlerini popup_button metoduna bağladık
        # buttonClicked metodu ilişkili oluğu metoda basılan butondan ürettiği objeyi gönderir
        
        x = msg.exec_()
        # mesaj kutusunsa kullanıcıdan gelen dönütü x değerine attık
        # x değeri bize tıklanan dönüt butonlarına göre farklı sayısal değerler döndürür
        print(x)
        
        
        Ok => 1024
        Ignore => 1048576
        Cancel => 419304 (pencerenin sağ üstündeki kapatma işareti de aynı değeri döndürür)
        
    def popup_button(self,i): # 2. parametredeki i'ye basılan butonun nesnesi gönderilir
        print(i.text())
        # i üzerinden basılan butonun textine ulaşabiliriz
        # ulaşılan text bilgisini if bloğunda değerlendirebiliriz
        if i.text() == "OK":
            QtWidgets.qApp.quit()
            # kullancı OK butonuna bastığında qApp in quit metoduyla kapanmasını sağladık
    """        
                
        
def app():
    app = QtWidgets.QApplication(sys.argv)        
    win = Window()
    win.show()
    sys.exit(app.exec_())
app()    