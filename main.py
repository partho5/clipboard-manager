# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Thu Jan  5 14:19:39 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def cancel(self):
        sys.exit()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 415)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 10, 151, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(50, 40, 591, 241))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 589, 239))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        connection=sqlite3.connect('clipData.db')
        query="CREATE TABLE IF NOT EXISTS 'copied_data' (ID INTEGER PRIMARY KEY AUTOINCREMENT, copied_text TEXT NOT NULL, copy_time TEXT NOT NULL, uploaded INTEGER NOT NULL)"
        connection.execute(query)
        connection.close()

        mygroupbox = QtGui.QGroupBox()
        myform = QtGui.QFormLayout()
        labellist = []
        text=" <html><body><p style=' background-color:#e1bee7;' >efhn euhf uifh niufh uifh uif huhruif <br>heruif hufh iur hreuihreiu hreui hreuighg"
        text+="oi jgrejg rejg ujrg urjg <br> urjg uirgjuiju ijf reijf rjf </p></body></html>"
        for i in range(3):
            labellist.append(QtGui.QLabel(text))
            myform.addRow(labellist[i])
        mygroupbox.setLayout(myform)
        self.scrollArea.setWidget(mygroupbox)

        self.cancelBtn = QtGui.QPushButton(self.centralwidget)
        self.cancelBtn.setGeometry(QtCore.QRect(280, 310, 98, 31))
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.cancelBtn.clicked.connect(self.cancel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color: #44aa88;font-weight:600; vertical-align:super;font:Times-New-Roman\">My ClipBoard</span></p></body></html>", None))
        self.cancelBtn.setText(_translate("MainWindow", "Close", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QMainWindow()
    Dialog.setWindowTitle("Clipboard Synchronizer")
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
