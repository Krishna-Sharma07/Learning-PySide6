from PySide6.QtWidgets import QApplication
import sys
from text_edit import text_edit

app = QApplication(sys.argv)

window = text_edit()
window.show()

app.exec()