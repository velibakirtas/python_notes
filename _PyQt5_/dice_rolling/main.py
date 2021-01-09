from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QMovie
import sys
import time
from diceForm import Ui_MainWindow
import random


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.rb1.toggled.connect(self.rbClicked)
        self.ui.rb2.toggled.connect(self.rbClicked)
        self.ui.rb3.toggled.connect(self.rbClicked)
        
        
        self.ui.btn_roll.clicked.connect(self.clickConnect)
        
        
    def rbClicked(self):
        rb = self.sender()
        if rb.isChecked():
            print("current radio: "+ rb.text())
            
    def clickConnect(self):
        self.gif = QMovie("dicegif3.gif")
        self.ui.lbl_gif.setMovie(self.gif)
        self.gif.start()
        items = self.ui.groupBox.findChildren(QtWidgets.QRadioButton)           
        for rb in items:
            if rb.isChecked():
                intrbe = int(rb.text())
                if intrbe == 1:
                    self.ui.lbl_dice2.clear()
                    self.ui.lbl_dice3.clear()
                    self.dice_roll1()
                elif intrbe == 2:
                    self.ui.lbl_dice3.clear()
                    self.dice_roll1()
                    self.dice_roll2()
                elif intrbe == 3:
                    self.dice_roll1()
                    self.dice_roll2()
                    self.dice_roll3() 
                    
    def dice_roll1(self):
        coming_dice1 = random.randint(1,6)
        self.ui.lbl_dice1.setPixmap(QPixmap(f"{coming_dice1}.png"))
        print("incoming dice: {} ".format(coming_dice1))
    def dice_roll2(self):
        coming_dice2 = random.randint(1,6) 
        self.ui.lbl_dice2.setPixmap(QPixmap(f"{coming_dice2}.png"))
        print("and\n{} ".format(coming_dice2))
    def dice_roll3(self):
        coming_dice3 = random.randint(1,6) 
        self.ui.lbl_dice3.setPixmap(QPixmap(f"{coming_dice3}.png"))
        print("and\n{} ".format(coming_dice3))                                       

                    






def app():
    app = QtWidgets.QApplication(sys.argv)      
    win = Window()
    win.show()
    sys.exit(app.exec_())
    
app()    