# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\User\syno\Final Main\windows\admin_dashboard_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
        MainWindow.setStyleSheet("background: rgb(225, 225, 225);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background: rgb(225, 225, 225);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 46))
        self.frame_2.setStyleSheet("background: rgb(208, 162, 110);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background: rgb(208, 162, 110);\n"
"")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setPixmap(QtGui.QPixmap(":/resources/account.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;\n"
"background: rgb(208, 162, 110);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 591))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 653))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background: rgb(208, 162, 110);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMinimumSize(QtCore.QSize(13, 0))
        self.frame_5.setStyleSheet("background: rgb(208, 162, 110);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_5)
        self.tableWidget.setMaximumSize(QtCore.QSize(111111, 16777215))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background:rgb(225, 225, 225);\n"
"border-radius: 30px;")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAutoScrollMargin(17)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setIconSize(QtCore.QSize(0, 0))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(114)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.horizontalLayout_2.addWidget(self.tableWidget)
        self.frame_7 = QtWidgets.QFrame(self.frame_5)
        self.frame_7.setMinimumSize(QtCore.QSize(345, 0))
        self.frame_7.setMaximumSize(QtCore.QSize(308, 16777215))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.frame_7)
        self.frame_6.setMinimumSize(QtCore.QSize(221, 0))
        self.frame_6.setStyleSheet("background:rgb(225, 225, 225);\n"
"border-radius: 30px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.formLayout = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setMinimumSize(QtCore.QSize(100, 22))
        self.label_2.setMaximumSize(QtCore.QSize(81, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.fullname = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.fullname.setFont(font)
        self.fullname.setStyleSheet("border:1px solid black;\n"
"border-radius: 10px;")
        self.fullname.setText("")
        self.fullname.setMaxLength(32)
        self.fullname.setObjectName("fullname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fullname)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setMinimumSize(QtCore.QSize(105, 22))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.user_name_input = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.user_name_input.setFont(font)
        self.user_name_input.setStyleSheet("border:1px solid black;\n"
"border-radius: 10px;")
        self.user_name_input.setMaxLength(32)
        self.user_name_input.setObjectName("user_name_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.user_name_input)
        self.new_password = QtWidgets.QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_password.setFont(font)
        self.new_password.setStyleSheet("border:1px solid black;\n"
"border-radius: 10px;")
        self.new_password.setText("")
        self.new_password.setMaxLength(32)
        self.new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password.setObjectName("new_password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.new_password)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setMinimumSize(QtCore.QSize(100, 22))
        self.label_4.setMaximumSize(QtCore.QSize(94, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.add_btn = QtWidgets.QPushButton(self.frame_6)
        self.add_btn.setMinimumSize(QtCore.QSize(85, 29))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.add_btn.setFont(font)
        self.add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_btn.setStyleSheet("#add_btn{\n"
"    border:1px solid black;\n"
"    border-radius: 10px;\n"
"    background:rgb(208, 162, 110);\n"
"}\n"
"#add_btn:hover{\n"
"    background:rgb(208, 162, 110,0.7);\n"
"}\n"
"#add_btn:pressed{\n"
"    background:rgb(208, 162, 110,0.1);\n"
"    \n"
"}\n"
"")
        self.add_btn.setObjectName("add_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.add_btn)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Admin Dashboard"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fullname"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Balance"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Past Bill"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Average Bill"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "kWh"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Next Due"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Actions"))
        self.label_2.setText(_translate("MainWindow", "Fullname :"))
        self.fullname.setPlaceholderText(_translate("MainWindow", "Christine Dagcuta"))
        self.label_3.setText(_translate("MainWindow", "Username :"))
        self.user_name_input.setPlaceholderText(_translate("MainWindow", "christine143"))
        self.new_password.setPlaceholderText(_translate("MainWindow", "New Password"))
        self.label_4.setText(_translate("MainWindow", "Password :"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
