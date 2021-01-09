from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton
import sys

class win2(QMainWindow): 
    def __init__(self):
        super().__init__()

class win1(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.Button = QPushButton("Click!")
        self.setCentralWidget(self.Button)
        self.Button.clicked.connect(self.clicked)
        
        self.secondWin = win2() 

    def clicked(self):
        self.secondWin.show()

def main():
    app = QApplication(sys.argv)
    main = win1(); main.show()
    sys.exit(app.exec_())

main()