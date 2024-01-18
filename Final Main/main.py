import sys, sqlite3, calendar
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QPushButton, QTableWidgetItem, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from windows.login_page import Ui_MainWindow as Login
from windows.dashboard2_page import Ui_MainWindow as Dashboard
from windows.admin_dashboard_page import Ui_MainWindow as AdminDashboard
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure
from datetime import datetime, timedelta
from random import randint


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.db_conn = sqlite3.connect("data.db")
        self.sql = self.db_conn.cursor()
        self.sql.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, password TEXT NOT NULL, fullname TEXT NOT NULL, balance TEXT NOT NULL, past_bill TEXT NOT NULL, average_bill TEXT NOT NULL, kwh TEXT NOT NULL, next_due TEXT NOT NULL, user_type INTEGER NOT NULL)")
        self.db_conn.commit()
        self.create_billing_history_table()
        self.session_type = 0
        self.session_uid = 0
        self.session_user_type = 0
        self.cost_per_kwh = 5 # 5 usd per kwh, 5 * kwh = their billing cost
        self.session()


    def create_billing_history_table(self):
        self.sql.execute("""
            CREATE TABLE IF NOT EXISTS billing_history (
                billing_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                billing_date TEXT NOT NULL,
                amount_billed TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        self.db_conn.commit()

    def __update_Bill(self, new_balance, new_bill_date, uid):
        next_due = self.next_billing_date(new_bill_date)
        self.sql.execute("UPDATE users SET balance = ?, past_bill_date = ?, next_due = ? WHERE id = ?", (new_balance, new_bill_date, next_due, uid))
        self.db_conn.commit()
    
    def __update_bill_history(self, uid, billing_date, billed_amount):
        self.sql.execute("INSERT INTO billing_history(user_id, billing_date, amount_billed) VALUES(?,?,?)",(uid, billing_date, billed_amount))
        self.db_conn.commit()
    
    def __cut_kwh(self, uid):
        self.sql.execute("UPDATE users SET kwh = 0 WHERE id= ?",(uid,))

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
    
    def __usernameExist(self, username):
        self.sql.execute("SELECT * FROM users WHERE username = ?;",(str(username),))
        if(len(self.sql.fetchall()) > 0):
            return True
        return False

    def __get_users_data(self, uid):
        if(str(uid) == "*"):
            self.sql.execute("SELECT * FROM users ORDER BY id ASC;")
        else:
            self.sql.execute("SELECT * FROM users WHERE id = ?;",(str(uid),))
        results = self.sql.fetchall()
        return results
    
    def __del_user_data(self, uid):
        self.sql.execute("DELETE FROM users WHERE id = ?;",(str(uid),))
        self.db_conn.commit()

    def __add_user_data(self, fullname: str, username: str, password: str):
        current_date = datetime.now().strftime("%Y-%m-%d")
        initial_balance = 10000
        random_kwh = randint(800,1000)
        next_bill = self.next_billing_date(current_date)
        self.sql.execute("INSERT INTO users(username, password, fullname, balance, past_bill_date, average_bill, kwh, next_due, user_type) VALUES(?,?,?,?,?,?,?,?,?)", (username, password, fullname, initial_balance, current_date,"0",random_kwh,next_bill, 1))
        self.db_conn.commit()
    
    def __get_past_bill(self, uid):
        self.sql.execute("SELECT * FROM billing_history WHERE user_id = ? ORDER BY billing_id DESC", (uid,))
        results = self.sql.fetchall()
        return results

    def __handle_setup(self):
        self.ui.setupUi(self)
        if(self.session_type == 1):
            if(self.session_user_type == 0):
                self.__admin_init()
            elif(self.session_user_type == 1):
                self.__user_init()
    
    def parseDate(self, date):
        return datetime.strptime(date, "%Y-%m-%d")
    
    def next_billing_date(self, user_date):
        date = datetime.strptime(user_date, "%Y-%m-%d")
        return (date + timedelta(days=30)).strftime("%Y-%m-%d")

    def show_message(self, title, text, icon_type):
        msg = QMessageBox()
        msg.setIcon(icon_type)
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon('icon.png'))
        msg.setText(text)
        msg.exec_()

    def session(self):
        """
        # Session type: 0 = Login 
        # Session type: 1 = Dashboard
        # Session User type: 0 = Administrator
        # Session User type: 1 = Normal User
        """
        if(self.session_type == 0):
            self.ui = Login()
        elif(self.session_type == 1):
            if(self.session_user_type == 0):
                self.ui = AdminDashboard()
            else:
                self.ui = Dashboard()
 
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
    
    def auto_bill(self):
        data = self.__get_users_data(self.session_uid)[0]
        uid = self.session_uid
        kwh = data[7]
        balance = data[4]
        next_due = data[-2]
        current_date = datetime.now().strftime("%Y-%m-%d")

        new_bill = (self.cost_per_kwh * int(kwh))
        new_balance = int(balance) - int(new_bill)
        if(new_balance < new_bill):
            self.__cut_kwh(uid)

        elif(datetime.strptime(current_date, "%Y-%m-%d") >= datetime.strptime(next_due, "%Y-%m-%d")):
            self.__update_Bill(new_balance, current_date, uid)
            self.__update_bill_history(uid, current_date, new_bill)

    """
    Below are the:
    -- ADMIN Dashboard Functions
    """
    def __admin_init(self):
        # Initialize the users table data on login.
        self.admin_refresh_table()

    def admin_refresh_table(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        data = self.__get_users_data("*")

        for row_data in data:
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)

            for col, value in enumerate(row_data):
                if(col == 9):
                    user_id = row_data[0]
                    button = self.button_parse('Delete', 'tbl_delete_btn', user_id)
                    self.ui.tableWidget.setCellWidget(rowPosition, col, button)
                else:
                    item = QTableWidgetItem(str(value))
                    self.ui.tableWidget.setItem(rowPosition, col, item)
    
    def button_parse(self, btn_name, obj_name, user_id):
        button = QPushButton(btn_name)
        button.setObjectName(obj_name)
        button.clicked.connect(lambda _, uid=user_id: self.tbl_row_delete(uid))
        button.setStyleSheet("""
        #tbl_delete_btn{
            margin:2px;
            font-size:14px;
            border: 1px dotted black;
            border-radius:10px!important;
            background:rgb(208, 0, 0,0.5);
        }
        #tbl_delete_btn:hover{
            background:rgb(208, 0, 0,0.3);
            border: 1px solid black;
        }
        """)
        return button

    def tbl_row_delete(self, row_id):
        username = self.__get_users_data(row_id)[0][1]
        confirm_delete = QMessageBox.question(self, 'Delete row', f'Delete user {username}?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if(confirm_delete == QMessageBox.Yes):
            self.__del_user_data(row_id)
            self.admin_refresh_table()
            # print(f"[{row_id}] DELETD!!")

    def on_add_btn_pressed(self):
        def parse(data):return data.text().strip()
        fullname = self.ui.fullname
        username = self.ui.user_name_input
        password = self.ui.new_password
        if(parse(fullname) == '' or parse(username) == '' or parse(password) == ''):
            self.show_message("ERROR", f"All fields must be filled!", QMessageBox.Warning)
            return
        elif(len(parse(username)) != len(parse(username).replace(' ',''))):
            self.show_message("ERROR", f"Username must not have spaces!", QMessageBox.Warning)
            return
        elif(self.__usernameExist(parse(username))):
            self.show_message("ERROR", f"Username {parse(username)} already exists!\nPlease choose another username", QMessageBox.Warning)
            return

        self.__add_user_data(parse(fullname), parse(username), parse(password))
        self.show_message("INFO", f"Success! Added new user {parse(username)}", QMessageBox.Information)
        self.admin_refresh_table()
        fullname.setText("")
        username.setText("")
        password.setText("")

    """
    Below are the:
    -- USER Dashboard Functions
    """
    def __user_init(self):
        self.auto_bill()
        fullname, balance, past_bill, average_bill, kwh, next_due = self.bills_data()
        past_bill = self.__get_past_bill(self.session_uid)[0][-1]

        self.ui.sidebar_menu2.setHidden(True)
        self.ui.balance_obj.setText(f"${balance}")
        self.ui.pastbill_obj.setText(f"${past_bill}")
        self.ui.avgbill_obj.setText(f"${average_bill}")
        self.generate_line_graph()


    def generate_line_graph(self):

        self.sql.execute("SELECT * FROM billing_history WHERE user_id = ?;", (self.session_uid,))
        billing_data = self.sql.fetchall()

        billing_dates = [entry[2] for entry in billing_data]
        billing_amounts = [float(entry[3]) for entry in billing_data]

        billing_month_names = [calendar.month_name[int(date.split('-')[1])] for date in billing_dates]

        fig = Figure(figsize=(10.1, 4.5), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(billing_month_names, billing_amounts, marker='o', label='Billing History')

        ax.set_xlabel('Billing Months')
        ax.set_ylabel('Billing Amount')
        ax.set_title('Billing History Line Graph')
        ax.legend()

        canvas = FigureCanvas(fig)
        canvas.setParent(self.ui.graph)
        canvas.draw()

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
    
    def on_print_bill_pressed(self):
        fullname, balance, past_bill, average_bill, kwh, next_due = self.bills_data()
        past_bill = self.__get_past_bill(self.session_uid)[0][-1]
        next_due = self.parseDate(next_due).strftime("%B, %d %Y")

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
        past_bill = self.__get_past_bill(self.session_uid)[0][-1]
        next_due = self.parseDate(next_due).strftime("%B, %d %Y")

        self.ui.header_widget.setCurrentIndex(1)
        self.ui.print_name.setText(fullname)
        self.ui.print_balance.setText(balance)
        self.ui.print_past_bill.setText(past_bill)
        self.ui.print_avgbill.setText(average_bill)
        self.ui.print_kwh.setText(kwh)
        self.ui.print_next_due.setText(next_due)

    def on_aboutus_button_toggled(self):
        self.ui.header_widget.setCurrentIndex(2)


if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

