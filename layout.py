from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class Rocwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout")
        button1 = QPushButton("Button1")
        button1.clicked.connect(self.b1_clicked)
        button2 = QPushButton("Button2")
        button2.clicked.connect(self.b2_clicked)
        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        self.setLayout(layout)
    
    def b1_clicked(self):
        print("B1 Clickes")

    def b2_clicked(self):
        print("B2 Clicked")