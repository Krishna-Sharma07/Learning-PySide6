from PySide6.QtWidgets import  QMainWindow, QPushButton

class ButtonHolder(QMainWindow):

    def __init__ (self):
        super().__init__()
        self.setWindowTitle("To do App")
        to_do = QPushButton("Add Task")
        self.setCentralWidget(to_do)
