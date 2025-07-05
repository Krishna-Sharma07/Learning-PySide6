from PySide6.QtWidgets import QApplication
import sys
from tab import Tab

app = QApplication(sys.argv)

window = Tab()
window.show()

app.exec()
