from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

class Widget(QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User Data")
        self.submit.clicked.connect(self.do_something)

    def do_something(self):
        print(self.name.text(), " is a ", self.occupation.text())