from PySide6.QtWidgets import QApplication
import sys
from list import List

app = QApplication()

window = List()
window.show()

app.exec()