from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    # define the main window
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 200, 200)
    win.setWindowTitle("Test PyQt5")
    label = QtWidgets.QLabel(win)
    label.setText("my first label")
    label.move(50, 50)
    win.show()
    sys.exit(app.exec_())


window()
