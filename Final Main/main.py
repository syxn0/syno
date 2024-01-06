import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from windows.login_page import Ui_MainWindow as Login


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
    
    def onclicklogin(self):
        self.button.clicked.connect(self):
    
    def log_page(self):
        def __init__(self):
            super(log_page,self).__init__()
            
    
    
        

if __name__ == "_main_":
    app = QApplication(sys.argv)
    window = MainWindow()
    msg = QMessageBox()
    window.show()
    sys.exit(app.exec_())