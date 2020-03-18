# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        


if __name__ == "__main__":
    app = QApplication([])

    ui_file = QFile("PythonTest.ui")
    ui_file.open(QFile.ReadOnly)

    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    window.show()
    #window = MainWindow()
    #window.show()
    sys.exit(app.exec_())
