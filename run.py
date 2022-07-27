import os
import sys
from frame import Ui_MainWindow
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QFileDialog

class MainWindow(qtw.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.run_program.clicked.connect(self.rename)
        self.ui.image_folder.clicked.connect(self.open_folder)


    def rename(self):
        new_name = self.ui.new_name.toPlainText()
        delimiter = self.ui.delimiter.toPlainText()
        path = self.path

        i = 0
        for file in os.listdir(path):
            format = os.path.splitext(file)[1]
            source = path + '/' + file
            name = new_name + delimiter + str(i) + format
            os.rename(source, path + '/' + name)
            i += 1

        qtw.QMessageBox.information(self, "QMessageBox.information()", "Success, every file has been renamed to " + new_name + '.')

    def open_folder(self):
        self.path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.file_path.setText(self.path)




if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())