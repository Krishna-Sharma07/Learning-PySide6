from PySide6.QtWidgets import QWidget, QCheckBox, QGroupBox, QButtonGroup, QRadioButton, QHBoxLayout, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox and Radios")

        group_box_1 = QGroupBox("Choose Operating System")

        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggles)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggles)

        mac = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggles)
        
        layout1 = QVBoxLayout()
        layout1.addWidget(windows)
        layout1.addWidget(linux)
        layout1.addWidget(mac)
        group_box_1.setLayout(layout1)

        drinks = QGroupBox("Drinks")
        beer = QCheckBox("Beer")
        coffee = QCheckBox("Coffee")
        juice = QCheckBox("Juice")
        juice.setChecked(True)

        exclusive = QButtonGroup(self)
        exclusive.addButton(juice)
        exclusive.addButton(coffee)
        exclusive.addButton(beer)
        exclusive.setExclusive(True)

        layout2 = QVBoxLayout()
        layout2.addWidget(beer)
        layout2.addWidget(juice)
        layout2.addWidget(coffee)
        drinks.setLayout(layout2)
        
        answer = QGroupBox("Choose Answer: ")
        a = QRadioButton("A")
        b = QRadioButton("B")
        c = QRadioButton("C")
        a.setChecked(True)

        layout3 = QVBoxLayout()
        layout3.addWidget(a)
        layout3.addWidget(b)
        layout3.addWidget(c)
        answer.setLayout(layout3)

        layout4 = QHBoxLayout()
        layout4.addWidget(group_box_1)
        layout4.addWidget(drinks)

        layout5 = QVBoxLayout()
        layout5.addLayout(layout4)
        layout5.addWidget(answer)
        
        self.setLayout(layout5)

    def windows_box_toggles(self, checked):
        if(checked):
            print("Windows Checked")
        else:
            print("Windows Unchecked")

    def linux_box_toggles(self, checked):
        if(checked):
            print("Linux Checked")
        else:
            print("Linux Unchecked")

    def mac_box_toggles(self, checked):
        if(checked):
            print("Mac Checked")
        else:
            print("Mac Unchecked")