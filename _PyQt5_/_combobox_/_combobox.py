from PyQt5 import QtWidgets
import sys
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.cbSehirler.addItem("İstanbul")
        self.ui.cbSehirler.addItem("Ankara")
        self.ui.cbSehirler.addItem("İzmir")
        # obje üzerinden cbSehirler comboboxuna ulaşıp addItem metodu ile 3 tane eleman ekledik
        
        """self.ui.cbSehirler.addItems(["Trabzon","Samsun"])"""
        # addItems metodu ile parametreye liste yollayarak birden fazla eleman comboboxa eklenebilir
        
        # | loadItem butonu amaç bağlantısı |
        self.ui.btn_loadItem.clicked.connect(self.LoadItems)
        # | GetItem butonu amaç bağlantısı |
        self.ui.btn_getItem.clicked.connect(self.GetItem)
        
        # | clear butonu amaç bağlantısı |
        self.ui.btn_clear.clicked.connect(self.ClearItems)
        
        # | seçilen eleman değişikliğinde index bilgisi almak için metot bağlantısı |
        self.ui.cbSehirler.currentIndexChanged.connect(self.SelectedChangedIndex)
        # eleman değişikliğinde yeni seçilen elemanın index bilgisini döndürür
        
        # | seçilen eleman değişikliğinde text bilgisi almak için metot bağlantısı |
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.SelectedChangedText)
        # eleman değişikliğinde yeni seçilen elemanın text bilgisini döndürür
        
        
    # | loadItem buton ilişkilendirmesi
    def LoadItems(self):
        sehirler = ["Adana","Trabzon","Samsun"]   
        self.ui.cbSehirler.addItems(sehirler)     
        
    # | getItem buton bağlantısı |
    def GetItem(self):
        """print(self.ui.cbSehirler.currentText())"""
        # currentText metodu ile cbSehirler comboboxunda seçilmiş olan geçerli elemanın text bilgisini döndürür
        """print(self.ui.cbSehirler.currentIndex())"""
        # currentIndex metodu ise comboboxta seçilmiş olan elemanın indexinin bilgisini döndürür
        """print(self.ui.cbSehirler.count())"""
        # count metoduyla da combobox içindeki elemanların sayısını verir
        
    # | clear buton bağlantısı |
    def ClearItems(self):
            self.ui.cbSehirler.clear()
            # clear metodu ile combobox içindeki tüm elemanlar silinir
    
    # | seçilen eleman değişikliğinde index bilgisini veren metot oluşturma |    
    def SelectedChangedIndex(self, index):
        print(index)   
        
    # | seçilen eleman değişikliğinde text bilgisini veren metot oluşturma |    
    def SelectedChangedText(self, text):
        print(text)          
                
            
        
app = QtWidgets.QApplication(sys.argv)        
win = Window()
win.show()
sys.exit(app.exec_())