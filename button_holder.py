from PySide6.QtWidgets import  QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def to_do_clicked():
        print("Task Added")

    def __init__ (self):
        super().__init__()
        self.setWindowTitle("To do App")
        to_do = QPushButton("Add Task")
        to_do.clicked.connect()
        self.setCentralWidget(to_do)
