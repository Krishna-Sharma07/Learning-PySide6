from PySide6.QtWidgets import QApplication
import sys
from lable_image import Lable_image

app = QApplication(sys.argv)

window = Lable_image()
window.show()

app.exec()