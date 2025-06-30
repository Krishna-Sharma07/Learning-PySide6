from PySide6.QtWidgets import QApplication
from lable_and_line_edit import widget
import sys 

app = QApplication(sys.argv)

widget = widget()
widget.show()

app.exec()