from PySide6.QtWidgets import QApplication
import sys
from list import List

app = QApplication(sys.argv)

window = List()
window.show()

app.exec()