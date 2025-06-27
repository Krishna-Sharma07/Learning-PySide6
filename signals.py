from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QPushButton, QSlider

def add_clicked(data):
    print("Task Added : ", data)

def respond_to_slider(data):
    print("Value: ", data)

app = QApplication()

"""button = QPushButton("Add")

button.setCheckable(True)
button.clicked.connect(add_clicked)
"""

slider = QSlider(Qt.Horizontal)

slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(1)
slider.valueChanged.connect(respond_to_slider)

slider.show()
app.exec()