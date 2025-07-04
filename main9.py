from PySide6.QtWidgets import QApplication
import sys
from grid_layout import Grid_layout

app = QApplication()

window = Grid_layout()
window.show()

app.exec()