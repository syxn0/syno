# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\syno\Final Main\windows\lugin_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 602)
        MainWindow.setMinimumSize(QtCore.QSize(720, 550))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
        MainWindow.setBaseSize(QtCore.QSize(720, 550))
        MainWindow.setStyleSheet("*{\n"
"    background: rgb(225, 225, 225);\n"
"}\n"
"#frame {\n"
"    width: 300px;\n"
"    background-color:rgb(203, 143, 75,0.77);\n"
"    border-bottom-right-radius: 35px;\n"
"    border-top-right-radius:35px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("background:none;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setStyleSheet("image: url(:/resources/energy-coffeepower.gif);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_9.addWidget(self.frame_4)
        self.label = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setToolTipDuration(0)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.frame_5, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame)
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setStyleSheet("#user,#password{\n"
"    border:1px solid black;\n"
"    border-radius:5px;\n"
"    margin-left: 25px;\n"
"    margin-right:25px;\n"
"    margin-top: 10px;\n"
"    \n"
"}\n"
"\n"
"#login{    \n"
"    margin-top:8px;\n"
"    margin-bottom:4px;\n"
"    padding:2px;\n"
"    border:1px solid black;\n"
"    border-radius:13px;\n"
"    background-color:rgb(203, 143, 75,0.9);\n"
"    color:black;\n"
"    \n"
"}\n"
"\n"
"#login:hover{\n"
"    background-color:rgb(203, 143, 75,0.5);\n"
"}\n"
"#login:pressed{\n"
"    margin-top:8px;\n"
"    margin-bottom:4px;\n"
"    padding:2px;\n"
"    background-color:rgb(203, 143, 75,0.1);\n"
"}\n"
"\n"
"#forgot{\n"
"    border:none;\n"
"}\n"
"#forgot:hover{\n"
"    color:rgb(0,170,255,0.7);\n"
"}\n"
"#create{\n"
"    border:none;\n"
"}\n"
"#create:hover{\n"
"    color:rgb(0,170,255,0.7);\n"
"}\n"
"\n"
"#frame_2{\n"
"    border: 2px solid black;\n"
"    border-radius: 25px;\n"
"    padding:10px;\n"
"}\n"
"#frame_3{\n"
"    background:none;\n"
"}")
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.frame2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(270, 270))
        self.frame_2.setMaximumSize(QtCore.QSize(617, 16777215))
        self.frame_2.setBaseSize(QtCore.QSize(204, 500))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.hello = QtWidgets.QLabel(self.frame_2)
        self.hello.setMinimumSize(QtCore.QSize(50, 21))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(17)
        font.setUnderline(False)
        self.hello.setFont(font)
        self.hello.setObjectName("hello")
        self.verticalLayout_7.addWidget(self.hello, 0, QtCore.Qt.AlignHCenter)
        self.user = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.user.setFont(font)
        self.user.setStyleSheet("")
        self.user.setObjectName("user")
        self.verticalLayout_7.addWidget(self.user)
        self.password = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.password.setFont(font)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout_7.addWidget(self.password)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.login = QtWidgets.QPushButton(self.frame_3)
        self.login.setGeometry(QtCore.QRect(28, 0, 81, 42))
        self.login.setMinimumSize(QtCore.QSize(50, 12))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.login.setFont(font)
        self.login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login.setIconSize(QtCore.QSize(23, 19))
        self.login.setObjectName("login")
        self.forgot = QtWidgets.QPushButton(self.frame_3)
        self.forgot.setGeometry(QtCore.QRect(120, -10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setUnderline(True)
        self.forgot.setFont(font)
        self.forgot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forgot.setStyleSheet("background:none;")
        self.forgot.setObjectName("forgot")
        self.verticalLayout_7.addWidget(self.frame_3, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_8.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Coffee Energy"))
        self.hello.setText(_translate("MainWindow", "User Login"))
        self.user.setPlaceholderText(_translate("MainWindow", "Username"))
        self.password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.forgot.setText(_translate("MainWindow", "Forgot password?"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
