# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from assembler import Assembler
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1153, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.browsButton = QtWidgets.QPushButton(self.centralwidget)
        self.browsButton.setGeometry(QtCore.QRect(360, 10, 51, 31))
        self.browsButton.setObjectName("browsButton")
        self.duration = QtWidgets.QSpinBox(self.centralwidget)
        self.duration.setGeometry(QtCore.QRect(180, 590, 81, 31))
        self.duration.setMinimum(1)
        self.duration.setMaximum(1000)
        self.duration.setProperty("value", 100)
        self.duration.setObjectName("duration")
        self.assemblyEditor = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.assemblyEditor.setGeometry(QtCore.QRect(30, 50, 380, 490))
        self.assemblyEditor.setAcceptDrops(False)
        self.assemblyEditor.setObjectName("assemblyEditor")
        self.assembleButton = QtWidgets.QPushButton(self.centralwidget)
        self.assembleButton.setGeometry(QtCore.QRect(490, 280, 151, 61))
        self.assembleButton.setObjectName("assembleButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(830, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.simulate = QtWidgets.QPushButton(self.centralwidget)
        self.simulate.setGeometry(QtCore.QRect(40, 590, 93, 28))
        self.simulate.setObjectName("simulate")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 560, 71, 16))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(740, 50, 380, 490))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
################################################################################################
#User code
        self.browsButton.clicked.connect(self.browsClicked)
        self.assembleButton.clicked.connect(self.assembleClicked)
        self.simulate.clicked.connect(self.simulateClicked)

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Assembly"))
        self.browsButton.setText(_translate("MainWindow", "Brows"))
        self.assembleButton.setText(_translate("MainWindow", "Assemble >>"))
        self.label_2.setText(_translate("MainWindow", "MachineCode"))
        self.simulate.setText(_translate("MainWindow", "Simulate"))
        self.label_3.setText(_translate("MainWindow", "Duration Us"))

################################################################################################
#User code
    def assembleClicked(self):
        with open("assembly.asm", 'w') as asmFile:
            asmFile.write(self.assemblyEditor.toPlainText())
        Assembler("assembly.asm", "binaryCode.txt")

        with open ("binaryCode.txt", 'r') as binaryFile:
            self.textBrowser.setPlainText(binaryFile.read())

    def browsClicked(self):
        text = ""
        name, _ = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open File')
        with open(name, 'r') as file:
            text = file.read()
        self.assemblyEditor.setPlainText(text)

    def simulateClicked(self):
        QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
        duration = self.duration.value()

        projectPath = 'D:/Education/University/3rdCSE/CO/Projects/MIPS/Mips/MipsProcessor.mpf'
        library = 'work'
        moduleName = 'FullAdderTest'

        simulateCommand = 'vsim -do "project open {project}; vsim {library}.{module}; run {duration}; quit -f" -c'.format(
            project=projectPath, library=library, module=moduleName, duration=duration)
        os.system(simulateCommand)
        
        QtWidgets.QApplication.restoreOverrideCursor()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
