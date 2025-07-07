from PySide6.QtCore import QObject
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class Widget(QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("Widget.ui", None)
        self.ui.setWindowTitle("User Data")
        self.ui.submit.clicked.connect(self.do_something)

    def do_something(self):
        print(self.ui.name.text(), " is a ", self.ui.occupation.text())

    def Show(self):
        self.ui.show()