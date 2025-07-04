from PySide6.QtWidgets import QWidget, QSizePolicy, QGridLayout, QPushButton

class Grid_layout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")

        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        button4 = QPushButton("Four")
        button5 = QPushButton("Five")
        button6 = QPushButton("Six")
        button7 = QPushButton("Seven")

        grid_layout = QGridLayout()
        grid_layout.addWidget(button1, 0, 0)
        grid_layout.addWidget(button2, 0, 1, 1, 2)
        grid_layout.addWidget(button3, 1, 0, 2, 1)
        grid_layout.addWidget(button4, 1, 1)
        grid_layout.addWidget(button5, 1, 2)
        grid_layout.addWidget(button6, 2, 1)
        grid_layout.addWidget(button7, 2, 2)

        self.setLayout(grid_layout)