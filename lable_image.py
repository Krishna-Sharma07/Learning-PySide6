from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap

class Lable_image(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLable Image")

        lable = QLabel()
        lable.setPixmap(QPixmap("z.png"))

        layout = QVBoxLayout()
        layout.addWidget(lable)

        self.setLayout(layout)