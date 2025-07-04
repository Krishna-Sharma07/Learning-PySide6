from PySide6.QtWidgets import QApplication
import sys
from checkbox_and_radios import Window

app = QApplication()

window = Window()
window.show()

app.exec()