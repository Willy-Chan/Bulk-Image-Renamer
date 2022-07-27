from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_folder = QtWidgets.QPushButton(self.centralwidget)
        self.image_folder.setGeometry(QtCore.QRect(430, 430, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.image_folder.setFont(font)
        self.image_folder.setObjectName("image_folder")
        self.new_name = QtWidgets.QTextEdit(self.centralwidget)
        self.new_name.setGeometry(QtCore.QRect(410, 310, 431, 41))
        self.new_name.setObjectName("new_name")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(200, 310, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 360, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.delimiter = QtWidgets.QTextEdit(self.centralwidget)
        self.delimiter.setGeometry(QtCore.QRect(410, 360, 431, 41))
        self.delimiter.setObjectName("delimiter")
        self.run_program = QtWidgets.QPushButton(self.centralwidget)
        self.run_program.setGeometry(QtCore.QRect(440, 530, 181, 28))
        self.run_program.setObjectName("run_program")


        self.image = QtWidgets.QLabel(self.centralwidget)
        self.pixmap = QPixmap('image.jpg')
        self.image.setPixmap(self.pixmap)
        self.image.resize(self.pixmap.width(),          # Optional, resize label to image size
                          self.pixmap.height())
        self.image.setGeometry(QtCore.QRect(190, 80, 900, 141))
        self.image.setObjectName("image")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionbruh = QtWidgets.QAction(MainWindow)
        self.actionbruh.setObjectName("actionbruh")
        self.actionLocation = QtWidgets.QAction(MainWindow)
        self.actionLocation.setObjectName("actionLocation")
        self.file_path = QtWidgets.QLabel(self.centralwidget)
        self.file_path.setGeometry(QtCore.QRect(700, 410, 900, 99))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(6)
        self.file_path.setFont(font)
        self.file_path.setObjectName("file_path")


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bulk Image Renamer"))
        self.image_folder.setText(_translate("MainWindow", "Select Image Folder"))
        self.label_1.setText(_translate("MainWindow", "Rename every file to:"))
        self.label_2.setText(_translate("MainWindow", "Delimiter (optional):"))
        self.run_program.setText(_translate("MainWindow", "Rename every file!"))
        self.actionbruh.setText(_translate("MainWindow", "Time"))
        self.actionLocation.setText(_translate("MainWindow", "Location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
