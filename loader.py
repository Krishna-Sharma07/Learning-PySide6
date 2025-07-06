import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

app = QtWidgets.QApplication(sys.argv)
window = loader.load("./Widget.ui")

def do_something():
    print(window.name.text(), "is a", window.occupation.text())

window.setWindowTitle("User Data")

window.submit.clicked.connect(do_something)
window.show()

app.exec()