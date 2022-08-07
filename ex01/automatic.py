# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automaticProgram.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 140, 77, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 170, 77, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 210, 77, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 250, 121, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 110, 77, 18))
        self.label_5.setObjectName("label_5")
        self.textEdit_Context = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Context.setGeometry(QtCore.QRect(110, 340, 411, 391))
        self.textEdit_Context.setObjectName("textEdit_Context")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 20, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_Id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Id.setGeometry(QtCore.QRect(240, 130, 113, 25))
        self.lineEdit_Id.setObjectName("lineEdit_Id")
        self.lineEdit_Pw = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Pw.setGeometry(QtCore.QRect(240, 170, 113, 25))
        self.lineEdit_Pw.setObjectName("lineEdit_Pw")
        self.lineEdit_Search = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Search.setGeometry(QtCore.QRect(240, 210, 113, 25))
        self.lineEdit_Search.setObjectName("lineEdit_Search")
        self.lineEdit_Url1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Url1.setGeometry(QtCore.QRect(250, 250, 113, 25))
        self.lineEdit_Url1.setObjectName("lineEdit_Url1")
        self.lineEdit_Url2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Url2.setGeometry(QtCore.QRect(410, 250, 113, 25))
        self.lineEdit_Url2.setObjectName("lineEdit_Url2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 250, 21, 18))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(110, 310, 77, 18))
        self.label_8.setObjectName("label_8")
        self.textEdit_Status = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Status.setGeometry(QtCore.QRect(590, 140, 401, 461))
        self.textEdit_Status.setObjectName("textEdit_Status")
        self.pushButton_Start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Start.setGeometry(QtCore.QRect(590, 610, 181, 121))
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.pushButton_Stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Stop.setGeometry(QtCore.QRect(810, 610, 181, 121))
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # self.pushButton_Start.clicked.connect(MainWindow.start)
        # self.pushButton_Stop.clicked.connect(MainWindow.start)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "아이디"))
        self.label_2.setText(_translate("MainWindow", "비밀번호"))
        self.label_3.setText(_translate("MainWindow", "검색어"))
        self.label_4.setText(_translate("MainWindow", "url 수집페이지"))
        self.label_5.setText(_translate("MainWindow", "상태창"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#005500;\">업무 자동화 도우미</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "-"))
        self.label_8.setText(_translate("MainWindow", "작성내용"))
        self.pushButton_Start.setText(_translate("MainWindow", "시작"))
        self.pushButton_Stop.setText(_translate("MainWindow", "중지"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

