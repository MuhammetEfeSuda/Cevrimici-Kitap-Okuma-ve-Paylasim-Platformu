# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris_yap.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 509)
        MainWindow.setStyleSheet("#centralwidget{background-color: rgb(0, 0, 0);}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -20, 861, 511))
        self.label_2.setStyleSheet("border-radius:20;\n"
"background-color: rgb(194, 6, 15);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 341, 491))
        self.label.setStyleSheet("border-radius:15;\n"
"background-color: rgb(59, 57, 54);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 30, 131, 121))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("1200px-Kültür_Üniversitesi_Logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_5.setStyleSheet("color:white")
        self.label_5.setIndent(-1)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 230, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_6.setStyleSheet("color:white")
        self.label_6.setIndent(-1)
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 270, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_7.setStyleSheet("color:white")
        self.label_7.setIndent(-1)
        self.label_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(475, 60, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_8.setFont(font)
        self.label_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_8.setStyleSheet("color:white")
        self.label_8.setIndent(-1)
        self.label_8.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_8.setObjectName("label_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(435, 130, 261, 41))
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_2.setMaxLength(25)
        self.lineEdit_2.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(435, 180, 261, 41))
        self.lineEdit_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"border: 2px solid black;\n"
"border-radius:8px;\n"
"padding:5px\n"
"}\n"
"\n"
"QLineEdit::focus{\n"
"border : 2px solid blue;\n"
"border-color: rgb(85, 0, 127)\n"
"\n"
"}")
        self.lineEdit_4.setMaxLength(25)
        self.lineEdit_4.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(455, 240, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("\n"
"QPushButton{\n"
"background-color: rgb(59, 57, 54);\n"
"color:white;\n"
"border-radius:10;}\n"
"QPushButton::hover{background-color: rgb(117, 117, 117);}\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 290, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"color:white;\n"
"    background-color: rgb(0, 170, 255);\n"
"border-radius:10;}\n"
"\n"
"\n"
"QPushButton::hover{background-color: rgb(117, 117, 117);}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 300, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_9.setStyleSheet("color:white")
        self.label_9.setIndent(-1)
        self.label_9.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Kültür Üniversitesi"))
        self.label_6.setText(_translate("MainWindow", "Çevrimiçi Kitap Okuma"))
        self.label_7.setText(_translate("MainWindow", "Ve"))
        self.label_8.setText(_translate("MainWindow", "Giriş Yap"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Kullanıcı Adınız"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Şifreniz"))
        self.pushButton_4.setText(_translate("MainWindow", "Giriş Yap"))
        self.pushButton_5.setText(_translate("MainWindow", "Kayıt Ol"))
        self.label_9.setText(_translate("MainWindow", "Paylaşım Platformu"))
import iku_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
