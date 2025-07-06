from PySide6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QPushButton

class Combo_box(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combo Box")

        self.combo_box = QComboBox(self)

        self.combo_box.addItem("Earth")
        self.combo_box.addItems(["Mercury", "Venus", "Mars", "Jupiter"])

        current = QPushButton("Current Value")
        current.clicked.connect(self.current_value)

        set = QPushButton("Set Value")
        set.clicked.connect(self.set_value)

        get = QPushButton("Get Value")
        get.clicked.connect(self.get_value)

        layout = QVBoxLayout()
        layout.addWidget(self.combo_box)
        layout.addWidget(current)
        layout.addWidget(set)
        layout.addWidget(get)

        self.setLayout(layout)

    def current_value(self):
        print("Current Value: ", self.combo_box.currentText())

    def set_value(self):
        self.combo_box.setCurrentIndex(3)
    
    def get_value(self):
        for i in range(self.combo_box.count()):
            print("Index [" , i , "] : ", self.combo_box.itemText(i))