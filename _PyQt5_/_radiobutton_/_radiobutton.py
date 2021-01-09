from PyQt5 import QtWidgets
import sys
from radiobuttonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        ##self.ui.radio_Turkiye.setChecked(True)
        # bu şekilde ulaşılan radio butonunu seçili hale getirebilriz
        
        # | ulke radio button amaç bağlantısı |
        self.ui.radio_Turkiye.toggled.connect(self.onClicked_Ulke)
        self.ui.radio_azerbaycan.toggled.connect(self.onClicked_Ulke)
        self.ui.radio_germany.toggled.connect(self.onClicked_Ulke)
        self.ui.radio_greek.toggled.connect(self.onClicked_Ulke)
    
    # | egitim radio butonları amaç bağlantısı |
        self.ui.radio_ilkokul.toggled.connect(self.onClicked_egitim)      
        self.ui.radio_lise.toggled.connect(self.onClicked_egitim)      
        self.ui.radio_uni.toggled.connect(self.onClicked_egitim)      
        self.ui.radio_YL.toggled.connect(self.onClicked_egitim)      
    # | ulke push button amaç bağlantısı |    
        self.ui.btn_ulke.clicked.connect(self.getSelectedUlke)
        
    # | eğitim push button amaç bağlantısı |        
        self.ui.btn_egitim.clicked.connect(self.getSelectedegitim)
        
    # | ulke radio buttonları ilişkilendirmesi |    
    def onClicked_Ulke(self):
        rbu = self.sender()
        if rbu.isChecked():
            print("seçilen radio: " + rbu.text())
        
    # | egitim radio buttonları ilişkilendirmesi |
    def onClicked_egitim(self):
        rbe = self.sender()
        if rbe.isChecked():
            print("seçilen radio: " + rbe.text())       
            
    # | ülke push button ilişkilendirmesi |
    def getSelectedUlke(self):
        items = self.ui.groupBox_ulke.findChildren(QtWidgets.QRadioButton)   
        for rb in items:
            if rb.isChecked():
                self.ui.lblUlke.setText("Seçilen Ülke: " + rb.text())
                
    # | egitim push button ilişkilendirmesi |
    def getSelectedegitim(self):
        items = self.ui.groupBox_egitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lblegitim.setText("Eğitim Durumu: " + rb.text())                   
           
            
            
                         
app = QtWidgets.QApplication(sys.argv)        
win = Window()
win.show()
sys.exit(app.exec_())