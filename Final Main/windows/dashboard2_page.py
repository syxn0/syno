# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\syno\Final Main\windows\dashboard2_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.sidebar_menu2 = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.sidebar_menu = QtWidgets.QWidget(self.centralwidget)
        self.sidebar_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.sidebar_menu.setStyleSheet("QWidget{\n"
"background-color:rgb(203, 143, 75,0.77);\n"
"}\n"
"QPushButton{\n"
"    color:white;\n"
"    text-align:center;\n"
"    height:40px;\n"
"    border:none;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    color:black;\n"
"    font-weight:bold;\n"
"}")
        self.sidebar_menu.setObjectName("sidebar_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.sidebar_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.profile_icon = QtWidgets.QHBoxLayout()
        self.profile_icon.setObjectName("profile_icon")
        self.prof = QtWidgets.QLabel(self.sidebar_menu)
        self.prof.setMinimumSize(QtCore.QSize(40, 40))
        self.prof.setMaximumSize(QtCore.QSize(40, 40))
        self.prof.setStyleSheet("background:none;")
        self.prof.setText("")
        self.prof.setPixmap(QtGui.QPixmap(":/resources/account.png"))
        self.prof.setScaledContents(True)
        self.prof.setObjectName("prof")
        self.profile_icon.addWidget(self.prof)
        self.verticalLayout_3.addLayout(self.profile_icon)
        self.sidebutton = QtWidgets.QVBoxLayout()
        self.sidebutton.setContentsMargins(-1, 15, -1, -1)
        self.sidebutton.setSpacing(15)
        self.sidebutton.setObjectName("sidebutton")
        self.dashboard_icon = QtWidgets.QPushButton(self.sidebar_menu)
        self.dashboard_icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboard_icon.setIcon(icon)
        self.dashboard_icon.setIconSize(QtCore.QSize(35, 40))
        self.dashboard_icon.setCheckable(True)
        self.dashboard_icon.setAutoExclusive(True)
        self.dashboard_icon.setObjectName("dashboard_icon")
        self.sidebutton.addWidget(self.dashboard_icon)
        self.print_icon = QtWidgets.QPushButton(self.sidebar_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.print_icon.sizePolicy().hasHeightForWidth())
        self.print_icon.setSizePolicy(sizePolicy)
        self.print_icon.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.print_icon.setIcon(icon1)
        self.print_icon.setIconSize(QtCore.QSize(25, 30))
        self.print_icon.setCheckable(True)
        self.print_icon.setAutoExclusive(True)
        self.print_icon.setObjectName("print_icon")
        self.sidebutton.addWidget(self.print_icon)
        self.help_icon = QtWidgets.QPushButton(self.sidebar_menu)
        self.help_icon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.help_icon.setIcon(icon2)
        self.help_icon.setIconSize(QtCore.QSize(28, 35))
        self.help_icon.setCheckable(True)
        self.help_icon.setAutoExclusive(True)
        self.help_icon.setObjectName("help_icon")
        self.sidebutton.addWidget(self.help_icon)
        self.verticalLayout_3.addLayout(self.sidebutton)
        spacerItem = QtWidgets.QSpacerItem(20, 387, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.logout_icon = QtWidgets.QPushButton(self.sidebar_menu)
        self.logout_icon.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout_icon.setIcon(icon3)
        self.logout_icon.setIconSize(QtCore.QSize(31, 35))
        self.logout_icon.setCheckable(True)
        self.logout_icon.setAutoExclusive(True)
        self.logout_icon.setObjectName("logout_icon")
        self.verticalLayout_3.addWidget(self.logout_icon)
        self.aboutus_icon = QtWidgets.QPushButton(self.sidebar_menu)
        self.aboutus_icon.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resources/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.aboutus_icon.setIcon(icon4)
        self.aboutus_icon.setIconSize(QtCore.QSize(25, 35))
        self.aboutus_icon.setCheckable(True)
        self.aboutus_icon.setAutoExclusive(True)
        self.aboutus_icon.setObjectName("aboutus_icon")
        self.verticalLayout_3.addWidget(self.aboutus_icon)
        self.gridLayout.addWidget(self.sidebar_menu, 0, 0, 1, 1)
        self.sidebar_menu2 = QtWidgets.QWidget(self.centralwidget)
        self.sidebar_menu2.setStyleSheet("QWidget{\n"
"    background-color:rgb(203, 143, 75,0.77);\n"
"    color:white;\n"
"}\n"
"QPushButton{\n"
"    color:white;\n"
"    text-align:left;\n"
"    height:40px;\n"
"    border:none;\n"
"    padding-left:10px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    color:black;\n"
"    font-weight:bold;\n"
"}\n"
"    \n"
"")
        self.sidebar_menu2.setObjectName("sidebar_menu2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sidebar_menu2)
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.sidebar_menu2)
        self.label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.label_2.setStyleSheet("background:none;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/resources/account.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.sidebar_menu2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background:none;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.sidebar_buttons = QtWidgets.QVBoxLayout()
        self.sidebar_buttons.setContentsMargins(-1, 15, -1, -1)
        self.sidebar_buttons.setSpacing(15)
        self.sidebar_buttons.setObjectName("sidebar_buttons")
        self.dashboard_button = QtWidgets.QPushButton(self.sidebar_menu2)
        self.dashboard_button.setMinimumSize(QtCore.QSize(10, 0))
        self.dashboard_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.dashboard_button.setIcon(icon)
        self.dashboard_button.setIconSize(QtCore.QSize(66, 38))
        self.dashboard_button.setCheckable(True)
        self.dashboard_button.setAutoExclusive(True)
        self.dashboard_button.setObjectName("dashboard_button")
        self.sidebar_buttons.addWidget(self.dashboard_button)
        self.print_button = QtWidgets.QPushButton(self.sidebar_menu2)
        self.print_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.print_button.setIcon(icon1)
        self.print_button.setIconSize(QtCore.QSize(40, 35))
        self.print_button.setCheckable(True)
        self.print_button.setAutoExclusive(True)
        self.print_button.setObjectName("print_button")
        self.sidebar_buttons.addWidget(self.print_button)
        self.help_button = QtWidgets.QPushButton(self.sidebar_menu2)
        self.help_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.help_button.setIcon(icon2)
        self.help_button.setIconSize(QtCore.QSize(40, 35))
        self.help_button.setCheckable(True)
        self.help_button.setAutoExclusive(True)
        self.help_button.setObjectName("help_button")
        self.sidebar_buttons.addWidget(self.help_button)
        self.verticalLayout_4.addLayout(self.sidebar_buttons)
        spacerItem1 = QtWidgets.QSpacerItem(20, 387, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.logout_button = QtWidgets.QPushButton(self.sidebar_menu2)
        self.logout_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.logout_button.setIcon(icon3)
        self.logout_button.setIconSize(QtCore.QSize(40, 35))
        self.logout_button.setCheckable(True)
        self.logout_button.setAutoExclusive(True)
        self.logout_button.setObjectName("logout_button")
        self.verticalLayout_4.addWidget(self.logout_button)
        self.aboutus_button = QtWidgets.QPushButton(self.sidebar_menu2)
        self.aboutus_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.aboutus_button.setIcon(icon4)
        self.aboutus_button.setIconSize(QtCore.QSize(40, 35))
        self.aboutus_button.setCheckable(True)
        self.aboutus_button.setAutoExclusive(True)
        self.aboutus_button.setObjectName("aboutus_button")
        self.verticalLayout_4.addWidget(self.aboutus_button)
        self.gridLayout.addWidget(self.sidebar_menu2, 0, 1, 1, 1)
        self.main_menu = QtWidgets.QWidget(self.centralwidget)
        self.main_menu.setObjectName("main_menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_menu)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header = QtWidgets.QWidget(self.main_menu)
        self.header.setObjectName("header")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_11 = QtWidgets.QPushButton(self.header)
        self.pushButton_11.setStyleSheet("border:none;")
        self.pushButton_11.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/resources/horizontal-bars.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon5)
        self.pushButton_11.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_4.addWidget(self.pushButton_11)
        spacerItem2 = QtWidgets.QSpacerItem(371, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(370, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton_13 = QtWidgets.QPushButton(self.header)
        self.pushButton_13.setStyleSheet("border:none;")
        self.pushButton_13.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/resources/account.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_13.setIcon(icon6)
        self.pushButton_13.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_4.addWidget(self.pushButton_13)
        self.verticalLayout_5.addWidget(self.header)
        self.header_widget = QtWidgets.QStackedWidget(self.main_menu)
        self.header_widget.setStyleSheet("#bill{\n"
"    border:1px solid black;\n"
"    background: rgb(234, 236, 204);\n"
"}\n"
"#pastbill{\n"
"    border:1px solid black;\n"
"    background:rgb(219, 204, 149);\n"
"}\n"
"#averagebill{\n"
"    border:1px solid black;\n"
"    background: #CD8D7A;\n"
"}\n"
"#dashboard{\n"
"background-color: rgb(207, 207, 207);\n"
"}")
        self.header_widget.setObjectName("header_widget")
        self.dashboard = QtWidgets.QWidget()
        self.dashboard.setObjectName("dashboard")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dashboard)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.dashboard)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bill = QtWidgets.QFrame(self.frame)
        self.bill.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bill.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bill.setObjectName("bill")
        self.horizontalLayout_3.addWidget(self.bill)
        self.pastbill = QtWidgets.QFrame(self.frame)
        self.pastbill.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pastbill.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pastbill.setObjectName("pastbill")
        self.horizontalLayout_3.addWidget(self.pastbill)
        self.averagebill = QtWidgets.QFrame(self.frame)
        self.averagebill.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.averagebill.setFrameShadow(QtWidgets.QFrame.Raised)
        self.averagebill.setObjectName("averagebill")
        self.horizontalLayout_3.addWidget(self.averagebill)
        self.verticalLayout.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(self.dashboard)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setStyleSheet("border:1px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setMinimumSize(QtCore.QSize(264, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_3.setStyleSheet("border:1px solid black;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.header_widget.addWidget(self.dashboard)
        self.print = QtWidgets.QWidget()
        self.print.setObjectName("print")
        self.label_5 = QtWidgets.QLabel(self.print)
        self.label_5.setGeometry(QtCore.QRect(390, 240, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.header_widget.addWidget(self.print)
        self.help = QtWidgets.QWidget()
        self.help.setObjectName("help")
        self.label_6 = QtWidgets.QLabel(self.help)
        self.label_6.setGeometry(QtCore.QRect(410, 270, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.header_widget.addWidget(self.help)
        self.aboutus = QtWidgets.QWidget()
        self.aboutus.setObjectName("aboutus")
        self.label_7 = QtWidgets.QLabel(self.aboutus)
        self.label_7.setGeometry(QtCore.QRect(390, 370, 201, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.header_widget.addWidget(self.aboutus)
        self.verticalLayout_5.addWidget(self.header_widget)
        self.gridLayout.addWidget(self.main_menu, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.header_widget.setCurrentIndex(0)
        self.pushButton_11.toggled['bool'].connect(self.sidebar_menu.setHidden) # type: ignore
        self.pushButton_11.toggled['bool'].connect(self.sidebar_menu2.setVisible) # type: ignore
        self.dashboard_icon.toggled['bool'].connect(self.dashboard_button.setChecked) # type: ignore
        self.dashboard_button.toggled['bool'].connect(self.dashboard_icon.setChecked) # type: ignore
        self.print_button.toggled['bool'].connect(self.print_icon.setChecked) # type: ignore
        self.print_icon.toggled['bool'].connect(self.print_button.setChecked) # type: ignore
        self.help_button.toggled['bool'].connect(self.help_icon.setChecked) # type: ignore
        self.help_icon.toggled['bool'].connect(self.help_button.setChecked) # type: ignore
        self.aboutus_button.toggled['bool'].connect(self.aboutus_icon.setChecked) # type: ignore
        self.aboutus_icon.toggled['bool'].connect(self.aboutus_button.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Profile"))
        self.dashboard_button.setText(_translate("MainWindow", "Dashboard"))
        self.print_button.setText(_translate("MainWindow", "Print Bill"))
        self.help_button.setText(_translate("MainWindow", "Help"))
        self.logout_button.setText(_translate("MainWindow", "Logout"))
        self.aboutus_button.setText(_translate("MainWindow", "About Us"))
        self.label_5.setText(_translate("MainWindow", "Print"))
        self.label_6.setText(_translate("MainWindow", "Help"))
        self.label_7.setText(_translate("MainWindow", "About Us"))
import windows.resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
