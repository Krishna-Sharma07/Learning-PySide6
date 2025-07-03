from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy

class Size_policies(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Size Policies")

        lable = QLabel("Some text: ")
        line_edit = QLineEdit()

        line_edit.setSizePolicy(QSizePolicy.Policy.Expanding , QSizePolicy.Policy.Expanding )

        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(lable)
        hlayout1.addWidget(line_edit)

        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")

        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(button1, 2)
        hlayout2.addWidget(button2, 1)
        hlayout2.addWidget(button3, 1)

        vlayout = QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        self.setLayout(vlayout)
        