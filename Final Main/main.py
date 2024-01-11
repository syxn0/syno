import sys, sqlite3
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from windows.login_page import Ui_MainWindow as Login
from windows.dashboard2_page import Ui_MainWindow as Dashboard
from windows.admin_dashboard_page import Ui_MainWindow as AdminDashboard


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db_conn = sqlite3.connect("data.db")
        self.sql = self.db_conn.cursor()
        self.sql.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, fullname TEXT NOT NULL, balance TEXT NOT NULL, past_bill TEXT NOT NULL, average_bill TEXT NOT NULL, kwh TEXT NOT NULL, next_due TEXT NOT NULL, user_type INTEGER NOT NULL)")
        self.db_conn.commit()
        self.session_type = 0
        self.session_uid = 0
        self.session_user_type = 0
        self.session()
    
    def sidebar(self,Sidebar):
        Sidebar()


    def __userExists(self, username, password):
        self.sql.execute("SELECT * FROM users WHERE username = ? AND password = ?;",(username, password))
        results = self.sql.fetchall()
        if(len(results) > 0):
            self.session_type = 1
            self.session_uid = results[0][0]
            self.session_user_type = results[0][-1]
            self.session()
            return

        self.show_message("ERROR", "Incorrect login credentials!", QMessageBox.Warning)
    
    def __get_users_data(self, uid):
        self.sql.execute("SELECT * FROM users WHERE id = ?;",(str(uid)))
        results = self.sql.fetchall()
        return results

    
    def __handle_setup(self):
        self.ui.setupUi(self)
        if(self.session_type == 1 and self.session_user_type == 1):
            self.ui.sidebar_menu2.setHidden(True)
            self.ui.pushButton.setText("Print Bill")

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
            self.ui = AdminDashboard() if(self.session_user_type == 0) else Dashboard()
 
        self.__handle_setup()
    
    def on_login_pressed(self):
        username = self.ui.user.text().strip()
        password = self.ui.password.text().strip()
        if(username == '' or password == ''):
            self.show_message("ERROR", "Incorrect login credentials!", QMessageBox.Warning)
            return

        self.__userExists(username, password)

    def logout(self):
        response = QMessageBox.question(self, 'Logout', 'Confirm logout?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if(response == QMessageBox.Yes):
            self.session_type = 0
            self.session()
        
    def bills_data(self):
        data = self.__get_users_data(self.session_uid)[0]
        fullname = data[3]
        balance = data[4]
        past_bill = data[5]
        average_bill = data[6]
        kwh = data[7]
        next_due = data[8]
        return fullname, balance, past_bill, average_bill, kwh, next_due
    
    def on_logout_icon_pressed(self):
        self.logout()
    
    def on_logout_button_pressed(self):
        self.logout()
    
    def on_print_button_pressed(self):
        fullname, balance, past_bill, average_bill, kwh, next_due = self.bills_data()
        filename = f'{fullname.replace(" ","_")}-Bills.txt'
        bill = open(filename, 'w')
        bill.write(f'Name: {fullname}\nBalance: {balance}\nPast Bill: {past_bill}\nAverage Bill: {average_bill}\nKwh: {kwh}\nNext Due: {next_due}')
        self.show_message("INFO", f"Success! File saved as {filename}", QMessageBox.Information)


    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.sidebar_menu.findChildren(QPushButton) \
            + self.ui.sidebar_menu2.findChildren(QPushButton)

        for btn in btn_list:
            if index in [1,2,3,4]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)    

    def on_dashboard_button_toggled(self):
        self.ui.header_widget.setCurrentIndex(0)

    def on_print_button_toggled(self):
        fullname, balance, past_bill, average_bill, kwh, next_due = self.bills_data()

        self.ui.header_widget.setCurrentIndex(1)
        self.ui.print_name.setText(fullname)
        self.ui.print_balance.setText(balance)
        self.ui.print_past_bill.setText(past_bill)
        self.ui.print_avgbill.setText(average_bill)
        self.ui.print_kwh.setText(kwh)
        self.ui.print_next_due.setText(next_due)

    def on_help_button_toggled(self):
        self.ui.header_widget.setCurrentIndex(2) 

    def on_aboutus_button_toggled(self):
        self.ui.header_widget.setCurrentIndex(3)  
        self.ui.label_7.setText("We love the earth! it is our planet!")


if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

