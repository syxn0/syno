import sys, sqlite3
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from windows.login_page import Ui_MainWindow as Login
from windows.dashboard2_page import Ui_MainWindow as Dashboard
# from sidebar import Ui_MainWindow as Dashboard

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db_conn = sqlite3.connect("data.db")
        self.sql = self.db_conn.cursor()
        self.sql.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, user_type INTEGER NOT NULL)")
        self.db_conn.commit()
        self.session_type = 1
        self.user_sessions = {
            0 : 'User not logged',
            1 : 'User is logged'
        }
        self.session()
    
    def sidebar(self,Sidebar):
        Sidebar()


    def __userExists(self, username, password):
        self.sql.execute("SELECT * FROM users WHERE username = ? AND password = ?;",(username, password))
        results = self.sql.fetchall()
        if(len(results) > 0):
            return True
        return False
    
    def __handle_setup(self):
        self.ui.setupUi(self)
        if(self.session_type == 1):
            self.ui.sidebar_menu2.setHidden(True)

    def show_message(self, title, text, icon_type):
        msg = QMessageBox()
        msg.setIcon(icon_type)
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('icon.png'))
        msg.setText(text)
        msg.exec_()

    def session(self):
        if(self.session_type == 0):
            self.ui = Login()
        elif(self.session_type == 1):
            self.ui = Dashboard()
 
        self.__handle_setup()        
    
    def on_login_pressed(self):
        username = self.ui.user.text()
        password = self.ui.password.text()
        isValid = self.__userExists(username, password)
        if(isValid):
            self.session_type = 1
            self.session()
        else:
            self.show_message("ERROR", "Incorrect login credentials!", QMessageBox.Warning)
        
    def on_sidebar_menu2_pressed(self):
        print("FUCK")


    # def on_stackedWidget_currentChanged(self, index):
    #     btn_list = self.ui.sidebar_menu.findChildren(QPushButton) \
    #                 + self.ui.sidebar_menu2.findChildren(QPushButton)

    #     for btn in btn_list:
    #         if index in [1,2,3,4]:
    #             btn.setAutoExclusive(False)
    #             btn.setChecked(False)
    #         else:
    #             btn.setAutoExclusive(True)    

    # def on_dashboard_button_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(1)

    # def on_print_button_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(2) 

    # def on_help_button_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(3) 

    # def on_aboutus_button_toggled(self):
    #     self.ui.stackedWidget.setCurrentIndex(4)  
    




if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

