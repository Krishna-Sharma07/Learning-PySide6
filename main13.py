from PySide6.QtWidgets import QApplication
import sys
from combo_box import Combo_box

app = QApplication(sys.argv)

window = Combo_box()
window.show()

app.exec()
