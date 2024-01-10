from windows.dashboard2_page import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MySideBar(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sidebar_menu2.setHidden(True)

        self.dashboard_button.clicked.connect(self.switch_to_dashboardPages)
        self.dashboard_icon.clicked.connect(self.switch_to_dashboardPages)

        self.print_button.clicked.connect(self.switch_to_printPages)
        self.print_icon.clicked.connect(self.switch_to_printPages)

        self.help_button.clicked.connect(self.switch_to_helpPages)
        self.help_icon.clicked.connect(self.switch_to_helpPages)

        self.aboutus_button.clicked.connect(self.switch_to_aboutusPages)
        self.aboutus_icon.clicked.connect(self.switch_to_aboutusPages)



    def switch_to_dashboardPages(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_printPages(self):
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_helpPages(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_aboutusPages(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_dashboardPages(self):
        self.stackedWidget.setCurrentIndex(0)

