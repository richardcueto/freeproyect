# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(530, 433)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 160, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.abrir = QtWidgets.QPushButton(self.centralwidget)
        self.abrir.setGeometry(QtCore.QRect(210, 270, 75, 24))
        self.abrir.setObjectName("abrir")
        self.entrada = QtWidgets.QTextBrowser(self.centralwidget)
        self.entrada.setGeometry(QtCore.QRect(60, 210, 421, 41))
        self.entrada.setObjectName("entrada")
        self.guardar = QtWidgets.QPushButton(self.centralwidget)
        self.guardar.setGeometry(QtCore.QRect(210, 360, 75, 24))
        self.guardar.setObjectName("guardar")
        self.salida = QtWidgets.QTextBrowser(self.centralwidget)
        self.salida.setGeometry(QtCore.QRect(60, 310, 421, 41))
        self.salida.setObjectName("salida")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 191, 131))
        self.label_2.setStyleSheet("border-image: url(:/prefix/log.png);\n"
"border-image: url(:/prefix/logo.png);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 26))
        self.menubar.setObjectName("menubar")
        self.menuKML = QtWidgets.QMenu(self.menubar)
        self.menuKML.setObjectName("menuKML")
        self.menuOtros = QtWidgets.QMenu(self.menubar)
        self.menuOtros.setObjectName("menuOtros")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuKML.menuAction())
        self.menubar.addAction(self.menuOtros.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RichsApp"))
        self.label.setText(_translate("MainWindow", "Seleccionar KML:"))
        self.abrir.setText(_translate("MainWindow", "Abrir"))
        self.guardar.setText(_translate("MainWindow", "Guardar"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/prefix/logo.png\"/></p></body></html>"))
        self.menuKML.setTitle(_translate("MainWindow", "KML"))
        self.menuOtros.setTitle(_translate("MainWindow", "Otros"))
import logo_rc
