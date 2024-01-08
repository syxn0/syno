import sys, sqlite3
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from windows.login_page import Ui_MainWindow as Login
from windows.dashb_page import Ui_MainWindow as Dashboard

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db_conn = sqlite3.connect("data.db")
        self.sql = self.db_conn.cursor()
        self.sql.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, user_type INTEGER NOT NULL)")
        self.db_conn.commit()

        self.session_type = 0
        self.user_sessions = {
            0 : 'User not logged',
            1 : 'User is logged'
        }
        self.session()

    def __userExists(self, username, password):
        self.sql.execute("SELECT * FROM users WHERE username = ? AND password = ?;",(username, password))
        results = self.sql.fetchall()
        if(len(results) > 0):
            return True
        return False

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
        self.ui.setupUi(self)
    
    def on_login_pressed(self):
        username = self.ui.user.text()
        password = self.ui.password.text()
        isValid = self.__userExists(username, password)
        if(isValid):
            self.session_type = 1
            self.session()
        else:
            self.show_message("ERROR", "Incorrect login credentials!", QMessageBox.Warning)
 

if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

