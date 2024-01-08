import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from windows.login_page import Ui_MainWindow as Login
from windows.dashb_page import Ui_MainWindow as Dashboard

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.session_type = 1
        self.user_sessions = {
            0 : 'User not logged',
            1: 'User is logged'
        }
        self.session()

    def session(self):
        if(self.session_type == 0):
            self.ui = Login()
        elif(self.session_type == 1):
            self.ui = Dashboard()
        self.ui.setupUi(self)


if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

