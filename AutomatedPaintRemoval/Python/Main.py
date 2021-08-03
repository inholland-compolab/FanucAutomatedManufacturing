import sys
from PySide2 import QtWidgets

import MainWindow as main_window

app = QtWidgets.QApplication(sys.argv)
window = main_window.MainWindow()
window.show()
app.exec_()
