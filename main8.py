from PySide6.QtWidgets import QApplication
import sys
from size_policies import Size_policies

app = QApplication()

window = Size_policies()
window.show()

app.exec()