from PySide6.QtWidgets import QApplication
from status_bar import mainwindow
import sys

app = QApplication(sys.argv)

window = mainwindow(app)
window.show()

app.exec()