from PySide6.QtWidgets import QTabWidget, QPushButton, QLineEdit, QLabel, QHBoxLayout,QVBoxLayout, QWidget

class Tab(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TabBar")

        tab_widget = QTabWidget(self)

        #information

        info = QWidget()
        info.setWindowTitle("Information")
        lable = QLabel("First Name: ")
        line_edit = QLineEdit()
        hlayout =QHBoxLayout()
        hlayout.addWidget(lable)
        hlayout.addWidget(line_edit)
        info.setLayout(hlayout)

        #button

        button = QWidget()
        button.setWindowTitle("Buttons")
        b1 = QPushButton("1")
        b2 = QPushButton("2")
        b3 = QPushButton("3")
        vlayout = QVBoxLayout()
        vlayout.addWidget(b1)
        vlayout.addWidget(b2)
        vlayout.addWidget(b3)
        button.setLayout(vlayout)

        tab_widget.addTab(info, "Information")
        tab_widget.addTab(button, "Buttons")

        layout = QVBoxLayout()
        layout.addWidget(tab_widget)

        self.setLayout(layout)