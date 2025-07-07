import sys
from PySide6.QtWidgets import QApplication
from loader2 import Widget

app = QApplication(sys.argv)

window = Widget()
window.Show()

app.exec()