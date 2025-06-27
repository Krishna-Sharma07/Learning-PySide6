from PySide6.QtWidgets import QApplication, QWidget
import sys
from layout import Rocwidget

app = QApplication(sys.argv)
window = Rocwidget()
window.show()
app.exec()